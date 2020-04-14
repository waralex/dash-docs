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
moby_dick_text = [
    'Call me Ishmael. ',
    ''.join([
        'Some years ago- never mind how long precisely- having little or no money ',
        'in my purse, and nothing particular to interest me on shore, ',
        'I thought I would sail about a little and see the watery part of the world. ',
    ]),
    'It is a way I have of driving off the spleen and regulating the circulation.'
]

moby_dick = OrderedDict(
    [
        (
            'Sentence Number', [i+1 for i in range(len(moby_dick_text))],
        ),
        (
            'Text', [i for i in moby_dick_text]
        )
    ]
)

data_numeric = pd.DataFrame(OrderedDict(
    [
        [
            'Column {}'.format(i + 1), list(range(30))
        ] for i in range(15)
    ]
))

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

many_columns = OrderedDict(
    [
        ('Column {}'.format(i+1), [51231.431, 3124.31, 1234.124, 122412.31])
        for i in range(15)
    ]
)
df_15_columns = pd.DataFrame(many_columns)
df_moby_dick = pd.DataFrame(moby_dick)

df_numeric = pd.DataFrame(data_numeric)

Display = rc.CreateDisplay({
    'dash_table': dash_table,
    'html': html,
    'df': df,
    'df_election': df_election,
    'df_long': df_long,
    'df_long_columns': df_long_columns,
    'df_15_columns': df_15_columns,
    'df_moby_dick': df_moby_dick,
    'df_numeric': df_numeric,
    'pd': pd
})


