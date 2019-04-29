import dash
from dash.dependencies import Input, Output
import dash_table
import pandas as pd


app = dash.Dash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')


app.layout = dash_table.DataTable(
    id='table-filtering-be',
    columns=[
        {"name": i, "id": i} for i in sorted(df.columns)
    ],

    filtering='be',
    filter=''
)


@app.callback(
    Output('table-filtering-be', "data"),
    [Input('table-filtering-be', "filter")])
def update_graph(filter):
    print(filter)
    filtering_expressions = filter.split(' && ')
    dff = df
    for filter_part in filtering_expressions:
        if ' eq ' in filter_part:
            col_name = filter_part.split(' eq ')[0]
            filter_value = filter_part.split(' eq ')[1]
            dff = dff.loc[dff[col_name] == filter_value]
        if ' > ' in filter_part:
            col_name = filter_part.split(' > ')[0]
            filter_value = float(filter_part.split(' > ')[1])
            dff = dff.loc[dff[col_name] > filter_value]
        if ' < ' in filter_part:
            col_name = filter_part.split(' < ')[0]
            filter_value = float(filter_part.split(' < ')[1])
            dff = dff.loc[dff[col_name] < filter_value]

    return dff.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)
