import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import pandas as pd

app=dash.Dash()
df=pd.read_csv(r'C:\Users\ninjaac\Desktop\P14-Machine-Learning-AZ-Template-Folder\Part 3 - Classification\Section 14 - Logistic Regression\Logistic_Regression\Social_Network_Ads.csv')
app.layout=html.Div(children=[
    html.H1('the graph based on the data slider'),
    dcc.Graph(id='op'),
    dcc.Slider(
        id='ip',
        min=df['Age'].min(),
        max=df['Age'].max(),
        value=df["Age"].min(),
        marks={str(Age): str(Age) for Age in df['Age'].unique()},
        step=None,
    )
])

@app.callback(Output('op','figure'),
              [Input('ip','value')])
def update_figure(selected_age):
    filter_df=df[df["Age"]==selected_age]
    graph=[]
    for i in filter_df['Gender'].unique():
        df_by_gender=filter_df[filter_df['Gender']==i]
        graph.append(dict(
            x=df_by_gender['Age'],
            y=df_by_gender["EstimatedSalary"],
            mode='markers',
            opacity=0.6,
            marker={
                'size':15,
                "line":{'width':0.5,'color':'white'},
            },
            name=i,
        ))

        return {
            'data':graph,
            'layout':dict(
                xaxis={'title':'Age of the person'},
                yaxis={'title':'estimated salary'},
                legend={'x':0,'y':2},
                hovermode='closest',
                transition={'duration':200}
            )

        }


if __name__=='__main__':
    app.run_server(debug=True)