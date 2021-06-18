from dash.dependencies import Input, Output
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.metrics import accuracy_score, mean_squared_error
import numpy as np

app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

df = px.data.iris()

fig = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns),
                #fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[df.sepal_length, df.sepal_width, df.petal_length, df.petal_width, df.species, df.species_id],
               #fill_color='lavender',
               align='left'))
])

app.title = "Iris Dataset"

# All our figures

fig1 = px.scatter(df, x="sepal_width", y="sepal_length", color="species", size='petal_length', hover_data=['petal_width'], trendline="ols", marginal_y="box", marginal_x="histogram")

fig1.update_layout(
    autosize=True,
    height=700)

fig2 = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')

fig2.update_layout(
    autosize=True,
    height=700
)

fig3 = px.violin(df, y="sepal_width", color="species_id", box=True, points="all", hover_data=df.columns)

fig3.update_layout(
    autosize=True,
    height=700
)

fig4 = px.parallel_coordinates(df, color="species_id",
                    color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)

fig4.update_layout(
    autosize=True,
    height=700
)

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})


# Add a title
app.layout = html.Div([  
    html.H1(
      children='Iris Dataset',
      style={
         'textAlign': 'center'
      }
    ),
    
    dcc.Markdown(children= '''
        The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus"
    '''
    ),
    
    html.Br(),
    
    # First tab here
        # TODO children=[
            html.H3('Dataset'),
            dcc.Graph(figure=fig),
            
            html.H3('Scatterplot'),
            dcc.Graph(figure=fig1),
            
            # Two columns charts
            html.Div([
                html.Div([
                    html.H3('3D-plot'),
                    dcc.Graph(id='g1', figure=fig2)
                ], className="six columns"),

                html.Div([
                    html.H3('Violin-plot'),
                    dcc.Graph(id='g2', figure=fig3)
                ], className="six columns"),
            ], className="row"),
            
            html.H3('Parallel Coordinates'),
            dcc.Graph(figure=fig4)
        
        # Second tab here
        # TODO children=[
            
            html.Br(),
            
            # Two columns charts
            html.Div([
                
                # Left content
                html.Div([
                    
                    dcc.Markdown(children= '''
                    In this section, we automatically fit a Support Vector Machine using the columns and the parameters specified in the left column. The results are displayed in the right column.
                '''
                    ),
             
                    html.Br(),
                    
                    html.H3('Feature columns'),

                    dcc.Dropdown(
                        # TODO: Dropdown here
                    ),
                   
                   html.Br(),
                   html.H3('Test size'),
                    
                   dcc.Slider(
                        # TODO: Slider here
                    ),

                 ], className="six columns"),
                
                 # Right content
                html.Div(children=[
                    html.H3('SVM Model training'),
                ], className="six columns", id='output-container-button'),
            ], className="row"),
                    
    
], style={'width': '75%', 'textAlign': 'center', 'margin-left':'12.5%', 'margin-right':'0'})


@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('demo-dropdown1', 'value'), dash.dependencies.Input('test-size', 'value')])
def train_model(value2, value3):

    if len(value2) < 1:
        return "Please select at least 1 column"
    else:
        X_train, X_test, y_train, y_test = train_test_split(df[value2], df['species'], test_size=value3)

        clf = SVC(gamma='auto', probability=True)
        clf.fit(X_train, y_train)
        pred = clf.predict(X_test)
        acc = np.round(accuracy_score(pred, y_test),3)

        fig5 = px.scatter_3d(x=clf.predict_proba(X_test)[:,0], y=clf.predict_proba(X_test)[:,1], z=clf.predict_proba(X_test)[:,2], color=clf.predict(X_test))

        return html.Div([
            html.Br(),
            html.H6('Model accuracy %s'%str(acc)),
            html.Br(), 
            dcc.Graph(id='g5', figure=fig5)
        ])


if __name__ == '__main__':
    app.run_server(debug=True)