layout = html.Div(
    children=[
        rc.Markdown(
        '''
        # DataTable Height

        By default, the table's height will expand in order
        to render up to 250 rows.
        After 250 rows, the table with display a **pagination** UI
        that allows you to navigate through 250 rows at a time.
        '''
        ),

        rc.Markdown(
        '''
        > The set of examples on this page are rendered with a few different
        > dataframes that have different sizes and shapes. In particular,
        > some of the dataframes have a large number of columns or have cells
        > with long contents. If you'd like to follow along on your own
        > machine, then open up the menu below to copy and paste
        > the code behind these datasets.
        '''
        ),

        html.Details(open=False, children=[
            html.Summary('View the Datasets'),
            rc.Markdown(
            '''
            ```python
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

            many_columns = OrderedDict(
                [
                    ('Column {}'.format(i), [51231.431, 3124.31, 1234.124, 122412.31])
                    for i in range(15)
                ]
            )

            election_data = OrderedDict(
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

            data_numeric = pd.DataFrame(OrderedDict(
                [
                    [
                        'Column {}'.format(i + 1), list(range(30))
                    ] for i in range(15)
                ]
            ))

            moby_dick_text = [
                'Call me Ishmael. ',
                ''.join([
                    'Some years ago- never mind how long precisely- having little or no money ',
                    'in my purse, and nothing particular to interest me on shore, ',
                    'I thought I would sail about a little and see the watery part of the world. ',
                ]),
                'It is a way I have of driving off the spleen and regulating the circulation.'
            ]

            moby_dick = OrderedDict(
                [
                    (
                        'Sentence Number', [i+1 for i in range(len(moby_dick_text))],
                    ),
                    (
                        'Text', [i for i in moby_dick_text]
                    )
                ]
            )

            df_election = pd.DataFrame(election_data)
            df_long = pd.DataFrame(
                OrderedDict([(name, col_data * 10) for (name, col_data) in election_data.items()])
            )
            df_long_columns = pd.DataFrame(
                {
                    "This is Column {} Data".format(i): [1, 2]
                    for i in range(10)
                }
            )
            df_15_columns = pd.DataFrame(many_columns)
            df_numeric = pd.DataFrame(data_numeric)
            df_moby_dick = pd.DataFrame(long_cells)
            ```
            ''')
        ]),

        rc.Markdown(
        '''
        ## Setting Table Height with Pagination

        If you are using pagination, you can set the height by displaying
        less rows at a time. Instead of 250 rows, you could display
        10 rows at a time. By default and without wrapping,
        each row takes up 30px. So 10 rows with one header would set the
        table to be 330px tall. The pagination UI itself is around 60px tall.
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df_long.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            page_size=10
        )
        '''),

        rc.Markdown(
        '''
        <blockquote>
        In this example, the pagination is done natively in the browser:
        all of the data is sent upfront to the browser and
        Dash renders new pages as you click on the buttons. You can also
        do pagination in the backend so that only 10 rows are sent to the
        browser at a time (lowering network costs and memory). This is a good
        strategy if you have more than 10,000-50,000 rows.
        <dccLink children="Learn about backend pagination" href="/datatable/callbacks"/>.
        </blockquote>
        '''
        ),

        rc.Markdown(
        '''
        ## Setting Table Height with Vertical Scroll

        If you have less than ~1000 rows, then you could remove pagination,
        constrain the height, and display a vertical scrollbar.

        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df_long.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            page_action='none',
            style_table={'height': '300px', 'overflowY': 'auto'}
        )
        '''),

        rc.Markdown(
        '''
        **Limitations**

        If you have more than 1000 rows, then the browser will slow
        down when trying to render the table. With more than 1000 rows, we
        recommend switching to browser or server pagination (as above) or
        virtualization (as below).
        '''
        ),

        rc.Markdown(
        '''
        ### Vertical Scroll With Pagination

        If you have more than ~1000 rows, then you could keep pagination at
        the bottom of the table, constrain the height, and display a
        vertical scrollbar.
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df_long.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            page_size=20,  # we have less data in this example, so setting to 20
            style_table={'height': '300px', 'overflowY': 'auto'}
        )
        '''),

        rc.Markdown(
        '''
        ### Vertical Scroll With Fixed Headers

        You can also fix headers so that the table content scrolls but the
        headers remain visible.
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df_long.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            fixed_rows={'headers': True},
            style_table={'height': 400}  # defaults to 500
        )
        '''),

        rc.Markdown(
        '''
        **Limitations**

        If a column header is wider than the data within that column and the
        table's container isn't wide enough to display the headers,
        then the column will be as wide as the data and the header text
        will overflow onto the next column. This is a bug.
        The current workaround is to hide the overflow or
        <dccLink children="fix the width of the columns in pixels" href="/datatable/width"/>.
        See [plotly/dash-table#740](https://github.com/plotly/dash-table/issues/740) for updates.

        There are also a few limitations with this workaround:

        1. In those scenarios where the header is cut off, it is not possible
        to set ellipses within the header.
        See [plotly/dash-table#735](https://github.com/plotly/dash-table/issues/735) for updates.
        2. When the text is cutoff, it is useful to display tooltips displaying the
        entire text. It is not yet possible to add tooltips to headers.
        See [plotly/dash-table#295](https://github.com/plotly/dash-table/issues/295) for updates.
        3. If the header text is cut-off, then the header overflow is visible.
        The current workaround is to hide the overflow with `overflow: 'hidden'`.
        '''
        ),

        rc.Markdown(
        '''
        **Example of the limitation**

        This limitation will only happen if the headers are wider than the
        cells and the table's container isn't wide enough to display all of the
        headers:
        '''
        ),

        Display(
        '''
        dash_table.DataTable(
            data=df_numeric.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_numeric.columns],
            fixed_rows={'headers': True}
        )
        '''),

        rc.Markdown(
        '''
        **Workaround Option 1: Hiding the header overflow**
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df_numeric.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_numeric.columns],
            fixed_rows={'headers': True},
            style_header={
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'maxWidth': 0,
            },
        )
        '''),

        rc.Markdown(
        '''
        **Workaround Option 2: Fixing the width of the columns**
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df_numeric.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_numeric.columns],
            fixed_rows={'headers': True},
            style_cell={
                'minWidth': 95, 'maxWidth': 95, 'width': 95
            }
        )
        '''),

        rc.Markdown(
        '''
        **Workaround Option 3: Setting the width of the table**
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df_numeric.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_numeric.columns],
            fixed_rows={'headers': True},
            style_table={
                'width': 95 * len(df_numeric.columns),
                'overflowY': 'auto',
                'overflowX': 'auto'
            }
        )
        '''),

        rc.Markdown(
        '''
        ### Vertical Scroll with Virtualization

        As mentioned above, the browser has difficultiy rendering 1000s of
        rows in a table. Virtualization works around rendering performance
        issues in the web browser by rendering rows _on the fly_ as you scroll.

        All of the data for your table will still be sent over the network
        to the browser, so if you are displaying more than 10,000-100,000 rows
        you may consider using <dccLink href="/datatable/calblacks" children="backend pagination"/>
        to reduce the network costs and memory usage.
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df_numeric.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_numeric.columns],
            virtualization=True,
            fixed_rows={'headers': True},
            style_cell={'minWidth': 95, 'width': 95, 'maxWidth': 95},
            style_table={'height': 300}  # default is 500
        )
        '''),

        rc.Markdown(
        '''
        **Limitations**

        1. With virtualization, the browser doesn't know the width of the columns
        in advance; it can only determine the width of the columns when they
        are rendered. So, your columns may change size as you scroll unless
        you <dccLink href="/datatable/width" children="fix the column widths"/>.
        2. Since, with virtualization, we're rendering rows _on the fly_ as we scroll,
        the rendering performance will be slower than the browser-optimized
        native vertical scrolling. You may notice that table will appear blank
        for an instance before the cells are rendered if you scroll quickly.
        3. The same `fixed_rows` limitations exist as mentioned above.
        '''
        ),

        rc.Markdown(
        '''
        ## Expanding to the height of the container

        In some cases, you may not be able to set height of the table itself,
        you may only have control over setting the height of the container.
        For example, if your container is responsive and changes based off
        of the height of other elements on the page.

        In this case, you can set the overflow within the table.
        '''
        ),

        Display(
        '''
        html.Div(
            style={'height': 300},
            children=dash_table.DataTable(
                data=df_numeric.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in df_numeric.columns],
                virtualization=True,
                fixed_rows={'headers': True},
                style_cell={'minWidth': 95, 'width': 95, 'maxWidth': 95},
                style_table={'height': '100%'},
                css=[{'selector': '#table', 'rule': 'height: 100%'}]
            )
        )
        '''),

        Display(
        '''
        html.Div(
            style={'height': 300},
            children=dash_table.DataTable(
                data=df_numeric.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in df_numeric.columns],
                style_cell={'minWidth': 95, 'width': 95, 'maxWidth': 95},
                style_table={'height': '100%', 'overflowY': 'auto'},
                css=[{'selector': '#table', 'rule': 'height: 100%'}]
            )
        )
        '''),

        Display(
        '''
        html.Div(
            style={'height': 300},
            children=dash_table.DataTable(
                data=df_numeric.to_dict('records'),
                columns=[{'id': c, 'name': c} for c in df_numeric.columns],
                style_cell={'minWidth': 95, 'width': 95, 'maxWidth': 95},
                fixed_rows={'headers': True},
                style_table={'height': '100%'},
                css=[{'selector': '#table', 'rule': 'height: 100%'}]
            )
        )
        '''),

        rc.Markdown("## Height vs Max Height"),
        rc.Markdown(
        '''
        With `max-height`, if the table's contents are shorter than the
        `max-height`, then the container will be shorter.
        If you want a container with a constant height no matter the
        contents, then use `height`.

        Here, we're setting max-height to 300, or the height of the pink line.
        Note how the table renders shorter than this line.
        '''),
        html.Div(
            style={"width": 5, "height": 300, "backgroundColor": "hotpink"}
        ),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_table={
                'maxHeight': '300px',
                'overflowY': 'auto',
                'border': 'thin lightgrey solid'
            },
        )
        '''),

        rc.Markdown('''
        and here is `height` with the same content. Note how the table's
        container takes up all 300px.

        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_table={
                'height': '300px',
                'overflowY': 'auto',
                'border': 'thin lightgrey solid'
            },
        )
        '''),

    ]
)
