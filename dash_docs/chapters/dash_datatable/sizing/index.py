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

        html.H1('DataTable Width & Column Width'),

        html.H2('Default Width'),
        rc.Markdown(
        '''
        By default, the table will expand to the width of its container.
        The width of the columns is determined automatically in order to
        accommodate the content in the cells.
        '''
        ),
        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns]
        )
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

        html.Hr(),

        rc.Markdown(
        '''
        The default styles work well for a small number of columns and short
        text. However, if you are rendering a large number of columns or
        cells with long contents, then you'll need to employ one of the
        following overflow strategies to keep the table within its container.
        '''
        ),

        rc.Markdown(
        '''
        ## Wrapping onto Multiple Lines

        If your cells contain contain text with spaces, then you can overflow
        your content into multiple lines.
        '''
        ),
        Display(
        '''
        dash_table.DataTable(
            style_data={
                'whiteSpace': 'normal',
                'height': 'auto',
            },
            data=df_election.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_election.columns]
        )
        '''),

        rc.Markdown(
        '''
        ### Denser Multi-Line Cells with Line-Height

        If you are display lots of text in your cells, then you may want to
        make the text appear a little more dense by shortening up the line-height.
        By default (as above), it's around 22px. Here, it's 15px.
        '''
        ),
        Display(
        '''
        dash_table.DataTable(
            style_data={
                'whiteSpace': 'normal',
                'height': 'auto',
                'lineHeight': '15px'
            },
            data=df_election.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_election.columns]
        )
        '''),

        rc.Markdown(
        '''
        ### Wrapping onto Multiple Lines while Constraining the Height of Cells

        If your text is really long, then you can constrain the height of the
        cells and display a tooltip when hovering over the cell.

        This is a little tricky because, [by CSS 2.1 rules](https://www.w3.org/TR/CSS21/tables.html#height-layout),
        the height of a table cell is “the minimum height required by the content”.
        So, here we are setting the height of the cell indirectly
        by setting the div _within_ the cell.

        In this example, we display two lines of data by setting the `line-height`
        to be 15px and the height of each cell to be 30px.
        In this example, the second sentence is cut off.

        There are a few limitations with this method:

        1. Note that it is not possible to display ellipses with this method.
        2. It is not possible to set a max-height. All of the cells need to be
        the same height.

        Subscribe to plotly/dash-table#737 for updates or other workarounds
        on this issue.
        '''
        ),
        Display(
        """
        dash_table.DataTable(
            style_data={
                'whiteSpace': 'normal',
            },
            data=df_moby_dick.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_moby_dick.columns],
            css=[{
                'selector': '.dash-spreadsheet td div',
                'rule': '''
                    line-height: 15px;
                    max-height: 30px; min-height: 30px; height: 30px;
                    display: block;
                    overflow-y: hidden;
                '''
            }],
            tooltip_data=[
                {
                    column: {'value': str(value), 'type': 'markdown'}
                    for column, value in row.items()
                } for row in df_moby_dick.to_dict('rows')
            ],
            tooltip_duration=None
        )
        """),

        rc.Markdown(
        """
        ## Overflowing Into Ellipses

        Alternatively, you can keep the content on a single line but display
        a set of ellipses if the content is too long to fit into the cell.

        Here, `max-width` is set to 0. It could be any number, the only
        important thing is that it is supplied. The behaviour will be
        the same whether it is 0 or 50.

        If you want to just hide the content instead of displaying ellipses,
        then set `textOverflow` to `'clip'` instead of `'ellipsis'`.
        """
        ),
        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            style_cell={
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'maxWidth': 0
            },
        )
        '''),

        rc.Markdown(
        '''
        ### Ellipses & Tooltips

        If you are display text data that is cut off by ellipses, then you can
        include tooltips so that the full text appears on hover.

        By setting `tooltip_duration` to `None`, the tooltip won't disappear
        as long as you are hovered on it. You can override this by passing in
        a number in milliseconds (e.g. 2000 if you want it to disappear after
        two seconds).
        '''
        ),
        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            style_cell={
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
                'maxWidth': 0,
            },
            tooltip_data=[
                {
                    column: {'value': str(value), 'type': 'markdown'}
                    for column, value in row.items()
                } for row in df_election.to_dict('rows')
            ],
            tooltip_duration=None
        )
        '''),

        rc.Markdown(
        '''
        ## Horizontal Scroll

        Instead of trying to fit all of the content in the container, you could
        overflow the entire container into a scrollable container.
        '''
        ),

        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            style_table={'overflowX': 'scroll'},
        )
        '''),

        rc.Markdown(
        '''
        Note how we haven't explicitly set the width of the individual columns
        yet. The widths of the columns have been computed dynamically depending
        on the width of the table and the width of the cells contents.
        In the example above, by providing a scrollbar, we're effectively
        giving the table as much width as needs in order to fit the entire
        width of the cell contents on a single line.

        ### Horizontal Scroll with Max-Width & Wrapping

        We can combine some of these strategies by bounding the `maxWidth` of
        a column and overflowing into multiple lines (or ellipses) if the
        content exceeds that width while rendering the table within a
        scrollable horizontal container. If the column's contents don't
        exceed the `maxWidth`, then the column will only take up the
        necessary amount of horizontal space.
        '''
        ),

        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            style_table={'overflowX': 'scroll'},
            style_cell={
                'height': 'auto',
                'minWidth': '0px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            }
        )
        '''),

        rc.Markdown('### Horizontal Scroll with Max-Width & Ellipses'),

        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            style_table={'overflowX': 'scroll'},
            style_cell={
                'minWidth': '0px', 'maxWidth': '180px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            }
        )
        '''),

        rc.Markdown('### Horizontal Scroll with Fixed-Width Columns & Cell Wrapping'),

        rc.Markdown(
        '''
        Alternatively, you can fix the width of each column by adding `width`.
        In this case, the column's width will be constant, even if its contents
        are shorter or wider.
        '''
        ),

        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            style_table={'overflowX': 'scroll'},
            style_cell={
                'height': 'auto',
                # all three widths are needed
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'whiteSpace': 'normal'
            }
        )
        '''),

        rc.Markdown('### Horizontal Scroll with Fixed-Width & Ellipses'),

        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            style_table={'overflowX': 'scroll'},
            style_cell={
                # all three widths are needed
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            }
        )
        '''),

        rc.Markdown(
        '''
        ### Horizontal Scrolling via Fixed Columns

        You can also add a horizontal scrollbar to your table by fixing
        the leftmost columns with `fixed_columns`.
        '''
        ),

        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            fixed_columns={'headers': True, 'data': 1},
            style_table={'minWidth': '100%'}
        )
        '''),

        rc.Markdown(
        '''
        Here is the same example but with *fixed-width cells & ellipses*.
        '''
        ),

        Display(
        '''
        dash_table.DataTable(
            data=df_election.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df_election.columns],
            fixed_columns={ 'headers': True, 'data': 1 },
            style_table={'minWidth': '100%'},
            style_cell={
                # all three widths are needed
                'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
                'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            }
        )
        '''),


        rc.Markdown("## Individual Column Widths"),

        rc.Markdown(
        '''
        ### Percentage Based Widths

        The widths of individual columns can be supplied through the
        `style_cell_conditional` property. These widths can be specified as
        percentages or fixed pixels. You can supply the widths for _all_ of the
        columns or just a few of them.
        '''
        ),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_cell_conditional=[
                {'if': {'column_id': 'Date'},
                 'width': '30%'},
                {'if': {'column_id': 'Region'},
                 'width': '30%'},
            ]
        )
        '''),

        rc.Markdown(
        '''
        ### Individual Column Widths with Pixels

        In this example, we set three columns to have fixed-widths. The remaining
        two columns will be take up the remaining space.
        '''),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_cell_conditional=[
                {'if': {'column_id': 'Temperature'},
                 'width': '130px'},
                {'if': {'column_id': 'Humidity'},
                 'width': '130px'},
                {'if': {'column_id': 'Pressure'},
                 'width': '130px'},
            ]
        )
        '''),

        rc.Markdown(
        '''
        ### Overriding a single column's width

        You can set the width of all of the columns with `style_data` and
        override a single column with `style_cell_conditional`.
        '''
        ),

        Display(
        '''
        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'id': c, 'name': c} for c in df.columns],
            style_data={
                'width': '100px',
                'maxWidth': '100px',
                'minWidth': '100px',
            },
            style_cell_conditional=[
                {
                    'if': {'column_id': 'Region'},
                    'width': '250px'
                },
            ],
            style_table={
                'overflowX': 'scroll'
            }
        )
        '''),

        rc.Markdown(
        '''
        # DataTable Height

        By default, the table's height will expand in order
        to render up to 250 rows.
        After 250 rows, the table with display a **pagination** UI
        that allows you to navigate through 250 rows at a time.

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

        **Limitations**

        If you have more than 1000 rows, then the browser will slow
        down when trying to render the table. With more than 1000 rows, we
        recommend switching to browser or server pagination (as above) or
        virtualization (as below).
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
                'overflowY': 'auto'
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
