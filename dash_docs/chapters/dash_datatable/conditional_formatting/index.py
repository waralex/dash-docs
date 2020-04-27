from collections import OrderedDict
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import os

import dash_table
from dash_docs import reusable_components as rc
from dash_docs import tools

from .heatmap_recipe import discrete_background_color_bins
discrete_background_color_bins_string = tools.read_file(os.path.join(
    os.path.dirname(__file__),
    'heatmap_recipe.py'
))
from .databars_recipes import data_bars, data_bars_diverging
databars_string = tools.read_file(os.path.join(
    os.path.dirname(__file__),
    'databars_recipes.py'
))


df_gapminder = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
data = OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)

df = pd.DataFrame(data)

data_election = OrderedDict(
    [
        (
            "Date",
            [
                "July 12th, 2013 - July 25th, 2013",
                "July 12th, 2013 - August 25th, 2013",
                "July 12th, 2014 - August 25th, 2014",
            ],
        ),
        (
            "Election Polling Organization",
            ["The New York Times", "Pew Research", "The Washington Post"],
        ),
        ("Rep", [1, -20, 3.512]),
        ("Dem", [10, 20, 30]),
        ("Ind", [2, 10924, 3912]),
        (
            "Region",
            [
                "Northern New York State to the Southern Appalachian Mountains",
                "Canada",
                "Southern Vermont",
            ],
        ),
    ]
)

df_election = pd.DataFrame(data_election)
df_long = pd.DataFrame(
    OrderedDict([(name, col_data * 10) for (name, col_data) in data.items()])
)
df_long_columns = pd.DataFrame(
    {
        "This is Column {} Data".format(i): [1, 2]
        for i in range(10)
    }
)
# TODO - ADD THIS TO THE MARKUP
# DRY this up too
wide_data = [
    {'Firm': 'Acme', '2017': 13, '2018': 5, '2019': 10, '2020': 4},
    {'Firm': 'Olive', '2017': 3, '2018': 3, '2019': 13, '2020': 3},
    {'Firm': 'Barnwood', '2017': 6, '2018': 7, '2019': 3, '2020': 6},
    {'Firm': 'Henrietta', '2017': -3, '2018': -10, '2019': -5, '2020': -6},
]
df_wide = pd.DataFrame(wide_data)

data_with_none = [
    {'Firm': 'Acme', '2017': '', '2018': 5, '2019': 10, '2020': 4},
    {'Firm': 'Olive', '2017': None, '2018': 3, '2019': 13, '2020': 3},
    {'Firm': 'Barnwood', '2017': np.NaN, '2018': 7, '2019': 3, '2020': 6},
    {'Firm': 'Henrietta', '2017': 14, '2018': 1, '2019': 13, '2020': 1},
]
df_with_none = pd.DataFrame(data_with_none)


Display = rc.CreateDisplay({
    'discrete_background_color_bins': discrete_background_color_bins,
    'data_bars': data_bars,
    'data_bars_diverging': data_bars_diverging,
    'dash_table': dash_table,
    'html': html,
    'df': df,
    'df_election': df_election,
    'df_long': df_long,
    'df_long_columns': df_long_columns,
    'df_wide': df_wide,
    'df_gapminder': df_gapminder,
    'df_with_none': df_with_none,
    'pd': pd
})


