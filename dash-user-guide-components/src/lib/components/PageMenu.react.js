import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {replace} from 'ramda';

function PageMenu(props) {

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
        const elements = document.querySelectorAll('h2, h3, h4, h5, h6');
        elements.forEach(el => {

            if (!el.href) {
                // TODO - Some kind of URL character replacement
                // TODO - Replace all, not just first occurance
                el.id = `${replace(' ', '-', el.innerText).toLowerCase()}`;
            }
            links.push(`
                <div>
                    <a href="#${el.id}">${el.innerText}</a>
                </div>
            `);
        });
        document.getElementById('page-menu--links').innerHTML = links.join('');
    }
    window.setInterval(renderPageMenuLinks, 500);

    return (
        <div className='page-menu'>
            <div>{'On This Page'}</div>
            <div id="page-menu--links"/>
        </div>
    )
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
