from collections import OrderedDict
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

import dash_table
from dash_docs import reusable_components as rc

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
wide_data = [
    {'Firm': 'Acme', '2017': 13, '2018': 5, '2019': 10, '2020': 4},
    {'Firm': 'Olive', '2017': 3, '2018': 3, '2019': 13, '2020': 3},
    {'Firm': 'Barnwood', '2017': 6, '2018': 7, '2019': 3, '2020': 6},
    {'Firm': 'Henrietta', '2017': 8, '2018': 1, '2019': 13, '2020': 1},
]
df_wide = pd.DataFrame(wide_data)

Display = rc.CreateDisplay({
    'dash_table': dash_table,
    'df': df,
    'df_election': df_election,
    'df_long': df_long,
    'df_long_columns': df_long_columns,
    'df_wide': df_wide,
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
        ## Filtering & Conditional Formatting Recipes

        ### Highlighting the max and min value in a column
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
            style_data_conditional=style_row_by_max(df_wide)
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
                        'filter_query': '{{{}}} >= 5 && {{{}}} < 10'.format(col, col),
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
        _Let's break down `{{{}}}`. We want the final expression to look something like
        `{2017} > 5 & {2017} < 10` where 2017 is the name of the column.
        Since we're using `.format()`, we need to escape the brackets,
        so `{2017}` would be `{{2017}}`. Then, we need to replace `2017` with `{}`
        for the find-and-replace, so `{{2017}}` becomes `{{{}}}`._
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
            columns=[{'name': i, 'id': i} for i in df_wide.columns],
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

        rc.Display(
        '''

        '''
        ),

        rc.Markdown('''
        ### Displaying special values for `NaN`, `None`, or empty strings
        '''),

        rc.Markdown('''
        ### Highlighting text that contains a value
        '''),

        rc.Markdown('''
        ### Highlighting text that equals a value
        '''),

        rc.Markdown('''
        ### Highlighting cells by value like a heatmap
        '''),

        rc.Markdown('''
        ### Displaying data bars
        '''),

        rc.Markdown('''
        ### Highlighting months
        '''),

        rc.Markdown('''
        ### Highlighting days
        '''),

        rc.Markdown(
        """
        ## Conditional Formatting via Pandas

        `filter_query` can be slow if you are writing many expressions.

        An easier and faster way to filter many cells is to perform the filter
        in the backend in Python and include the filter results as a hidden
        column.
        """
        ),

        rc.Markdown("""
        ## Highlighting Certain Rows by Index

        You can draw attention to certain rows by providing a unique
        background color, bold text, or colored text.
        """),
        Display("""
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {"name": i, "id": i} for i in df.columns
            ],
            style_data_conditional=[{
                "if": {"row_index": 4},
                "backgroundColor": "#3D9970",
                'color': 'white'
            }]
        )
        """),
        Display("""
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {"name": i, "id": i} for i in df.columns
            ],
            style_as_list_view=True,
            style_data_conditional=[{
                "if": {"row_index": 4},
                "fontWeight": "bold"
            }]
        )
        """),

        rc.Markdown("""
        ## Highlighting Columns

        Similarly, certain columns can be highlighted.
        """),
        Display("""
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {'name': i, 'id': i} for i in df.columns
            ],
            style_data_conditional=[{
                'if': {'column_id': 'Temperature'},
                'backgroundColor': '#3D9970',
                'color': 'white',
            }]
        )
        """),

        rc.Markdown("""
        ## Highlighting Cells

        You can also highlight certain cells. For example, you may want to
        highlight certain cells that exceed a threshold or that match
        a filter elsewhere in the app.

        The `filter` keyword in `style_data_conditional` uses the same
        filtering expression language as the table's interactive filter UI.
        """),
        Display("""
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[
                {'name': i, 'id': i} for i in df.columns
            ],
            style_data_conditional=[
                {
                    'if': {
                        'column_id': 'Region',
                        'filter_query': '{Region} == "Montreal"'
                    },
                    'backgroundColor': '#3D9970',
                    'color': 'white',
                },
                {
                    'if': {
                        'column_id': 'Humidity',
                        'filter_query': '{Humidity} == 20'
                    },
                    'backgroundColor': '#3D9970',
                    'color': 'white',
                },
                {
                    'if': {
                        'column_id': 'Temperature',
                        'filter_query': '''
                            {Temperature} > 3.9 && {Temperature} < 5.1
                        '''
                    },
                    'backgroundColor': '#3D9970',
                    'color': 'white',
                },
                {
                    'if': {
                        'column_id': 'Temperature',
                        'filter_query': '{Date} datestartswith 2019-01'
                    },
                    'backgroundColor': '#3D9970',
                    'color': 'white',
                },

                {
                    'if': {
                        'column_id': 'Temperature',
                        'filter_query': '{Date} datestartswith 2019-02-05'
                    },
                    'backgroundColor': '#3D9970',
                    'color': 'white',
                },

                {
                    'if': {
                        'filter_query': '{id} = 1'
                    },
                    'backgroundColor': '#3D9970',
                    'color': 'white',
                },

                {
                    'if': {
                        'filter_query': '{Temperature} > {Humidity}'
                    },
                    'backgroundColor': '#3D9970',
                    'color': 'white',
                },

            ]
        )
        """),


        rc.Markdown(
        '''
        ## Highlighting thousands of cells

        If you are highlighting thousands of cells, this can slow down.
        '''
        )
        # TODO - Example of a hidden column with something like {highlight}=1

    ]
)
