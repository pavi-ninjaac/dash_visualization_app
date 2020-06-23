import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer
import pandas as pd

df=pd.read_csv(r'C:\Users\ninjaac\Desktop\P14-Machine-Learning-AZ-Template-Folder\Part 3 - Classification\Section 14 - Logistic Regression\Logistic_Regression\Social_Network_Ads.csv')
def generate_table(df):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
          html.Tr([ html.Td(df.iloc[i][col]) for col in df.columns])  for i in range(10)
        ])
    ])

app=dash.Dash()

app.layout=html.Div(children=[
    html.H1('table example'),
    generate_table(df),

])

if __name__=='__main__':
    app.run_server(debug=True)