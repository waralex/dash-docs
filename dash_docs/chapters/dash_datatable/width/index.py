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

        Subscribe to [plotly/dash-table#737](https://github.com/plotly/dash-table/issues/737) for updates or other workarounds
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
        > In the example above, ellipsis are not displayed for the header.
        > We consider this a bug, subscribe to [plotly/dash-table#735](https://github.com/plotly/dash-table/issues/735) for updates.
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
            style_table={'overflowX': 'auto'},
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

        '''
        ),

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
            style_table={'overflowX': 'auto'},
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
            style_table={'overflowX': 'auto'},
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
                'overflowX': 'auto'
            }
        )
        '''),

    ]
)
