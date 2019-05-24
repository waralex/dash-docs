import dash
from dash.dependencies import Input, Output
import dash_table
import pandas as pd


app = dash.Dash(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

PAGE_SIZE = 5

app.layout = dash_table.DataTable(
    id='table-sorting-filtering',
    columns=[
        {'name': i, 'id': i, 'deletable': True} for i in sorted(df.columns)
    ],
    pagination_settings={
        'current_page': 0,
        'page_size': PAGE_SIZE
    },
    pagination_mode='be',

    filtering='be',
    filter='',

    sorting='be',
    sorting_type='multi',
    sort_by=[]
)


@app.callback(
    Output('table-sorting-filtering', 'data'),
    [Input('table-sorting-filtering', 'pagination_settings'),
     Input('table-sorting-filtering', 'sort_by'),
     Input('table-sorting-filtering', 'filter')])
def update_table(pagination_settings, sort_by, filter):
    filtering_expressions = filter.split(' && ')
    dff = df
    for filter in filtering_expressions:
        if ' eq ' in filter:
            col_name = filter.split(' eq ')[0]
            filter_value = filter.split(' eq ')[1]
            dff = dff.loc[dff[col_name] == filter_value]
        if ' > ' in filter:
            col_name = filter.split(' > ')[0]
            filter_value = float(filter.split(' > ')[1])
            dff = dff.loc[dff[col_name] > filter_value]
        if ' < ' in filter:
            col_name = filter.split(' < ')[0]
            filter_value = float(filter.split(' < ')[1])
            dff = dff.loc[dff[col_name] < filter_value]

    if len(sort_by):
        dff = dff.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )

    return dff.iloc[
        pagination_settings['current_page']*pagination_settings['page_size']:
        (pagination_settings['current_page'] + 1)*pagination_settings['page_size']
    ].to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)
