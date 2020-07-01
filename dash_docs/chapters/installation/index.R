library(dash)
library(dashCoreComponents)
library(dashHtmlComponents)

layout <- htmlDiv(list(
htmlH1('Dash Installation'),
dccMarkdown("

In order to use Dash, you need to make sure that
the Dash R package is present in your local
development environment. As Dash is under active development,
upgrading your Dash version frequently is recommended
in order to ensure you can take advantage of the latest
features and performance improvements. Make sure you're on at least version `3.0.2` of R.
You can see what version of R you have by entering version in the R CLI.

Run the following command in your development environment to install the latest version of Dash:

"),

dccMarkdown("
```{r}
# installs dashHtmlComponents, dashCoreComponents, and dashTable
# and will update the component libraries when a new package is released
install.packages('dash')
```
"),
htmlBr(),
dccMarkdown("Ready? Now, let's [make your first Dash app](/getting-started).
"),

htmlHr(),

dccMarkdown("
> A quick note on checking your versions and on upgrading.
> These docs are run using the versions listed above and
> these versions should be the latest versions available.
> To check which version that you have installed, you can run e.g.
>
> ```{r}
> library(dashCoreComponents)
> packageVersion('dashCoreComponents')
> ```
>
>
> To see the latest changes of any package, check the GitHub repo's CHANGELOG.md file:
> - [dash changelog](https://github.com/plotly/dashR/blob/master/CHANGELOG.md)
> - [dash-core-components changelog](https://github.com/plotly/dash-core-components/blob/master/CHANGELOG.md)
> - [dash-html-components changelog](https://github.com/plotly/dash-html-components/blob/master/CHANGELOG.md)
> - [dash-table changelog](https://github.com/plotly/dash-table/blob/master/CHANGELOG.md)
>
> Finally, note that the plotly package and the dash-renderer package are
> important package dependencies that are installed automatically
> with dash-core-components and dash respectively.
> These docs are using dash-renderer==1.4.1 and plotly==4.9.2.
>
> All of these packages adhere to [semver](https://semver.org/).
"),
htmlHr(),
dccMarkdown("
[Back to the Table of Contents](/)
")

))
