from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel('Vendas.xlsx')

fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df['ID Loja'].unique())
opcoes.append('Todas as lojas')

app.layout = html.Div(children=[
    html.H1(children='Dash board in python'),
    html.H2(children='Faturamento baseado em um banco de dados imaginarios'),

    html.Div(children='''
        Quantidade de produtos vendidos por loja
    '''),

    dcc.Dropdown(opcoes, value='Todas as lojas', id='lista_lojas'),

    dcc.Graph(
        id='grafico_quantidade_vendas',
        figure=fig
    )
])


@app.callback(
    Output('grafico_quantidade_vendas', 'figure'),
    Input('lista_lojas', 'value')
)
def update_output(value):
    if value == 'Todas as lojas':
        fig = px.bar(df, x="Produto", y="Quantidade",
                     color="ID Loja", barmode="group")

    else:
        tabela_filtada = df.loc[df['ID Loja'] == value, :]
        fig = px.bar(tabela_filtada, x="Produto", y="Quantidade",
                     color="ID Loja", barmode="group")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
