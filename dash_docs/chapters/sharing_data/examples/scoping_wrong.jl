using CSV
using DataFrames
using Dash
using DashHtmlComponents
using DashCoreComponents
using JSON3

df = DataFrame(a = [1, 2, 3],
               b = [4, 1, 4],
               c = ["x", "y", "z"])

app = dash()

app.layout = html_div() do
    dcc_dropdown(id="dropdown",
                 options = [
                    (label = i, value = i) for i in df["c"]
                 ],
                 value="x"
    ),
    html_div(id="output")
end

callback!(
    app,
    Output("output", "children"),
    Input("dropdown", "value"),
) do value
    # Here, `df` is an example of a variable that is
    # 'outside the scope of this function'.
    # It is not safe to modify or reassign this variable
    # inside this callback.
    # do not do this, this is not safe!
    global df = filter!(row -> row.c == value, df)
    return length(df[1, :])
end

run_server(app, "0.0.0.0", 8000)
