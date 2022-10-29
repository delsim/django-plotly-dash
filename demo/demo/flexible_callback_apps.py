'''
Demonstration apps using flexible callbacks

Copyright (c) 2022 Gibbs Consulting and others - see CONTRIBUTIONS.md

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''


from dash import dcc, html
from dash.dependencies import Input, Output

from django_plotly_dash import DjangoDash


app = DjangoDash('FlexibleCallbackExample')


app.layout = html.Div([
    dcc.RadioItems(id="a-dropdown",
                   options=[{'label': 'Left', 'value': 'left'},
                            {'label': 'Centre', 'value': 'middle'},
                            {'label': 'Right', 'value': 'right'},
                            ],
                   value='middle'),
    dcc.RadioItems(id="e-dropdown",
                   options=[{'label': 'Left', 'value': 'left'},
                            {'label': 'Centre', 'value': 'middle'},
                            {'label': 'Right', 'value': 'right'},
                            ],
                   value='right'),
    html.Div(id="b-div"),
    html.Div(id="c-div"),
    html.Div(id="d-div"),
    html.Div(id="f-div"),
    html.Div(id="g-div"),
])


@app.callback(inputs=dict(a=Input('a-dropdown', 'value')),
              output=[Output('b-div', 'children')],
              )
def app_calc_b(a, **kwargs):
    return [f"[b:{a}]"]


@app.callback(inputs=dict(a=Input('e-dropdown', 'value')),
              output=Output('c-div', 'children'),
              )
def app_calc_c(a, **kwargs):
    return f"[c:{a}]"


@app.callback(inputs=dict(a=Input('a-dropdown', 'value'),
                          c=Input('c-div', 'children'),
                          b=Input('b-div', 'children'),
                          ),
              output=Output('d-div', 'children'),
              )
def app_calc_d(b, c, a, **kwargs):
    return f"d should have b as ->{b}<- and a as ->{a}<- and c as ->{c}<-"


@app.callback(inputs=dict(a=Input('a-dropdown', 'value'),
                          c=Input('c-div', 'children'),
                          b=Input('b-div', 'children'),
                          ),
              output=Output('f-div', 'children'),
              )
def app_calc_f(a, b, c, **kwargs):
    return f"f should have b as ->{b}<- and a as ->{a}<- and c as ->{c}<-"


@app.callback(inputs=dict(a=Input('a-dropdown', 'value'),
                          b=Input('b-div', 'children'),
                          c=Input('c-div', 'children'),
                          ),
              output=Output('g-div', 'children'),
              )
def app_calc_f(a, b, c, **kwargs):
    return f"g should have b as ->{b}<- and a as ->{a}<- and c as ->{c}<-"


expapp = DjangoDash('FlexibleCallbackExampleExpanded')


expapp.layout = html.Div([
    dcc.RadioItems(id="a-dropdown",
                   options=[{'label': 'Left', 'value': 'left'},
                            {'label': 'Centre', 'value': 'middle'},
                            {'label': 'Right', 'value': 'right'},
                            ],
                   value='middle'),
    dcc.RadioItems(id="e-dropdown",
                   options=[{'label': 'Left', 'value': 'left'},
                            {'label': 'Centre', 'value': 'middle'},
                            {'label': 'Right', 'value': 'right'},
                            ],
                   value='right'),
    html.Div(id="b-div"),
    html.Div(id="c-div"),
    html.Div(id="d-div"),
    html.Div(id="e-div"),
    html.Div(id="g-div"),
])


@expapp.callback(inputs=dict(a=Input('a-dropdown', 'value')),
                 output=[Output('b-div', 'children')],
                 )
def app_calc_b(a, **kwargs):
    return [f"[b:{a}]"]


@expapp.callback(inputs=dict(a=Input('e-dropdown', 'value')),
                 output=Output('c-div', 'children'),
                 )
def app_calc_c(a, **kwargs):
    return f"[c:{a}]"


@expapp.callback(inputs=dict(a=Input('a-dropdown', 'value'),
                             c=Input('c-div', 'children'),
                             b=Input('b-div', 'children'),
                             ),
                 output=Output('d-div', 'children'),
                 )
def app_calc_d(b, c, a, **kwargs):
    return f"d should have b as ->{b}<- and a as ->{a}<- and c as ->{c}<-"


@expapp.callback(inputs=dict(a=Input('a-dropdown', 'value'),
                             c=Input('c-div', 'children'),
                             b=Input('b-div', 'children'),
                             ),
                 output=Output('e-div', 'children'),
                 )
def app_calc_f(a, b, c, **kwargs):
    return f"e should have b as ->{b}<- and a as ->{a}<- and c as ->{c}<-"


#@expapp.callback(inputs=dict(a=Input('a-dropdown', 'value'),
#                             b=Input('b-div', 'children'),
#                             c=Input('c-div', 'children'),
#                             ),
#                 output=Output('g-div', 'children'),
#                 )
#def app_calc_f(a, b, c, **kwargs):
#    return f"g should have b as ->{b}<- and a as ->{a}<- and c as ->{c}<-"


@expapp.callback(inputs=[Input('a-dropdown', 'value'),
                         Input('b-div', 'children'),
                         Input('c-div', 'children'),
                         ],
                 output=Output('g-div', 'children'),
                 )
def app_calc_f(a, b, c, **kwargs):
    return f"g should have b as ->{b}<- and a as ->{a}<- and c as ->{c}<-"
