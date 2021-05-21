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
    dcc.Input(id='gre', placeholder='What is your gre?', type='text'),
    dcc.RadioItems(
        id='prestige',
        options=[
                {'Are you famous':list_of_options[0], 'value':list_of_images[0]},
                {'Are you not so famous':list_of_options[1], 'value':list_of_images[1]},
                {'Are you not famous at all':list_of_options[2], 'value':list_of_images[2]},
                {'Are you a nobody':list_of_options[3], 'value':list_of_images[3]},
                ],
        value=list_of_images[4],
        ),
    html.Div(id='admit', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


########## Define Callback
@app.callback(Output('your_output_here', 'children'),
              [Input('your_input_here', 'value')])
def radio_results(image_you_chose):
    return html.Img(src=app.get_asset_url(image_you_chose), style={'width': 'auto', 'height': '50%'}),


############ Deploy
if __name__ == '__main__':
    app.run_server()
