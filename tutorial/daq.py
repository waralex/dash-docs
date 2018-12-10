import dash_core_components as dcc
import dash_html_components as html

from tutorial import styles
from textwrap import dedent as s

from tutorial.utils.component_block import ComponentBlock


def gen_code_container(componentName, propString='', description=''):

    if(len(propString) > 0):
        propString = '\n  ' + propString + '\n'
        
    return [

        html.Hr(), 

        html.H3(dcc.Link(componentName,
                         href='/dash-daq/{}'.format(componentName.lower()))),
        
        dcc.Markdown(s(description)),
        
        ComponentBlock('''import dash_daq as daq

daq.{}({})'''.format(componentName, propString.replace(',', ',\n ')),
                                language='python',
                                customStyle=styles.code_container),

        html.Br(), 
        
        dcc.Link('More {} Examples and Reference'.format(componentName),
                 href='/dash-daq/{}'.format(componentName.lower()))
    ]


layoutChildren = [

    dcc.Markdown(''' 
    # Dash DAQ 

    Dash is a web application framework that provides pure Python abstraction 
    around HTML, CSS, and JavaScript.

    Dash DAQ comprises a robust set of controls that make it simpler to 
    integrate data acquisition and controls into your Dash applications. 

    The source is on GitHub at [plotly/dash-daq](https://github.com/plotly/dash-daq). 

    These docs are using version {}.
    '''.replace('    ', '').format(dcc.__version__))
]


dash_daq_components = {
    'BooleanSwitch': {
        'description': '''A switch component that toggles between on \
        and off.''',
        'propString': '''on=True, id=\'hello\'''',
    },
    'ColorPicker': {
        'description': '''A color picker.'''
    },
    'Gauge': {
        'description': '''A gauge component that points to some value between \
        some range.''',
        'propString': '''min=0, max=10, value=6''',
    },
    'GraduatedBar': {
        'description': '''A graduated bar component that displays a value within \
        some range as a percentage.''',
        'propString': 'min=0, max=10, value=3''',
    },
    'Indicator': {
        'description': '''A boolean indicator LED.''', 
        'propString': 'value=True'
    },
    'Knob': {
        'description': '''A knob component that can be turned to a value \
        between some range.''',
        'propString': 'min=0, max=10, value=8'
    },
    'LEDDisplay': {
        'description': '''A 7-segment LED display component.''',
        'propString': 'value=\"3.14159\"'
    },
    'NumericInput': {
        'description': '''A numeric input component that can be set to \
        a value between some range.''',
        'propString': 'min=0, max=10, value=5'
    },
    'PowerButton': {
        'description': '''A power button component that can be turned \
        on or off.''',
        'propString': 'on=True'
    },
    'PrecisionInput': {
        'description': '''A numeric input component that converts an \
        input value to the desired precision.''',
        'propString': 'precision=4, value=299792458'
    },
    'StopButton': {
        'description': '''A stop button.''',
    },
    'Slider': {
        'description': '''A slider component with support for a \
        target value.''',
        'propString': 'value=17, min=0, max=100, \
        targets={\"25\": {\"label\": \"TARGET\"}}'
    },
    'Tank': {
        'description': '''A tank component that fills to a value \
        between some range.''',
        'propString': 'min=0, max=10, value=5'
    },
    'Thermometer': {
        'description': '''A thermometer component that fills to \
        a value between some range.''',
        'propString': 'min=95, max=105, value=98.6'
    },
    'ToggleSwitch': {
        'description': '''A switch component that toggles between \
        two values.''',
    }
}


for k in dash_daq_components.keys():
    layoutChildren += gen_code_container(k, **dash_daq_components[k])

layout = html.Div(className='gallery', children=layoutChildren)

