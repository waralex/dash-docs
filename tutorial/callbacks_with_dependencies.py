# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import State, Event, Input, Output
from server import app
import time

# Section 4 - Callbacks With Dependencies
layout_list = [
    html.H2('Callback Resolution'),

    html.Div('''A core feature in Dash is callback dependency resolution.'''),
    html.Div('''Consider the following scenario:
    `Component C` depends on `Component B` and `Componet B` depends on `Component A`.
    '''),
    html.Div('''
    When `Component A` updates, `Component B`'s callback will get called and
    `Component B` will get updated. Once the update finishes, Dash will
    trigger `Component C`'s callback automatically with B's new value.
    The user triggered the first update (by changing Component A) and dash
    triggered the remaining updates, updating all of the components that depend
    on Component A directly or indirectly.'''),

    html.Div('''
        A common real-world example are forms.
        Often, the options of one dropdown depend on the value of another
        dropdown.
        A third component might depend on the values of both components.

        When the first dropdown changes,
        the second dropdown is triggered to change but the third component
        shouldn't update until both dropdowns have finished updating.
        If Dash updated the third component without waiting for the
        second dropdown to update, then its callback could get called with
        inconsistent state.
    '''),

    html.Strong('Example'),

    html.Div('''
        In this example, each dropdown's options and values depend on the
        previous dropdown. We've inserted a 2 second delay in each of the
        callbacks to illustrate the order in which components get updated.
    '''),

    html.Div('''
        Note how the text component depends on the values of all of the
        dropdowns but doesn't get updated until all three dropdowns have
        finished updating.
    ''')
]

dropdown_example = dcc.SyntaxHighlighter("""import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

all_options = {
    'NYC': {
        'Places': [
            'Statue of Liberty', 'Wall Street'
        ],
        'Boroughs': [
            'Brooklyn', 'The Bronx', 'Manhattan', 'Queens', 'Staten Island'
        ]
    },
    u'Montréal': {
        'Places': [
            'Olympic Stadium', 'Parc la Fontaine'
        ],
        'Neighborhoods': [
            'Le Plateau', 'Hochelaga', 'Outremont'
        ]
    }
}
app.layout = html.Div([
    # Initial dropdown with initial state
    dcc.Dropdown(
        id='cities',
        options=[{'label': k, 'value': k} for k in all_options.keys()],
        value='NYC'
    ),

    # Note how options and values aren't supplied for the
    # remaining two dropdowns.
    # When the dash app starts, it will traverse the callback dependency tree
    # and call all of the appropriate callbacks to fill out the app's state
    dcc.Dropdown(id='category'),
    dcc.Dropdown(id='sub-category'),

    # We'll display the values of the dropdowns in this component
    html.Div(id='display')
])

# Update the category dropdown's 'options'
# when the input dropdown's 'value' changes
@app.callback(Output('category', 'options'),
              [Input('cities', 'value')])
def update_category_options(selected_city):
    time.sleep(2)
    filtered_options = all_options[selected_city].keys()
    return [{'label': k, 'value': k} for k in filtered_options]


# Update the category dropdown's 'value'
# when its 'options' get changed
@app.callback(Output('category', 'value'),
              [Input('category', 'options')])
def update_category_value(new_options):
    return new_options[0]['value']


# Update the sub-category dropdown's 'options'
# when the cities dropdown's 'value' changes or
# when the categories dropdown's value changes
@app.callback(Output('sub-category', 'options'), [
    Input('cities', 'value'),
    Input('category', 'value')])
def update_sub_category_options(selected_city, selected_category):
    time.sleep(2)
    filtered_options = all_options[selected_city][selected_category]
    return [{'label': k, 'value': k} for k in filtered_options]

# Update the sub-category dropdown's 'value'
# when its options change
@app.callback(
    Output('sub-category', 'value'),
    [Input('sub-category', 'options')])
def update_sub_category_value(new_options):
    return new_options[0]['value']

# Display the selected value when all of the
# dropdown's values have finished updating.
@app.callback(
    Output('display', 'content'),
    [Input(id, 'value') for id in ['cities', 'category', 'sub-category']])
def update_display(selected_city, selected_category, selected_sub_category):
    time.sleep(2)
    return u"You've selected {}, {}, and {}".format(
        selected_city,
        selected_category,
        selected_sub_category
    )
""", language='python', customStyle={'borderLeft': 'thin solid lightgrey'})


all_options = {
    'NYC': {
        'Places': [
            'Statue of Liberty', 'Wall Street'
        ],
        'Boroughs': [
            'Brooklyn', 'The Bronx', 'Manhattan', 'Queens', 'Staten Island'
        ]
    },
    u'Montréal': {
        'Places': [
            'Olympic Stadium', 'Parc la Fontaine'
        ],
        'Neighborhoods': [
            'Le Plateau', 'Hochelaga', 'Outremont'
        ]
    }
}

layout_list.extend([
    html.Div([
        dcc.Dropdown(
            id='cities',
            options=[{'label': k, 'value': k} for k in all_options.keys()],
            value='NYC'
        ),
        dcc.Dropdown(id='category'),
        dcc.Dropdown(id='sub-category'),
        html.Div(id='display')
    ], style={'border': 'thin lightgrey solid', 'padding': '15px'}),

    dropdown_example
])
layout = html.Div(layout_list)


@app.callback(Output('category', 'options'), [Input('cities', 'value')])
def update_category_options(selected_city):
    time.sleep(2)
    filtered_options = all_options[selected_city].keys()
    return [{'label': k, 'value': k} for k in filtered_options]


@app.callback(Output('category', 'value'), [Input('category', 'options')])
def update_category_value(new_options):
    return new_options[0]['value']


@app.callback(Output('sub-category', 'options'), [
    Input('cities', 'value'),
    Input('category', 'value')])
def update_sub_category_options(selected_city, selected_category):
    time.sleep(2)
    filtered_options = all_options[selected_city][selected_category]
    return [{'label': k, 'value': k} for k in filtered_options]


@app.callback(
    Output('sub-category', 'value'),
    [Input('sub-category', 'options')])
def update_sub_category_value(new_options):
    return new_options[0]['value']


@app.callback(
    Output('display', 'content'),
    [Input(id, 'value') for id in ['cities', 'category', 'sub-category']])
def update_display(selected_city, selected_category, selected_sub_category):
    time.sleep(2)
    return u"You've selected {}, {}, and {}".format(
        selected_city,
        selected_category,
        selected_sub_category
    )
