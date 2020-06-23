import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer

app=dash.Dash()
app.layout=html.Div(children=[
    html.H1('bar and line chart'),
    dcc.Graph(
        id='bar_chart',
        figure={
            'data':[ {'x': [1,2,3,4,5,6,7,8], 'y' : [3,6,7,7,4,5,6,8], 'type' : 'line', 'name': 'boats'},
                     {'x': [1,2,3,4,5,6,7,8], 'y' : [1,4,5,2,3,5,7,8], 'type' : 'bar', 'name': 'car'},
                    ],
            'layout':{
                'title':'bar chart'
        }

     }
)
])



if __name__=='__main__':
    app.run_server(debug=True)

