# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

from dash_docs import styles
from dash_docs import tools
from dash_docs.tutorial.utils.convert_props_to_list import rc.ComponentReference
from dash_docs.tutorial.utils.component_block import ComponentBlock
from dash_docs.tutorial.components import Syntax, Example
from dash_docs import reusable_components as rc

examples = {
    'confirm': tools.load_example('tutorial/examples/core_components/confirm.py'),
    'confirm-provider': tools.load_example('tutorial/examples/core_components/confirm_provider.py'),
    'date_picker_single': tools.load_example('tutorial/examples/core_components/date_picker_single.py'),
    'date_picker_range': tools.load_example('tutorial/examples/core_components/date_picker_range.py'),
    'dropdown': tools.load_example('tutorial/examples/core_components/dropdown.py'),
    'dropdown-dynamic-options': tools.load_example('tutorial/examples/core_components/dropdown_dynamic_options.py'),
    'graph-config': tools.load_example('tutorial/examples/core_components/export_graph_to_chart_studio.py'),
    'input-all-types': tools.load_example('tutorial/examples/core_components/input_all_types.py'),
    'input-basic': tools.load_example('tutorial/examples/core_components/input-basic.py'),
    'input-number-type': tools.load_example('tutorial/examples/core_components/input_number_type.py'),
    'rangeslider': tools.load_example('tutorial/examples/core_components/rangeslider.py'),
    'rangeslider-nonlinear': tools.load_example('tutorial/examples/core_components/rangeslider_nonlinear.py'),
    'slider': tools.load_example('tutorial/examples/core_components/slider.py'),
    'slider-updatemode': tools.load_example('tutorial/examples/core_components/slider_updatemode.py'),
    'store-clicks': tools.load_example('tutorial/examples/core_components/store_clicks.py'),
    'store-share': tools.load_example('tutorial/examples/core_components/store_share.py'),
    'tabs_callback':  tools.load_example('tutorial/examples/core_components/tabs_callback_graph.py'),
    'tabs_simple':  tools.load_example('tutorial/examples/core_components/tabs_simple.py'),
    'tabs_styled_with_classes':  tools.load_example('tutorial/examples/core_components/tabs_styled_with_classes.py'),
    'tabs_styled_with_classes_css':  tools.read_file('assets/tabs-styled-with-classes.css'),
    'tabs_styled_with_inline':  tools.load_example('tutorial/examples/core_components/tabs_styled_with_inline.py'),
    'tabs_styled_with_props':  tools.load_example('tutorial/examples/core_components/tabs_styled_with_props.py'),
    'upload-datafile':  tools.load_example('tutorial/examples/core_components/upload-datafile.py'),
    'upload-gallery':  tools.load_example('tutorial/examples/core_components/upload-gallery.py'),
    'upload-image':  tools.load_example('tutorial/examples/core_components/upload-image.py'),
    'button_basic': tools.load_example('tutorial/examples/core_components/button_basic.py'),
    'button_n_clicks_timestamp': tools.load_example('tutorial/examples/core_components/button_n_clicks_timestamp.py'),
    'logout_button': tools.load_example('tutorial/examples/core_components/logout_button.py'),
    'loading_component': tools.load_example('tutorial/examples/core_components/loading_component.py')
}

# RangeSlider

# Checklist

# Input

# Button


# Markdown

# DatePickerRange

# DatePickerSingle

# Link

# Textarea

# Tabs

# Graphs

# Upload

# ConfirmDialog

# ConfirmDialogProvider


# Loading component

# Location
