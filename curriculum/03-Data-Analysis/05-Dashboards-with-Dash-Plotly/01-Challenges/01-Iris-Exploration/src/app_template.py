from dash.dependencies import Input, Output
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

df = # TODO

fig = # The dataset as a plotly object

app.title = # TODO

# All our figures

fig1 = 

fig2 = 

fig3 = 

fig4 = 

app.layout = html.Div([  
    html.H1(
      children='Iris Dataset',
      style={
         'textAlign': 'center'
      }
    ),
    
    dcc.Markdown(children= # Description
    ),
    
    html.Br(),
    
    # Dataset 
    # TODO 

    # Scatterplot 
    # TODO

    # Two columns charts
    html.Div([
        html.Div([
            # 3D-plot 
            # TODO
        ], className="six columns"),

        html.Div([
            # Violin-plot 
            # TODO
        ], className="six columns"),
    ], className="row"),

    # Parallel coordinates
    # TODO

]) # TODO Center and reduce width

if __name__ == '__main__':
    app.run_server(debug=True)