layout = html.Div(
    children=[

        rc.Markdown("""
        # Conditional Formatting

        Conditional formatting is provided through the `style_data_conditional`
        property. The `if` keyword provides a set of conditional formatting
        statements and the rest of the keywords are camelCased CSS properties.

        The `if` syntax supports three operators: `row_index`, `column_id`,
        and `filter_query`. `filter_query` is the most flexible option.
        Here is an example of all three:
        """),

        Display("""
        df['id'] = df.index
        result = dash_table.DataTable(
            data=df.to_dict('records'),
            sort_action='native',
            columns=[
                {"name": i, "id": i} for i in df.columns
                if i != 'id'
            ],
            style_data_conditional=[
                {
                    'if': {
                        'column_id': 'Region',
                    },
                    'backgroundColor': 'dodgerblue',
                    'color': 'white'
                },
                {
                    'if': {
                        'filter_query': '{Humidity} > 19 && {Humidity} < 41',
                        'column_id': 'Humidity'
                    },
                    'backgroundColor': 'tomato',
                    'color': 'white'
                },

                {
                    'if': {
                        'column_id': 'Pressure',

                        # since using .format, escape { with {{
                        'filter_query': '{{Pressure}} = {}'.format(df['Pressure'].max())
                    },
                    'backgroundColor': '#85144b',
                    'color': 'white'
                },

                {
                    'if': {
                        'row_index': 5,
                        'column_id': 'Region'
                    },
                    'backgroundColor': 'hotpink',
                    'color': 'white'
                },

                {
                    'if': {
                        'filter_query': '{id} = 4',
                        'column_id': 'Region'
                    },
                    'backgroundColor': 'RebeccaPurple'
                }
            ]
        )
        del df['id']  # no-display
        """),
        rc.Markdown(
        '''
        Notes:
        - `row_index` is absolute - if you filter or sort your table,
           the 5th row will remain highlighted. Try sorting the columns and
           notice how "San Francisco" remains highlighted but "London" does not.
        - `id` is a special hidden column that can be used as an alternative
        to `row_index` for highlighting data by index. Since each row has a
        unique `id`, the conditional formatting associated with this `id`
        will remain associated with that data after sorting and filtering.
        - `RebeccaPurple`, `hotpink`, `DogerBlue`... These are
        [named CSS colors](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#Color_keywords).
        We recommend avoiding the common color names like
        `red`, `blue`, `green`  as they look very outdated. For other color
        suggestions, see [http://clrs.cc/](http://clrs.cc/).
        - Since we're using `.format`, we escape `{` with `{{` and `}` with `}}`.
        - To highlight a row, omit `column_id`. To highlight a particular cell, include `column_id`.
        - Limitation - If the table is editable, then the maximum value could change
        if the user edits the table. Since this example hard codes the
        maximum value in the filter expression, the highlighting value
        would no longer be highlighted. As a workaround, you could update
        `style_data_conditional` via a callback whenever `derived_virtual_data` changes.
        This limitation applies for any conditional formatting with hardcoded
        numbers computed from an expression in Python
        (including many of the examples below!).
        See [plotly/dash-table#755](https://github.com/plotly/dash-table/issues/755) for updates.
        '''
        ),

        rc.Markdown(
        '''
        ## Alternative Highlighting Styles

        Instead of highlighting the background cell, you can change the color
        of the text, bold the text, add underlines, or style it using any
        other css property.
        '''
        ),

        Display("""
        from dash_table.Format import Format, Sign

        result = dash_table.DataTable(
            data=df.to_dict('records'),
            sort_action='native',
            columns=[
                {"name": i, "id": i} for i in df.columns
            ],
            style_data_conditional=[
                {
                    'if': {
                        'filter_query': '{Humidity} > 19 && {Humidity} < 41',
                        'column_id': 'Humidity'
                    },
                    'color': 'tomato',
                    'fontWeight': 'bold'
                },
                {
                    'if': {
                        'filter_query': '{Pressure} > 19',
                        'column_id': 'Pressure'
                    },
                    'textDecoration': 'underline'
                }
            ]
        )
        """),

        rc.Markdown(
        '''
        ### Special characters like emoji, stars, checkmarks, circles

        You can copy and paste emoji unicode characters directly into your code.
        We recommend copying values from emojipedia, e.g.
        [https://emojipedia.org/star/](https://emojipedia.org/star/).

        New unicode emoji characters are released every year and may not be
        available in the character sets of your audience's machines.
        The appearance of these icons differs on most operating systems.

        You may need to place `# -*- coding: utf-8 -*-` at the top of your code.
        '''
        ),

        Display("""
        # -*- coding: utf-8 -*-

        df['Rating'] = df['Humidity'].apply(lambda x:
            '⭐⭐⭐' if x > 30 else (
            '⭐⭐' if x > 20 else (
            '⭐' if x > 10 else ''
        )))
        df['Growth'] = df['Temperature'].apply(lambda x: '↗️' if x > 0 else '↘️')
        df['Status'] = df['Temperature'].apply(lambda x: '🔥' if x > 0 else '🚒')
        result = dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {"name": i, "id": i} for i in df.columns
            ],
        )

        del df['Status']  # no-display
        del df['Growth']  # no-display
        del df['Rating']  # no-display
        """),

        rc.Markdown(
        '''
        ## Filtering & Conditional Formatting Recipes

        ### Highlighting the max value in a column
        '''),
        Display("""
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {"name": i, "id": i} for i in df.columns
            ],
            style_data_conditional=[
                {
                    'if': {
                        'filter_query': '{{Pressure}} = {}'.format(df['Pressure'].max()),
                        'column_id': 'Pressure'
                    },
                    'backgroundColor': '#FF4136',
                    'color': 'white'
                },
            ]
        )
        """),

        rc.Markdown('### Highlighting a row with the min value'),

        Display("""
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {"name": i, "id": i} for i in df.columns
            ],
            style_data_conditional=[
                {
                    'if': {
                        'filter_query': '{{Temperature}} = {}'.format(df['Temperature'].min()),
                    },
                    'backgroundColor': '#FF4136',
                    'color': 'white'
                },
            ]
        )
        """),

        rc.Markdown('''
        ### Highlighting the top three or bottom three values in a column
        '''),
        Display("""
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {"name": i, "id": i} for i in df.columns
            ],
            style_data_conditional=(
                [
                    {
                        'if': {
                            'filter_query': '{{Temperature}} = {}'.format(i),
                            'column_id': 'Temperature',
                        },
                        'backgroundColor': '#0074D9',
                        'color': 'white'
                    }
                    for i in df['Temperature'].nlargest(3)
                ] +
                [
                    {
                        'if': {
                            'filter_query': '{{Pressure}} = {}'.format(i),
                            'column_id': 'Pressure',
                        },
                        'backgroundColor': '#7FDBFF',
                        'color': 'white'
                    }
                    for i in df['Pressure'].nsmallest(3)
                ]
            )
        )
        """),

        rc.Markdown('''
        ### Highlighting the max value in every row
        '''),
        Display(
        """
        def highlight_max_row(df):
            df_numeric_columns = df.select_dtypes('number').drop(['id'], axis=1)
            return [
                {
                    'if': {
                        'filter_query': '{{id}} = {}'.format(i),
                        'column_id': col
                    },
                    'backgroundColor': '#3D9970',
                    'color': 'white'
                }
                # idxmax(axis=1) finds the max indices of each row
                for (i, col) in enumerate(
                    df_numeric_columns.idxmax(axis=1)
                )
            ]

        df_wide['id'] = df_wide.index
        result = dash_table.DataTable(
            data=df_wide.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_wide.columns if i != 'id'],
            style_data_conditional=highlight_max_row(df_wide)
        )

        del df_wide['id']  # no-display
        """
        ),

        rc.Markdown('''
        ### Highlighting the top two values in a row
        '''),

        Display(
        '''
        def style_row_by_top_values(df, nlargest=2):
            numeric_columns = df.select_dtypes('number').drop(['id'], axis=1).columns
            styles = []
            for i in range(len(df)):
                row = df.loc[i, numeric_columns].sort_values(ascending=False)
                for j in range(nlargest):
                    styles.append({
                        'if': {
                            'filter_query': '{{id}} = {}'.format(i),
                            'column_id': row.keys()[j]
                        },
                        'backgroundColor': '#39CCCC',
                        'color': 'white'
                    })
            return styles

        df_wide['id'] = df_wide.index
        result = dash_table.DataTable(
            data=df_wide.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_wide.columns if i != 'id'],
            style_data_conditional=style_row_by_top_values(df_wide)
        )

        del df_wide['id']  # no-display
        '''),

        rc.Markdown('''
        ### Highlighting the maximum value in the table
        '''),

        Display(
        '''
        def style_table_by_max_value(df):
            if 'id' in df:
                numeric_columns = df.select_dtypes('number').drop(['id'], axis=1)
            else:
                numeric_columns = df.select_dtypes('number')
            max_across_numeric_columns = numeric_columns.max()
            max_across_table = max_across_numeric_columns.max()
            styles = []
            for col in max_across_numeric_columns.keys():
                if max_across_numeric_columns[col] == max_across_table:
                    styles.append({
                        'if': {
                            'filter_query': '{{{col}}} = {value}'.format(
                                col=col, value=max_across_table
                            ),
                            'column_id': col
                        },
                        'backgroundColor': '#39CCCC',
                        'color': 'white'
                    })
            return styles

        df_wide['id'] = df_wide.index
        result = dash_table.DataTable(
            data=df_wide.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_wide.columns if i != 'id'],
            style_data_conditional=style_table_by_max_value(df_wide)
        )

        del df_wide['id']  # no-display
        '''),

        rc.Markdown('''
        ### Highlighting a range of values
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df_wide.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_wide.columns],
            style_data_conditional=[
                {
                    'if': {
                        'filter_query': '{2018} >= 5 && {2018} < 10',
                        'column_id': '2018'
                    },
                    'backgroundColor': '#B10DC9',
                    'color': 'white'
                }
            ]
        )
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df_wide.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_wide.columns],
            style_data_conditional=[
                {
                    'if': {
                        'filter_query': '{{{col}}} >= 5 && {{{col}}} < 10'.format(col=col),
                        'column_id': col
                    },
                    'backgroundColor': '#B10DC9',
                    'color': 'white'
                } for col in df_wide.columns
            ]
        )
        '''),
        rc.Markdown(
        '''
        _Let's break down `{{{col}}}`. We want the final expression to look something like
        `{2017} > 5 & {2017} < 10` where 2017 is the name of the column.
        Since we're using `.format()`, we need to escape the brackets,
        so `{2017}` would be `{{2017}}`. Then, we need to replace `2017` with `{col}`
        for the find-and-replace, so `{{2017}}` becomes `{{{col}}}.format(col=col)`_
        '''
        ),

        rc.Markdown('''
        ### Highlighting top 10% or bottom 10% of values by column
        '''),
        Display(
        '''
        dash_table.DataTable(
            data=df_wide.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_wide.columns],
            style_data_conditional=[
                {
                    'if': {
                        'filter_query': '{{{}}} >= {}'.format(col, value),
                        'column_id': col
                    },
                    'backgroundColor': '#B10DC9',
                    'color': 'white'
                } for (col, value) in df_wide.quantile(0.9).iteritems()
            ]
        )
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df_wide.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_wide.columns if i != 'id'],
            style_data_conditional=[
                {
                    'if': {
                        'filter_query': '{{{}}} <= {}'.format(col, value),
                        'column_id': col
                    },
                    'backgroundColor': '#B10DC9',
                    'color': 'white'
                } for (col, value) in df_wide.quantile(0.1).iteritems()
            ]
        )
        '''),

        rc.Markdown('''
        ### Highlighting values above average and below average
        '''),

        rc.Markdown('Here, the highlighting is done _per column_'),
        Display(
        '''
        dash_table.DataTable(
            data=df_wide.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_wide.columns],
            style_data_conditional=(
                [
                    {
                        'if': {
                            'filter_query': '{{{}}} > {}'.format(col, value),
                            'column_id': col
                        },
                        'backgroundColor': '#3D9970',
                        'color': 'white'
                    } for (col, value) in df_wide.quantile(0.1).iteritems()
                ] +
                [
                    {
                        'if': {
                            'filter_query': '{{{}}} <= {}'.format(col, value),
                            'column_id': col
                        },
                        'backgroundColor': '#FF4136',
                        'color': 'white'
                    } for (col, value) in df_wide.quantile(0.5).iteritems()
                ]
            )
        )
        '''),

        rc.Markdown('Here, the highlighting is done _per table_'),
        Display(
        '''
        def highlight_above_and_below_max(df):
            df_numeric_columns = df.select_dtypes('number').drop(['id'], axis=1)
            mean = df_numeric_columns.mean().mean()
            return (
                [
                    {
                        'if': {
                            'filter_query': '{{{}}} > {}'.format(col, mean),
                            'column_id': col
                        },
                        'backgroundColor': '#3D9970',
                        'color': 'white'
                    } for col in df_numeric_columns.columns
                ] +
                [
                    {
                        'if': {
                            'filter_query': '{{{}}} <= {}'.format(col, mean),
                            'column_id': col
                        },
                        'backgroundColor': '#FF4136',
                        'color': 'white'
                    } for col in df_numeric_columns.columns
                ]
            )

        df_wide['id'] = df_wide.index
        result = dash_table.DataTable(
            data=df_wide.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_wide.columns if 'id' not in df_wide],
            style_data_conditional=highlight_above_and_below_max(df_wide)
        )
        del df_wide['id'] # no-display
        '''),

        rc.Markdown('''
        ### Highlighting empty strings
        '''),

        Display(
        '''
        result = html.Div([
            html.Pre(repr(df_with_none)),
            dash_table.DataTable(
                data=df_with_none.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df_with_none.columns],
                style_data_conditional=(
                    [
                        {
                            'if': {
                                'filter_query': '{{{}}} = ""'.format(col),
                                'column_id': col
                            },
                            'backgroundColor': 'tomato',
                            'color': 'white'
                        } for col in df_with_none.columns
                    ]
                )
            )
        ])
        '''
        ),

        rc.Markdown('### Highlighting None, NaN, or empty string values'),

        rc.Markdown('''
        Filter queries cannot match None, NaN, or null values. So, to match
        these values we have to convert these cells to an empty string.
        See [plotly/dash-table#768](https://github.com/plotly/dash-table/issues/768)
        for updates on support to do this without `.fillna`.
        '''),

        Display(
        '''
        df_with_none_copy = df_with_none.fillna('')
        result = html.Div([
            html.Pre(repr(df_with_none_copy)),
            dash_table.DataTable(
                data=df_with_none_copy.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df_with_none_copy.columns],
                style_data_conditional=(
                    [
                        {
                            'if': {
                                'filter_query': '{{{}}} = ""'.format(col),
                                'column_id': col
                            },
                            'backgroundColor': 'tomato',
                            'color': 'white'
                        } for col in df_with_none_copy.columns
                    ]
                )
            )
        ])
        '''
        ),

        rc.Markdown('''
        ### Displaying special values for `NaN` or `None` values
        '''),

        Display(
        '''
        from dash_table.Format import Format

        result = html.Div([
            html.Pre(repr(df_with_none)),
            dash_table.DataTable(
                data=df_with_none.to_dict('records'),
                columns=[
                    {
                        'name': i,
                        'id': i,
                        'type': 'numeric',
                        'format': Format(
                            nully='N/A'
                        )
                    } for i in df_with_none.columns
                ],
                editable=True
            )
        ])
        '''
        ),

        rc.Markdown('''
        Limitations:
        - `Format(nully=)` does not yet match for empty strings, only
        `None` values. See [plotly/dash-table#763](https://github.com/plotly/dash-table/issues/763)
        for updates.
        - `'type': 'numeric'` needs to be set, see [plotly/dash-table#762](https://github.com/plotly/dash-table/issues/762)
        for updates.

        An alternative method would be to fill in e.g. 'N/A' in the data before rendering:
        '''),

        Display(
        '''
        from dash_table.Format import Format

        df_with_none_copy = df_with_none.fillna('N/A').replace('', 'N/A')
        result = html.Div([
            html.Pre(repr(df_with_none_copy)),
            dash_table.DataTable(
                data=df_with_none_copy.to_dict('records'),
                columns=[{'name': i, 'id': i} for i in df_with_none_copy.columns],
                editable=True,
                style_data_conditional=[
                    {
                        'if': {
                            'filter_query': '{{{col}}} = "N/A"'.format(col=col),
                            'column_id': col
                        },
                        'backgroundColor': 'tomato',
                        'color': 'white'
                    } for col in df_with_none_copy.columns
                ]
            )
        ])
        '''
        ),

        rc.Markdown(
        '''
        Limitation: If your table is editable, then if a user deletes the
        contents of a cell, 'N/A' will no longer be displayed.
        This is unlike the example with `Format` where the `DataTable` will
        automatically display `N/A` for any empty cells, even after editing.
        '''
        ),

        rc.Markdown('''
        ### Highlighting text that contains a value
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {'name': i, 'id': i} for i in df.columns
            ],
            style_data_conditional=[
                {
                    'if': {
                        'filter_query': '{Region} contains "New"'
                    },
                    'backgroundColor': '#0074D9',
                    'color': 'white'
                }
            ]
        )
        '''
        ),

        rc.Markdown('''
        ### Highlighting text that equals a value
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {'name': i, 'id': i} for i in df.columns
            ],
            style_data_conditional=[
                {
                    'if': {
                        'filter_query': '{Region} = "San Francisco"'
                    },
                    'backgroundColor': '#0074D9',
                    'color': 'white'
                }
            ]
        )
        '''
        ),

        rc.Markdown('''
        ### Highlighting cells by value with a colorscale like a heatmap
        '''),

        rc.Markdown(
        '''
        This recipe shades cells with `style_data_conditional` and creates a
        legend with HTML components. You'll need to `pip install colorlover`
        to get the colorscales.
        '''
        ),

        rc.Syntax(discrete_background_color_bins_string),

        Display(
        '''

        (styles, legend) = discrete_background_color_bins(df_wide)

        result = html.Div([
            html.Div(legend, style={'float': 'right'}),
            dash_table.DataTable(
                data=df_wide.to_dict('records'),
                sort_action='native',
                columns=[{'name': i, 'id': i} for i in df_wide.columns],
                style_data_conditional=styles
            ),
        ])
        '''
        ),

        rc.Markdown('''
        ### Highlighting with a colorscale on a single column
        '''),

        Display(
        '''
        (styles, legend) = discrete_background_color_bins(df_wide, columns=['2018'])

        result = html.Div([
            legend,
            dash_table.DataTable(
                data=df_wide.to_dict('records'),
                sort_action='native',
                columns=[{'name': i, 'id': i} for i in df_wide.columns],
                style_data_conditional=styles
            )
        ])
        '''
        ),

        rc.Markdown('''
        ### Displaying data bars

        These recipes display a creative use of background `linear-gradient`
        colors to display horizontal bar charts within the table.
        Your mileage may vary! Feel free to modify these recipes for your own
        use.
        '''),

        rc.Syntax(databars_string),

        Display(
        '''
        df_gapminder_500 = df_gapminder[:500]
        result = dash_table.DataTable(
            data=df_gapminder_500.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_gapminder_500.columns],
            style_data_conditional=(
                data_bars(df_gapminder_500, 'lifeExp') +
                data_bars(df_gapminder_500, 'gdpPercap')
            ),
            style_cell={
                'width': '100px',
                'minWidth': '100px',
                'maxWidth': '100px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
            page_size=20
        )
        '''
        ),

        rc.Markdown('''
        ### Data bars without text

        Display the data bars without text by creating a new column and making
        the text transparent.
        '''),

        Display(
        '''
        df_gapminder['gdpPercap relative values'] = df_gapminder['gdpPercap']
        df_gapminder_500 = df_gapminder[:500]
        result = dash_table.DataTable(
            data=df_gapminder_500.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_gapminder_500.columns],
            style_data_conditional=(
                data_bars(df_gapminder_500, 'gdpPercap relative values') + [{
                    'if': {'column_id': 'gdpPercap relative values'},
                    'color': 'transparent'
                }]
            ),
            style_cell={
                'width': '100px',
                'minWidth': '100px',
                'maxWidth': '100px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
            page_size=20
        )

        del df_gapminder['gdpPercap relative values'] # no-display
        '''
        ),

        rc.Markdown('''
        ### Diverging data bars

        The `data_bars_diverging` function splits up the data into two quadrants
        by the midpoint.
        Alternative representations of data bars may split up the data by
        positive and negative numbers or by the average values.
        Your mileage may vary! Feel free to modify the `data_bars_diverging`
        function to your own visualization needs. If you create something new,
        please share your work on the [Dash Community Forum](https://community.plotly.com/tag/show-and-tell).
        '''),

        Display(
        '''
        df_gapminder_500 = df_gapminder[:500]
        result = dash_table.DataTable(
            data=df_gapminder_500.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_gapminder_500.columns],
            style_data_conditional=(
                data_bars_diverging(df_gapminder_500, 'lifeExp') +
                data_bars_diverging(df_gapminder_500, 'gdpPercap')
            ),
            style_cell={
                'width': '100px',
                'minWidth': '100px',
                'maxWidth': '100px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
            page_size=20
        )
        '''
        ),

        rc.Markdown('''
        ### Highlighting dates
        '''),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {'name': i, 'id': i}
                if i != 'Date' else
                {'name': 'Date', 'id': 'Date', 'type': 'datetime'}
                for i in df.columns
            ],
            style_data_conditional=[{
                'if': {'filter_query': '{Date} datestartswith "2015-10"'},
                'backgroundColor': '#85144b',
                'color': 'white'
            }]
        )
        '''
        ),

    ]
)
