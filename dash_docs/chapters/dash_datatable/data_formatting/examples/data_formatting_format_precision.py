import dash
from dash_html_components import Br, Div
from dash_table import DataTable
from dash_table.Format import Format, Scheme, Trim

app = dash.Dash(__name__)

columns_1 = [
    dict(id='a', name='No precision', type='numeric', format=Format()),
    dict(id='a', name='Default', type='numeric', format=Format(precision=2)),
    dict(id='a', name='Fixed', type='numeric', format=Format(precision=2, scheme=Scheme.fixed)),
    dict(id='a', name='Decimal', type='numeric', format=Format(precision=2, scheme=Scheme.decimal)),
    dict(id='a', name='Integer', type='numeric', format=Format(precision=2, scheme=Scheme.decimal_integer)),
    dict(id='a', name='Decimal/Exponent', type='numeric', format=Format(precision=2, scheme=Scheme.decimal_or_exponent)),
    dict(id='a', name='Decimal SI', type='numeric', format=Format(precision=2, scheme=Scheme.decimal_si_prefix)),
    dict(id='a', name='Exponent', type='numeric', format=Format(precision=2, scheme=Scheme.exponent)),
]

columns_2 = [
    dict(id='a', name='Percentage', type='numeric', format=Format(precision=2, scheme=Scheme.percentage)),
    dict(id='a', name='Rounded Percentage', type='numeric', format=Format(precision=2, scheme=Scheme.percentage_rounded)),
    dict(id='a', name='Binary', type='numeric', format=Format(precision=2, scheme=Scheme.binary)),
    dict(id='a', name='Octal', type='numeric', format=Format(precision=2, scheme=Scheme.octal)),
    dict(id='a', name='hex', type='numeric', format=Format(precision=2, scheme=Scheme.lower_case_hex)),
    dict(id='a', name='HEX', type='numeric', format=Format(precision=2, scheme=Scheme.upper_case_hex)),
    dict(id='a', name='Unicode', type='numeric', format=Format(precision=2, scheme=Scheme.unicode))
]

columns_3 = [
    dict(id='a', name='4 decimals', type='numeric', format=Format(precision=4, scheme=Scheme.fixed)),
    dict(id='a', name='4 decimals / trimmed', type='numeric', format=Format(precision=4, scheme=Scheme.fixed, trim=Trim.yes)),
    dict(id='a', name='Custom 4 decimals / trimmed', type='numeric', format=dict(specifier='.4~f')),
]

values = [123.1, 123.12, 1234.123, 12345.12]
data = [dict(a=value) for value in values]

app.layout = Div([
    DataTable(columns=columns_1, data=data),
    Br(),
    DataTable(columns=columns_2, data=data),
    Br(),
    DataTable(columns=columns_3, data=data)
])

if __name__ == '__main__':
    app.run_server(debug=True)
