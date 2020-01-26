import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

np.random.seed(42)
x_data = np.random.randint(1,101,100)
y_data = np.random.randint(1,101,100)



app.layout = html.Div(children=[
    html.H1('Hello Dash'),
    dcc.Graph(id='scatterplot',
              figure={
                  'data':[
                      go.Scatter(x=x_data,y=y_data,mode='markers',
                                 marker = {
                                     'size':14,
                                     'color':'rgb(123,321,231)',
                                     'symbol':'octagon',
                                     'line': {'width':2}
                                 })
                  ],
                  'layout':go.Layout(title='First Scatterplot',
                                     xaxis={'title': 'First X Axis'})
              })

])

if __name__ == '__main__':
    app.run_server()