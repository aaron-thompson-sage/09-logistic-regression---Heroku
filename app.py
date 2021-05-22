import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State

########### Define your variables ######

myheading1='Are you going to my college?'
tabtitle = 'xkcd'
list_of_options=['famous', 'not so famous', 'not famous at all', 'a nobody']
sourceurl = 'https://xkcd.com/'
githublink = 'https://github.com/austinlasseter/dash-callbacks-radio'


########## Set up the chart

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    dcc.Input(id='gpa', placeholder='What is your gpa?', type='text'),
    html.Br(),
    dcc.Input(id='gre', placeholder='What is your gre?', type='text'),
    html.Br(),
    dcc.RadioItems(
        id='prestige',
        options=[
                {'label':list_of_options[0], 'value':1},
                {'label':list_of_options[1], 'value':2},
                {'label':list_of_options[2], 'value':3},
                {'label':list_of_options[3], 'value':4},
                ],
        value=4,
        ),
    html.Div(id='admit', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


########## Define Callback
@app.callback(Output('admit', 'children'),
              [Input('gpa', 'gre', 'value')])
def radio_results(image_you_chose):
    return html.Img(src=app.get_asset_url(image_you_chose), style={'width': 'auto', 'height': '50%'}),


############ Deploy
if __name__ == '__main__':
    app.run_server()
