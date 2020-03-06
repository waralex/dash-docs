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
import * as R from 'ramda';

window.assocPath = assocPath;
window.contains = contains;
window.filter = filter;
window.find = find;
window.path = path;
window.propOr = propOr;

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
            if(contains(searchWord, propOr('', terms[i], chapter).toLowerCase())) {
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
    window.matches = matches;

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

window.filterUrls = filterUrls;

export default class Sidebar extends Component {
    constructor(props) {
        super(props);
        this.state = {search: ''};
    }

    render() {
        if (this.props.depth == 0 && !window.URLS) {
            window.URLS = JSON.parse(JSON.stringify(this.props.urls));
        }
        const {depth, urls} = this.props;
        let searchResults = [];
        if(this.state.search.length > 2) {
            searchResults = filterUrls(
                JSON.parse(JSON.stringify(urls)),
                this.state.search
            ).searchResults;
        }

        function handleLocationChange() {
            if(searchResults.length > 0) {
                window.history.pushState({}, '', searchResults[0].url);
                window.dispatchEvent(new CustomEvent('_dashprivate_pushstate'));
            }
        }

        function handleKeyUp(event) {
            if (event.keyCode === 13) {
                handleLocationChange();
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
        const {searchResults} = this.props;
        if (!searchResults || searchResults.length == 0) {
            return 'No results found';
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
        // todo strip
        title = chapter.description_short;
    } else if (chapter.description) {
        title = chapter.description;
    }
    const active = window.location.pathname.trimRight('/') == chapter.url.trimRight('/');

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

                // Assume that a chapter's path matches that of its parent
                // TODO - find the first relative link
                console.warn('CHECKING OPEN');
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
