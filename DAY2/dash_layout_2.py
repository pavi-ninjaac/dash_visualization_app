import dash
import dash_core_components as dcc
import dash_html_components as html


external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']
app=dash.Dash()
colors={
    'backgroud':"black",
    'text':'blue',
}
app.layout=html.Div(style={'backgroundColor':colors['backgroud']},
                    children=[
                        html.H1(children='hello dash', style={ 'textAlign' : 'center', 'color': colors['text']}),
                        html.Div(children='web application frame work', style={'color':colors['text']}),
                        dcc.Graph(
                            id='example_2',
                            figure={
                                'data':[
                                    {'x' : [1,2,3,4,5], 'y' : [2,3,5,6,7], 'type':'bar', 'name': 'barchart'},
                                    {'x' : [4,5,6,7,8],  'y' :[1,2,3,4,5], 'type': 'bar', 'name' :'line'},
                                ],
                                'layout':{
                                    'plot_bgcolor':colors['backgroud'],
                                    'paper_bgcolor':colors['backgroud'],
                                    'font' :{
                                        'color':colors['text']
                                    }
                                }
                            }
                        )
                    ]


)




if __name__=='__main__':
    app.run_server(debug=True)