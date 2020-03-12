import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {replace} from 'ramda';

class PageMenu extends Component {
    constructor(props) {
        super(props);
        this.onLocationChanged = this.onLocationChanged.bind(this);
    }

    onLocationChanged() {
        this.forceUpdate();
    }

    componentDidMount() {
        this._clearOnLocationChanged = History.onChange(this.onLocationChanged);
    }

    componentWillUnmount() {
        this._clearOnLocationChanged();
    }

    render() {
        /*
         * Display links directly via setInterval because we don't know when the
         * headers will be rendered in the DOM
         */
        function renderPageMenuLinks() {
            if(document.getElementById('page-menu--links').innerText !== '') {
                window.clearInterval(renderPageMenuLinks);
                return;
            }
            const links = [];
            const elements = document.querySelectorAll('h1, h2, h3, h4, h5, h6');
            elements.forEach(el => {

                if (!el.href) {
                    el.id = `${replace(/ /g, '-', el.innerText).toLowerCase()}`;
                }
                /*
                 * TODO - Replace with a proper a and remove pageMenuScroll
                 * once https://github.com/plotly/dash-core-components/issues/769
                 * is fixed
                 */
                links.push(`
                    <div>
                        <span class="page-menu--link" onClick="pageMenuScroll('${el.id}')">
                            ${el.innerText}
                        </span>
                    </div>
                `);
            });
            document.getElementById('page-menu--links').innerHTML = links.join('');
        }
        window.setInterval(renderPageMenuLinks, 500);

        return (
            <div className='page-menu'>
                <div className='page-menu--header'>{'On This Page'}</div>
                <div id="page-menu--links"/>
            </div>
        )
    }
}

PageMenu.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};

export default PageMenu;
