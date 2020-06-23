import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_renderer

app=dash.Dash()

markdown='''
### title with markdown
Dah app will the best way of visualization wih interactive things [tutorial](http://bsjbf/gsio/gdfj.com)
you csn also watch the documentation of that in [documentation]('http://dash.ord/)
'''
app.layout=html.Div(children=[
    html.H1('markdoen test example'),
    dcc.Markdown(markdown)
])


if __name__=='__main__':
    app.run_server(debug=True)