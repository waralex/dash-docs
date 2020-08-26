using Dash
using DashHtmlComponents
using DashCoreComponents

app =
    dash(external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"])


app.layout = html_div() do
    dcc_markdown("""
    ## Dash Installation

    In order to use Dash, you need to have a version of Julia >= 1.2.

    To install the most recent version of Dash, run the following command:

    ```julia
        using Pkg;
        Pkg.add(PackageSpec(url="https://github.com/plotly/Dash.jl.git"))
    ```

    To install the latest stable development version of Dash, run the following commands:

    ```julia
        using Pkg;
        Pkg.add(PackageSpec(url="https://github.com/plotly/Dash.jl.git", rev="dev"))
        Pkg.add(PackageSpec(url="https://github.com/plotly/dash-html-components.git", rev="jl"))
        Pkg.add(PackageSpec(url="https://github.com/plotly/dash-core-components.git", rev="jl"))
        Pkg.add(PackageSpec(url="https://github.com/plotly/dash-table.git", rev="jl"))
    ```


    Once you have installed Dash, you are ready to [make your first Dash app](/getting-started).

    A quick note on checking your versions and on upgrading.
    These docs are run using the versions listed above and these versions should
    be the latest versions available.
    To check which version that you have installed, you can run:

    ```julia

    Pkg.status("Dash")
    Pkg.status("DashHtmlComponents")
    Pkg.status("DashCoreComponents")
    ```

    To see the latest changes of any package, check the CHANGELOG.MD file in
    the appropriate GitHub repo.

    * [Dash changelog](https://github.com/plotly/Dash.jl/blob/dev/CHANGELOG.md)
    * [DashCoreComponents changelog](https://github.com/plotly/dash-core-components/blob/master/CHANGELOG.md)
    * [DashHTMLComponents changelog](https://github.com/plotly/dash-html-components/blob/master/CHANGELOG.md)
    * [DashTable changelog](https://github.com/plotly/dash-table/blob/master/CHANGELOG.md)
    """)

end

run_server(app, "0.0.0.0", 8000)
