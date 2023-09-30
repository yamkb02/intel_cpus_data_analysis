import dash_bootstrap_components as dbc
from dash import html

# Define the About page layout
about_page = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(html.H1("Intel CPUs", className="display-5 text-center mb-2", style={"font-family": "Futura, sans-serif", "font-size": "1.5rem"}), md=6),
                dbc.Col(
                    dbc.Container(
                        [
                            dbc.Button("Home", href="/", color="primary", className="mr-1", style={"background-color": "#1d2439", "border-color": "#1d2439", "font-size": "1.5rem", "color": "white", "font-family": "Futura, sans-serif"}),
                            dbc.Button("About", href="/about", color="primary", className="mr-1", style={"background-color": "#1d2439", "border-color": "#1d2439", "font-size": "1.5rem", "color": "white", "font-family": "Futura, sans-serif"}),
                        ],
                        className="d-flex justify-content-center align-items-center",
                    ),
                    md=6,
                ),
            ],
            className="mb-4 align-items-center mt-4",
        ),
        html.H1("About", className="display-4 text-center mb-4"),
        html.P("This is a sample about page. You can edit this texasdast to provide more information about the dashboard."),
    ],
    fluid=True,
    className="p-0"  # Set className to "p-0" to remove the padding on the left and right sides
)