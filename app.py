import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

########### Define your variables ######

myheading1='Are you going to my college?'
tabtitle = 'xkcd'
list_of_options=['famous', 'not so famous', 'not famous at all', 'a nobody']
list_of_images=['outlier.png', 'correlation.png', 'gitcommit.jpg', 'scatterplot.png', 'good_code.png']
sourceurl = 'https://xkcd.com/'
githublink = 'https://github.com/austinlasseter/dash-callbacks-radio'

def predict(gpa, gre, prestige):
    return ((gre*0.00321119) + (gpa*0.7155019) - (prestige*0.42287144) - 3.35801144)

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
    value = gpa #predict(gpa, gre, prestige)
    if (value < 0.5):
        return f"Try a different college. ({value})"
    else :
        return f"Welcome to college! ({value})"


############ Deploy
if __name__ == '__main__':
    app.run_server()
