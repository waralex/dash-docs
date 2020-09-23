using Dash
using DashHtmlComponents
using DashCoreComponents

app =  dash()


app.layout = html_div() do
    html_h1("Interactive Visualizations"),
    html_blockquote(dcc_markdown("This is the 6th and final chapter of the [Dash Tutorial](/).
    The [previous chapter](/sharing-data-between-callbacks) covered basic callback usage and the [next chapter](/state)
    describes how to share data between callbacks. The [rest of the Dash documentation](/) covers other
    topics like multi-page apps and component libraries.
    Just getting started? Make sure to [install the necessary
    dependencies](/installation)")),
    dcc_markdown("
    ### Frequently Asked Questions

    Q: How can I customize the appearance of my Dash app?
    A: Dash apps are rendered in the browser as modern standards-compliiant web apps. This means
    you can use CSS to style your Dash app as you would standard HTML.

    All `DashHtmlComponents` support inline CSS styling through a `style` attribute. An external
    CSS stylesheet can also be used to style `DashHtmlComponents` and `DashCoreComponents` by
    targeting the IDs or classnames of your components. Both `DashHtmlComponents` and `DashCoreComponents`
    accept the attribute `className`, which corresponds to the HTML element attribute `class`.


    "),


end

run_server(app, "0.0.0.0", 8000)
