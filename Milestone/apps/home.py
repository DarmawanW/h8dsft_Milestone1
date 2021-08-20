import dash_html_components as html
import dash_bootstrap_components as dbc
 
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Welcome to the Supermarket Sales dashboard",
                className="text-center"),
                className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children=['Hello, My name is Darmawan Wijaya!', html.Br(),
                'I am a participant of the Hacktiv8 Data Science Bootcamp - Batch 002.', html.Br(), 
                'This is my Hacktiv8 Milestone Project dashboard!']),
                className="mb-4")
        ]),
 
        dbc.Row([
            dbc.Col(
                html.H5(children=['It consists of three main pages: ', html.Br(),
                '1. Visualization, which gives an data visualization of the supermarket sales, ', html.Br(),
                '2. Hypothesis Testing, which gives you a hypothesis testing between variables', html.Br(),
                '3. Home, you get the original dataset and visit my Github page from here,']),
                className="mb-5")
        ]),
 
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Get the original dataset here',
                        className="text-center"),
                        dbc.Button("Supermarket Sales",
                        href="https://www.kaggle.com/aungpyaeap/supermarket-sales",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
 
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Visit my Github Page',
                        className="text-center"),
                        dbc.Button("GitHub",
                        href="https://github.com/DarmawanW",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
        ], className="mb-5"),
    ])
 
])