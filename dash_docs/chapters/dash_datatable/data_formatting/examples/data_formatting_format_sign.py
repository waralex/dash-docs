import dash
from dash_table import DataTable
from dash_table.Format import Format, Scheme, Sign

app = dash.Dash(__name__)

columns = [
    dict(id='a', name='Default', type='numeric', format=Format()),
    dict(id='a', name='Negative', type='numeric', format=Format(sign=Sign.negative)),
    dict(id='a', name='Positive', type='numeric', format=Format(sign=Sign.positive)),
    dict(id='a', name='Parentheses', type='numeric', format=Format().sign(Sign.parantheses)),
    dict(id='a', name='Percentage/Parentheses', type='numeric', format=Format(scheme=Scheme.percentage, precision=2, sign=Sign.parantheses)),
    dict(id='a', name='Custom', type='numeric', format=dict(specifier='('))
]

values = [
    123.1, 123.12, 1234.123, 12345.12,
    -123.1, -123.12, -1234.123, -12345.12
]

app.layout = DataTable(columns=columns, data=[dict(a=value) for value in values])

if __name__ == '__main__':
    app.run_server(debug=True)
