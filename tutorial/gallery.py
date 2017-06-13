import dash_html_components as html
import dash_core_components as dcc

layout = html.Div([

    dcc.Markdown('''

    # Dash Gallery

    ## Getting Started Example

    The [Dash Getting Started Guide](/getting-started) contains
    many applications that range in complexity.

    The first interactive app that you'll create combines a `Slider`
    with a `Graph` and filters data using a Pandas `DataFrame`.
    The `animate` property in the `Graph` component was set to `True`
    so that the points transition smoothly.
    Some interactivity is built-in to the `Graph` component including
    hovering over values, clicking on legend items to toggle traces, and
    zooming into regions.

    [![Screenshot of simple Dash app](https://github.com/plotly/dash-docs/raw/master/images/gapminder-animation.gif)](/getting-started)

    [View the getting started guide](/getting-started)

    ## Goldman Sachs Remake: Portfolio Report

    This app recreates the look and feel of a Goldman Sachs report.
    It includes a Print to PDF button and the styles were optimized
    to look good on the web and in PDF form.

    The charts in the report on the web version are interactive.
    You can hover over points to see their values and zoom into
    regions. Since this report was built on top of Dash, you could
    adapt this report to include even more interactive elements, like
    a dropdown or a search box.

    With PDF styles, you can hide and show elements depending on whether
    the app is being viewed in the web browser or in print, using the
    same framework for the rich interactive applications as the static
    PDF reports.

    [![Screenshot of Goldman Sachs report](https://github.com/plotly/dash-docs/raw/master/images/goldman-sachs.png)](https://damp-stream-82875.herokuapp.com)

    [View the app](https://damp-stream-82875.herokuapp.com)

    ## Drug Discovery App

    This app displays a description of the drug as you hover over points in the
    graph.

    Selecting drugs in the dropdown highlights their position in the chart and
     appends their symbol in the table below.

     Built in a few hundred lines of Python code.

    ![Screenshot of drug discovery app](https://github.com/plotly/dash-docs/raw/master/images/drug-discovery-app.gif)

    ## NYTimes Remake: Recession in 255 Charts

    485 lines of Python code, including text copy.

    This Dash app was adapted from NYTimes's excellent
    [How the Recession Reshaped the Economy in 255 Charts](https://www.nytimes.com/interactive/2014/06/05/upshot/how-the-recession-reshaped-the-economy-in-255-charts.html).

    This Dash app is displays its content linearly, like an
    interactive report. The report highlights several notable
    views of the data and then invites the user to highlight
    their own regions at the end. This method of highlighting
    views is a great strategy for walking your readers through
    your complex analysis.

    The height of the charts was specified in viewport units (`vh`),
    scaling the size of the chart to the height of the screen. It
    looks great on monitors big and small.

    The text in the application is centered and its width is restricted
    to improve the reading experience. The graphs are full bleed:
    the extend past the narrow column of text the edges of page.

    [![Screenshot of NYTimes Dash app](https://github.com/plotly/dash-docs/raw/master/images/nytimes.png)](dash-showcase-report.herokuapp.com)

    [View the app](dash-showcase-report.herokuapp.com)


    '''.replace('    ', ''))



])
