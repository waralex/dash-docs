import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {
    all,
    assocPath,
    concat,
    contains,
    filter,
    find,
    has,
    hasPath,
    path,
    pathOr,
    propOr,
    slice,
    without
} from 'ramda';

/*
 * event polyfill for IE
 * https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent/CustomEvent
 */
function CustomEvent(event, params) {
    // eslint-disable-next-line no-param-reassign
    params = params || {
        bubbles: false,
        cancelable: false,
        // eslint-disable-next-line no-undefined
        detail: undefined,
    };
    const evt = document.createEvent('CustomEvent');
    evt.initCustomEvent(
        event,
        params.bubbles,
        params.cancelable,
        params.detail
    );
    return evt;
}
CustomEvent.prototype = window.Event.prototype;

function traverse(obj, pathArray, func) {
    if (obj.chapters) {
        for(let i=0; i < obj.chapters.length; i++) {
            traverse(obj.chapters[i], pathArray.concat(['chapters', i]), func);
        }
    }
    func(obj, pathArray);
}

function searchChapter(chapter, searchWord) {
    return (searchWord) => {
        const terms = [
            'name', 'description', 'description_short',
            'url', 'meta_keywords'
        ];
        for(let i=0; i<terms.length; i++) {
            if(contains(searchWord.toLowerCase(), propOr('', terms[i], chapter).toLowerCase())) {
                return true;
            }
        }
        return false;
    }
}

function filterUrls (urls, search) {
    const matches = [];
    traverse({'chapters': urls}, [], function(o, pathArray) {
        let matched = true;
        const searchWords = without('', search.split(' '));

        if (all(searchChapter(o), searchWords)) {
            matches.push(pathArray);
        }

    })

    if(matches.length > 0) {
        let newObj = {};
        let searchResults = [];
        matches.forEach(matchPath => {
            const searchResult = {
                'names': []
            };
            for(let i=0; i<matchPath.length + 1; i++) {
                const namePath = concat(slice(0, i, matchPath), ['name']);
                if(hasPath(namePath, {'chapters': urls})) {
                    searchResult.names.push(path(namePath, {'chapters': urls}));
                }
            }
            searchResult.url = path(concat(matchPath, ['url']), {'chapters': urls});
            searchResult.description = path(concat(matchPath, ['description']), {'chapters': urls});
            searchResult.description_short = path(concat(matchPath, ['description_short']), {'chapters': urls});
            newObj = assocPath(matchPath, path(matchPath, {'chapters': urls}), newObj)
            searchResults.push(searchResult);
        });
        return {
            chapters: newObj.chapters,
            searchResults
        };
    }
    return {}
}

export default class Sidebar extends Component {
    constructor(props) {
        super(props);
        this.state = {search: ''};
    }

    render() {
        const {depth, urls} = this.props;
        let searchResults = [];
        if(this.state.search.length > 2) {
            searchResults = filterUrls(
                JSON.parse(JSON.stringify(urls)),
                this.state.search
            ).searchResults;
        }

        function handleKeyUp(event) {
            if (event.keyCode === 13) {
                if(searchResults.length > 0) {
                    window.history.pushState({}, '', searchResults[0].url);
                    window.dispatchEvent(new CustomEvent('_dashprivate_pushstate'));
                }
            }
        }

        return (
            <div className="sidebar">
                <input
                    autoFocus
                    tabindex="1"
                    type="text"
                    autocomplete="false"
                    value={this.state.search}
                    onChange={e => this.setState({search: e.target.value})}
                    onKeyUp={handleKeyUp}
                    placeholder={'Search'}
                />
                {
                    this.state.search.length > 2 ?
                    <SearchResults
                        search={this.state.search}
                        searchResults={searchResults}
                    />
                    :
                    <TreeSidebar
                        urls={urls}
                        depth={depth}
                    />
                }
            </div>
        );
    }
}

class SearchResults extends Component {
    render() {
        const {searchResults, search} = this.props;
        if (!searchResults || searchResults.length == 0) {
            return (
                <div className='no-results'>
                    <span>{'No results found. Try the same search on '}</span>
                    <a href={`https://google.com/search?q=site%3Adash.plot.ly+${search}`}>
                        Google
                    </a>
                    <span>{', '}</span>
                    <a href={`https://duckduckgo.com?q=site%3Adash.plot.ly+${search}`}>
                        Duck Duck Go
                    </a>
                    <span>{', or the '}</span>
                    <a href={`https://community.plot.ly/search?q=${search}%20category%3A16`}>
                        Dash Community Forum
                    </a>
                    <span>{'. '}</span>

                    <hr/>

                    <small>
                        {`No luck? Here is a more specific search by wrapping your
                        query in "quotes" on `}
                        <a href={`https://google.com/search?q=site%3Adash.plot.ly+"${search}"`}>
                            Google
                        </a>
                        <span>{', '}</span>
                        <a href={`https://duckduckgo.com?q=site%3Adash.plot.ly+"${search}"`}>
                            Duck Duck Go
                        </a>
                        <span>{', or the '}</span>
                        <a href={`https://community.plot.ly/search?q="${search}"%20category%3A16`}>
                            Dash Community Forum
                        </a>
                        <span>{'. '}</span>
                    </small>

                    <hr/>

                    <small>
                        <i>
                            {`Still no luck? Get help for what you are
                              looking for by opening a topic on the `}
                            <a href="https://community.plot.ly/c/dash">Dash Community Forum</a>
                            {'.'}
                        </i>
                    </small>
                </div>
            )
        }

        const resultItems = [];
        for(let i=0; i<searchResults.length; i++) {
            // Only display the last two names
            searchResults[i].name = searchResults[i].names.slice(
                searchResults[i].names.length - 2,
                searchResults[i].names.length
            ).join(' > ');
            resultItems.push(link(searchResults[i]));
        }

        return (
            <div>
                {resultItems}
            </div>
        );
    }
}

function link(chapter) {

    let title = null;
    if (chapter.description_short) {
        title = chapter.description_short.trim();
    } else if (chapter.description) {
        title = chapter.description.trim();
    }
    const active = window.location.pathname.trimRight('/') == chapter.url.trimRight('/');

    // TODO - Replace with a dcc.Link
    return (
        <a href={chapter.url} title={title} className={`${active ? 'active': ''}`}>
            {chapter.name}
        </a>
    );
}

class TreeSidebar extends Component {
    render() {
        const {all_open, depth, urls} = this.props;
        const chapter_elements = [];

        for(let i=0; i<urls.length; i++) {

            const chapter = urls[i];
            if(!chapter) {
                continue;
            } else if (chapter.chapters) {

                open = (
                    (
                        has('urls', chapter)
                        &&
                        Boolean(find(url =>
                             url.startsWith(window.location.pathname)
                        ), chapter.urls)
                    )
                    ||
                    Boolean(find(

                        subchapter => {
                            return (
                                propOr('', 'url', subchapter)
                                .startsWith(window.location.pathname)
                            );
                        },

                        chapter.chapters
                    ))
                );
                chapter_elements.push(
                    <details open={open}>
                        <summary>{chapter.name}</summary>
                        <TreeSidebar
                            all_open={all_open}
                            urls={chapter.chapters}
                            depth={depth+1}
                        />
                    </details>
                );

            } else {
                chapter_elements.push(link(chapter));

            }
        }

        return (
            <div className={`sidebar--${depth}`}>
                {chapter_elements}
            </div>
        )
    }
}

Sidebar.defaultProps = {
    depth: 0
};

Sidebar.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * URLs
     */
    urls: PropTypes.array,

    /**
     * depth
     */
    depth: PropTypes.number,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
