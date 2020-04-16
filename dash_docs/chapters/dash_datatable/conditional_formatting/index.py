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

Display = rc.CreateDisplay({
    'dash_table': dash_table,
    'df': df,
    'df_election': df_election,
    'df_long': df_long,
    'df_long_columns': df_long_columns,
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
                        'row_index': 5
                    },
                    'backgroundColor': 'hotpink',
                    'color': 'white'
                },
                {
                    'if': {
                        'column_id': 'Region',
                    },
                    'backgroundColor': '#0074D9',
                    'color': 'white'
                },
                {
                    'if': {
                        'filter_query': '{Humidity} > 19 && {Humidity} < 41',
                        'column_id': 'Humidity'
                    },
                    'backgroundColor': '#3D9970',
                    'color': 'white'
                },
            ]
        )
        """),

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
