import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer

app=dash.Dash()
app.layout=html.Div('dash first app')


if __name__=='__main__':
    app.run_server(debug=True)
