import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

########### Define your variables ######

myheading1='Are you going to my college?'
tabtitle = '09-Admission'
list_of_options=['famous', 'not so famous', 'not famous at all', 'a nobody']
list_of_images=['outlier.png', 'correlation.png', 'gitcommit.jpg', 'scatterplot.png', 'good_code.png']
sourceurl = 'https://github.com/aaron-thompson-sage/09-logistic-regression---Heroku/blob/1632e6293d34cb0b80a07dcdc7bdbd708f23512d/docs/Admission-Prediction-Homework.ipynb'
githublink = 'https://github.com/aaron-thompson-sage/09-logistic-regression---Heroku'

def predict(gpa, gre, prestige):
    value = ((float(gre)*0.00321119) + (float(gpa)*0.7155019) - (float(prestige)*0.42287144) - 3.35801144)
    result = "unknown"
    if value < 0.5:
        result = f"Try a different college. ({value})"
    else:
        result = f"Welcome to college! ({value})"
    return result

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div(children=[dcc.Markdown('Enter GPA (0-4)')]),
    dcc.Input(id='my-id1', value='', type='text'),
    html.Div(children=[dcc.Markdown('Enter GRE (0-800)')]),
    dcc.Input(id='my-id2', value='', type='text'),
    html.Div(children=[dcc.Markdown('Enter Prestige (1-4)')]),
    dcc.Input(id='my-id3', value='', type='text'),
    html.Div(id='my-div'),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


########## Define Callback
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id1', component_property='value'),
    Input(component_id='my-id2', component_property='value'),
    Input(component_id='my-id3', component_property='value'),
    ]
)
def update_output_div(gpa, gre, prestige):
    return predict(gpa, gre, prestige)


############ Deploy
if __name__ == '__main__':
    app.run_server()
