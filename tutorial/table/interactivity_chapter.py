from textwrap import dedent

import dash_html_components as html
import dash_core_components as dcc

from tutorial import tools
from tutorial import styles


examples = {
    example: tools.load_example('tutorial/examples/table/{}'.format(example))
    for example in ['interactivity_connected_to_graph.py']
}

layout = html.Div(
    [

        dcc.Markdown(dedent("""
        # DataTable Interactivity

        `DataTable` includes several features for modifying and transforming
        the view of the data. These include:

        - Sorting by column (`sorting=True`)
        - Filtering by column (`filtering=True`)
        - Editing the cells (`editable=True`)
        - Deleting rows (`row_deletable=True`)
        - Deleting columns (`columns[i].deletable=True`)
        - Selecting rows (`row_selectable='single' | 'multi'`)
        - Paging front-end (`pagination_mode='fe'`)

        A quick note on filtering. We have defined our own
        syntax for performing filtering operations. Here are some
        examples for this particular dataset:

        - Enter `Asia` in the "continent" column
        - Enter `> 5000` in the "gdpPercap" column
        - Enter `< 80` in the `lifeExp` column

        > Note: simple strings can be entered plain, but if you have
        > spaces or special characters (including `-`, particularly in dates)
        > you need to wrap them in quotes.
        > Single quotes `'`, double quotes `"`, or backticks `\\`` all work.
        > [Full filter syntax reference](/datatable/filtering)
        """)),

        dcc.Markdown(dedent("""
        By default, these transformations are done clientside.
        Your Dash callbacks can respond to these modifications
        by listening to the `data` property as an `Input`.

        Note that if `data` is an `Input` then the entire
        `data` will be passed over the network: if your dataframe is large,
        then this will become slow. For large dataframes, you can perform the
        [sorting or filtering in Python instead](/datatable/callbacks).
        """)),

        dcc.SyntaxHighlighter(
            examples['interactivity_connected_to_graph.py'][0],
            language='python',
            customStyle=styles.code_container
        ),

        html.Div(
            examples['interactivity_connected_to_graph.py'][1],
            className='example-container'
        ),

    ]
)
