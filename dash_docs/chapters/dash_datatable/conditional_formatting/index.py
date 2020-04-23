from collections import OrderedDict
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np

import dash_table
from dash_docs import reusable_components as rc


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
    {'Firm': 'Henrietta', '2017': 14, '2018': 1, '2019': 13, '2020': 1},
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
        dash_table.DataTable(
            data=df.to_dict('records'),
            sort_action='native',
            columns=[
                {"name": i, "id": i} for i in df.columns
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

                        # since using format, escape { with {{
                        'filter_query': '{{Pressure}} = {}'.format(df['Pressure'].max())
                    },
                    'backgroundColor': '#85144b',
                    'color': 'white'
                },

                {
                    'if': {
                        'row_index': 5
                    },
                    'backgroundColor': 'hotpink',
                    'color': 'white'
                },
            ]
        )
        """),
        rc.Markdown(
        '''
        Notes:
        - `row_index` is absolute - if you filter or sort your table, the highlighted row will not change.
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
                {"name": i, "id": i}
                if i != 'Temperature' else
                {
                    'name': i, 'id': i,
                    'type': 'numeric',
                    'format': Format(sign=Sign.parantheses)
                }
                for i in df.columns
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

        rc.Markdown(
        '''
        Notes:
        - Since we're using `.format`, we escape `{` with `{{` and `}` with `}}`.
        - To highlight a row, omit `column_id`. To highlight a particular cell, include `column_id`.
        - `#FF4136` was taken from [clrs.css](http://clrs.cc/), a nice list of common colors.
        You can also use [named CSS colors](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#Color_keywords),
        but recommend avoiding the common color names like `red`, `blue`, `green`  as they look very outdated.
        - **Limitation** - If the table is editable, then the maximum value could change
        if the user edits the table. Since this example hard codes the
        maximum value in the filter expression, the highlighting value
        would no longer be highlighted.
        See [plotly/dash-table#755](https://github.com/plotly/dash-table/issues/755) for updates.
        '''
        ),

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
        rc.Markdown(
        '''
        Notes:
        - As above, if this table was editable, the largest values could
        change through user interaction while `style_data_conditional` would be
        highlighting the (outdated) original largest values.
        See [plotly/dash-table#756](https://github.com/plotly/dash-table/issues/756)
        for updates.
        '''
        ),

        rc.Markdown('''
        ### Highlighting the max value in every row
        '''),
        Display(use_exec=True, example_string=
        """
        df_wide['id'] = df_wide.index
        result = dash_table.DataTable(
            data=df_wide.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_wide.columns if i != 'id'],
            style_data_conditional=[
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
                    df_wide[['2017', '2018', '2019', '2020']].idxmax(axis=1)
                )
            ]
        )
        """
        ),
        rc.Markdown(
        '''
        Notes:
        - `id` is what we refer to as "row ids". It is included in `data` but not
        displayed within columns.
        Creating a `filter_query` with `id` is more robust than using `row_index`
        as the row indices remain the same after sorting or filtering whereas
        `id` is associated with original row of data.
        - As in the other examples, if the table is editable, the user could change the values
        in the rows which could lead to incorrect highlighting.
        See [plotly/dash-table#759](https://github.com/plotly/dash-table/issues/759) for updates.
        '''
        ),

        rc.Markdown('''
        ### Highlighting the top two values in a row
        '''),

        Display(use_exec=True, example_string=
        '''
        def style_row_by_top_values(df, columns, nlargest):
            styles = []
            for i in range(len(df)):
                row = df.loc[i, columns].sort_values(ascending=False)
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
            style_data_conditional=style_row_by_top_values(
                df_wide, ['2017', '2018', '2019', '2020'], 2
            )
        )
        '''),

        rc.Markdown('''
        ### Highlighting the maximum value in the table
        '''),

        Display(use_exec=True, example_string=
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
        ### Highlighting top 10% or bottom 10% of values
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
            mean = df.mean().mean()
            return (
                [
                    {
                        'if': {
                            'filter_query': '{{{}}} > {}'.format(col, mean),
                            'column_id': col
                        },
                        'backgroundColor': '#3D9970',
                        'color': 'white'
                    } for col in df.columns
                ] +
                [
                    {
                        'if': {
                            'filter_query': '{{{}}} <= {}'.format(col, mean),
                            'column_id': col
                        },
                        'backgroundColor': '#FF4136',
                        'color': 'white'
                    } for col in df.columns
                ]
            )

        result = dash_table.DataTable(
            data=df_wide.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_wide.columns],
            style_data_conditional=highlight_above_and_below_max(df_wide)
        )
        '''),

        rc.Markdown('''
        ### Highlighting `NaN`, `None`, or empty strings
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
                            'backgroundColor': 'tomato'
                        } for col in df_with_none.columns
                    ] +
                    [
                        {
                            'if': {
                                # TODO - This doesn't work?
                                'filter_query': '{{{}}} = null'.format(col),
                                'column_id': col
                            },
                            'backgroundColor': 'tomato'
                        } for col in df_with_none.columns
                    ]
                )
            )

        ])
        '''
        ),

        rc.Markdown('''
        ### Displaying special values for `NaN`, `None`, or empty strings
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
                ]
            )
        ])
        '''
        ),

        # TODO - Clean up this language
        rc.Markdown(
        '''
        **Limitations**
        - 'type': 'numeric' needs to be set: https://github.com/plotly/dash-table/issues/762
        - doesn't handle empty strings: https://github.com/plotly/dash-table/issues/763
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

        Display(
        '''
        import colorlover

        def discrete_background_color_bins(df, n_bins=5, columns='all'):
            bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
            if columns == 'all':
                if 'id' in df:
                    numeric_columns = df.select_dtypes('number').drop(['id'], axis=1)
                else:
                    numeric_columns = df.select_dtypes('number')
            else:
                numeric_columns = columns
            df_max = numeric_columns.max().max()
            df_min = numeric_columns.min().min()
            ranges = [
                ((df_max - df_min) * i) + df_min
                for i in bounds
            ]
            styles = []
            for i in range(1, len(bounds)):
                min_bound = ranges[i - 1]
                max_bound = ranges[i]
                for column in numeric_columns:
                    styles.append({
                        'if': {
                            'filter_query': (
                                '{{{column}}} >= {min_bound}' +
                                (' && {{{column}}} < {max_bound}' if (i < len(bounds) - 1) else '')
                            ).format(column=column, min_bound=min_bound, max_bound=max_bound),
                            'column_id': column
                        },
                        'backgroundColor': colorlover.scales[str(n_bins)]['seq']['Blues'][i - 1],
                        'color': 'white' if i > len(bounds) / 2. else 'inherit'
                    })
            return styles

        result = dash_table.DataTable(
            data=df_wide.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_wide.columns],
            style_data_conditional=discrete_background_color_bins(df_wide)
        )
        '''
        ),

        rc.Markdown('''
        ### Highlighting with a colorscale on a single column
        '''),

        Display(
        '''
        import colorlover

        def discrete_background_color_bins(df, n_bins=5, columns='all'):
            bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
            if columns == 'all':
                if 'id' in df:
                    numeric_columns = df.select_dtypes('number').drop(['id'], axis=1)
                else:
                    numeric_columns = df.select_dtypes('number')
            else:
                numeric_columns = df[columns]
            df_max = numeric_columns.max().max()
            df_min = numeric_columns.min().min()
            ranges = [
                ((df_max - df_min) * i) + df_min
                for i in bounds
            ]
            styles = []
            for i in range(1, len(bounds)):
                min_bound = ranges[i - 1]
                max_bound = ranges[i]
                for column in numeric_columns:
                    styles.append({
                        'if': {
                            'filter_query': (
                                '{{{column}}} >= {min_bound}' +
                                (' && {{{column}}} < {max_bound}' if (i < len(bounds) - 1) else '')
                            ).format(column=column, min_bound=min_bound, max_bound=max_bound),
                            'column_id': column
                        },
                        'backgroundColor': colorlover.scales[str(n_bins)]['seq']['Blues'][i - 1],
                        'color': 'white' if i > len(bounds) / 2. else 'inherit'
                    })
            return styles

        result = dash_table.DataTable(
            data=df_wide.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_wide.columns],
            style_data_conditional=discrete_background_color_bins(
                df_wide,
                columns=['2018']
            )
        )
        '''
        ),

        rc.Markdown('''
        ### Displaying data bars
        '''),

        Display(
        '''
        def data_bars(df, column):
            styles = []
            col_max = df[column].max()
            col_min = df[column].min()
            for value in df[column]:
                percentage = 100 * (value - col_min) / (col_max - col_min)
                styles.append({
                    'if': {
                        'filter_query': (
                            '{{{column}}} = {value}'
                        ).format(column=column, value=value),
                        'column_id': column
                    },
                    'background': (
                        """
                            linear-gradient(90deg,
                            #0074D9 0%,
                            #0074D9 {percentage}%,
                            white {percentage}%,
                            white 100%)
                        """.format(percentage=percentage)
                    )
                })
            return styles


        result = dash_table.DataTable(
            data=df_gapminder.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_gapminder.columns],
            style_data_conditional=(
                data_bars(df_gapminder, 'lifeExp') +
                data_bars(df_gapminder, 'gdpPercap')
            ),
            # TODO - These widths aren't right...
            style_cell={
                'width': '{}%'.format(100. / len(df_gapminder.columns)),
                'minWidth': '{}%'.format(100. / len(df_gapminder.columns)),
                'maxWidth': '{}%'.format(100. / len(df_gapminder.columns)),
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
            page_size=20
        )
        '''
        ),

        rc.Markdown('''
        ### Displaying data bars
        '''),

        Display(
        '''
        def data_bars_diverging(df, column, color_above='#3D9970', color_below='#FF4136'):
            styles = []
            col_max = df[column].max()
            col_min = df[column].min()
            midpoint = (col_max + col_min) / 2.

            for value in df[column]:
                percentage = 100. * (value - col_min) / (col_max - col_min)
                if value > midpoint:
                    background = (
                        """
                            linear-gradient(90deg,
                            white 0%,
                            white 50%,
                            {color_above} 50%,
                            {color_above} {percentage}%,
                            white {percentage}%,
                            white 100%)
                        """.format(percentage=percentage, color_above=color_above)
                    )
                else:
                    background = (
                        """
                            linear-gradient(90deg,
                            white 0%,
                            white {percentage}%,
                            {color_below} {percentage}%,
                            {color_below} 50%,
                            white 50%,
                            white 100%)
                        """.format(percentage=percentage, color_below=color_below)
                    )

                styles.append({
                    'if': {
                        'filter_query': (
                            '{{{column}}} = {value}'
                        ).format(column=column, value=value),
                        'column_id': column
                    },
                    'background': background
                })
            return styles

        result = dash_table.DataTable(
            data=df_gapminder.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_gapminder.columns],
            style_data_conditional=(
                data_bars_diverging(df_gapminder, 'lifeExp') +
                data_bars_diverging(df_gapminder, 'gdpPercap')
            ),
            # TODO - These widths aren't right...
            style_cell={
                'width': '{}%'.format(100. / len(df_gapminder.columns)),
                'minWidth': '{}%'.format(100. / len(df_gapminder.columns)),
                'maxWidth': '{}%'.format(100. / len(df_gapminder.columns)),
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
            page_size=20
        )
        '''
        ),

        # TODO - Maybe incorporate this into the computation above since it
        # is faster if the number of bins is less than the number of unique
        # values. Check to see what the granularity looks like with 100 bins,
        # maybe you won't be able to tell a difference?
        rc.Markdown(
        '''
        ### Discretized Data Bars
        '''
        ),
        Display(
        '''
        def quantiles(df, column):
            n_bins = 100
            bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
            ranges = [
                ((df[column].max() - df[column].min()) * i) + df[column].min()
                for i in bounds
            ]
            styles = []
            for i in range(1, len(bounds)):
                min_bound = ranges[i - 1]
                max_bound = ranges[i]
                max_bound_percentage = bounds[i] * 100
                styles.append({
                    'if': {
                        'filter_query': (
                            '{{{column}}} >= {min_bound}' +
                            (' && {{{column}}} < {max_bound}' if (i < len(bounds) - 1) else '')
                        ).format(column=column, min_bound=min_bound, max_bound=max_bound),
                        'column_id': column
                    },
                    'background': (
                        """
                            linear-gradient(90deg,
                            #0074D9 0%,
                            #0074D9 {max_bound_percentage}%,
                            white {max_bound_percentage}%,
                            white 100%)
                        """.format(max_bound_percentage=max_bound_percentage)
                    )
                })

            return styles

        result = dash_table.DataTable(
            data=df_gapminder.to_dict('records'),
            sort_action='native',
            columns=[{'name': i, 'id': i} for i in df_gapminder.columns],
            style_data_conditional=(
                quantiles(df_gapminder, 'lifeExp')
            ),
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
