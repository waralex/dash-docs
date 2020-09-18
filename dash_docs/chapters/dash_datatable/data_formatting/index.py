from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import dash_table
from dash_docs import styles, tools
from dash_docs import reusable_components as rc

examples = tools.load_examples(__file__)

layout = html.Div([
    rc.Markdown('# DataTable - Number Formatting'),

    rc.Markdown(
    '''
    `DataTable` offers extensive number formatting and localization possibilities with the columns nested prop `format` and
    table-wide localization prop `local_format`.

    Most formatting and localization for columns can be done through the `dash_table.FormatTemplate`
    and `dash_table.Format` Python helpers but it's also possible to use the `d3-format`
    `specifier` and `locale` directly.
    '''),

    rc.Markdown(
    '''
    See [d3-format](https://github.com/d3/d3-format) for additional syntax details.
    '''),

    rc.Markdown(
    '''
    ## Using FormatTemplate

    The FormatTemplate provides the following predefined templates:

    - Money
    - Percentage
    '''),

    rc.Markdown(
        examples['data_formatting_formattemplate.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['data_formatting_formattemplate.py'][1],
        className='example-container'
    ),

    rc.Markdown(
    '''
    ## Using Format Helper
    '''),

    rc.Markdown('''
    ### Group
    '''),

    rc.Markdown(
        examples['data_formatting_format_group.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['data_formatting_format_group.py'][1],
        className='example-container'
    ),

    rc.Markdown('''
    ### Align and Fill
    '''),

    rc.Markdown(
        examples['data_formatting_format_fill.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['data_formatting_format_fill.py'][1],
        className='example-container'
    ),

    rc.Markdown('''
    ### Padding and Padding Width
    '''),

    rc.Markdown(
        examples['data_formatting_format_padding.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['data_formatting_format_padding.py'][1],
        className='example-container'
    ),

    rc.Markdown('''
    ### Precision and Scheme
    '''),

    rc.Markdown(
        examples['data_formatting_format_precision.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['data_formatting_format_precision.py'][1],
        className='example-container'
    ),

    rc.Markdown('''
    ### Sign
    '''),

    rc.Markdown(
        examples['data_formatting_format_sign.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['data_formatting_format_sign.py'][1],
        className='example-container'
    ),

    rc.Markdown('''
    ### Symbol
    '''),

    rc.Markdown(
        examples['data_formatting_format_symbol.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['data_formatting_format_symbol.py'][1],
        className='example-container'
    ),

    rc.Markdown('## Localization'),

    rc.Markdown(
        examples['data_formatting_format_localization.py'][0],
        style=styles.code_container
    ),
    html.Div(
        examples['data_formatting_format_localization.py'][1],
        className='example-container'
    )
])
