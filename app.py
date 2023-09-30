# Import the necessary libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from about import about_page
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc

# Load the dataset
df = pd.read_csv('Intel_CPUs_cleaned.csv')

# Count the number of True values for each column
desktop_count = df['Desktop'].sum()
embedded_count = df['Embedded'].sum()
mobile_count = df['Mobile'].sum()

# Create a new DataFrame for the pie chart
data = pd.DataFrame({
    'Type': ['Desktop', 'Embedded', 'Mobile'],
    'Count': [desktop_count, embedded_count, mobile_count]
})

# Create a pie chart with a light gray grid
fig1 = px.pie(data, values='Count', names='Type', template='plotly_dark')
fig1.update_layout(
    title_text='Market Segmentation of Intel CPUs',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
)

# Create a bar chart of core counts with a light gray grid
fig2 = px.histogram(df, x='CoreCount', template='plotly_dark')
fig2.update_layout(
    title_text='Distribution of Core Counts in Intel CPUs',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
)

# Create a scatter plot of ClockSpeedMax vs Price with a light gray grid
fig3 = px.scatter(df, x='ClockSpeedMax', y='Price', template='plotly_dark')
fig3.update_layout(
    title_text='Maximum Clock Speed vs Price',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
)

# Create a scatter plot of CoreCount vs Price with a light gray grid
fig4 = px.scatter(df, x='CoreCount', y='Price', template='plotly_dark')
fig4.update_layout(
    title_text='Core Count vs Price',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
)

# Calculate the correlation matrix and create a heatmap using Plotly with a dark theme
correlation_data = df.iloc[:, 1:].corr()
fig5 = go.Figure(data=go.Heatmap(
    z=correlation_data,
    x=correlation_data.columns,
    y=correlation_data.columns,
    hoverongaps=False), layout=go.Layout(template='plotly_dark'))
fig5.update_layout(
    title_text='Correlation Matrix',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

# Create a heatmap of Price vs CoreCount and ThreadCount using Plotly with a dark theme
heatmap_data = df[['Price', 'CoreCount', 'ThreadCount']]
fig6 = go.Figure(data=go.Heatmap(
    z=heatmap_data.corr(),
    x=heatmap_data.columns,
    y=heatmap_data.columns,
    hoverongaps=False), layout=go.Layout(template='plotly_dark'))
fig6.update_layout(
    title_text='Heatmap of Price vs CoreCount and ThreadCount',
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)'
)

# Create a box plot to show the distribution of clock speed max for each lithography group using Plotly with a light gray grid
fig7 = px.box(df, x="Lithography", y="ClockSpeedMax", template='plotly_dark')
fig7.update_layout(
    title_text="Distribution of Clock Speed Max by Lithography",
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
)

# Create a regression plot to show the relationship between price and core count using Plotly with a light gray grid
fig8 = px.scatter(df, x="CoreCount", y="Price", trendline="ols", template='plotly_dark')
fig8.update_layout(
    title_text="Price vs Core Count Regression",
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    xaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='lightgray',
    ),
)

# Create a Dash application with the Bootstrap dark theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout for the page content
page_content = dbc.Container(
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
        dbc.Row(
            [
                dbc.Col(dbc.Card(dcc.Graph(figure=fig1), className="p-3 shadow-lg", style={"background-color": "#2e3858"}), md=6),
                dbc.Col(dbc.Card(dcc.Graph(figure=fig2), className="p-3 shadow-lg", style={"background-color": "#2e3858"}), md=6),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(dcc.Graph(figure=fig3), className="p-3 shadow-lg", style={"background-color": "#2e3858"}), md=6),
                dbc.Col(dbc.Card(dcc.Graph(figure=fig4), className="p-3 shadow-lg", style={"background-color": "#2e3858"}), md=6),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(dcc.Graph(figure=fig5), className="p-3 shadow-lg", style={"background-color": "#2e3858"}), md=6),
                dbc.Col(dbc.Card(dcc.Graph(figure=fig6), className="p-3 shadow-lg", style={"background-color": "#2e3858"}), md=6),
            ],
            className="mb-4",
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Card(dcc.Graph(figure=fig7), className="p-3 shadow-lg", style={"background-color": "#2e3858"}), md=6),
                dbc.Col(dbc.Card(dcc.Graph(figure=fig8), className="p-3 shadow-lg", style={"background-color": "#2e3858"}), md=6),
            ],
            className="mb-4",
        ),
    ],
    fluid=True,
    className="p-0"  # Set className to "p-0" to remove the padding on the left and right sides
)

# Callback to update page content based on URL pathname
@app.callback(Output('page-content', 'children'), Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/about':
        return about_page
    else:
        return page_content
    
# Define the main layout
app.layout = dbc.Container(
    [
        dcc.Location(id='url', refresh=False),  # Add this line to track the URL
        dbc.Row(
            [
                dbc.Col(id='page-content'),  # Update this line
            ],
        ),
    ],
    fluid=True,
    style={"background-color": "#1d2439", "font-family": "Futura, sans-serif"} # Set the background color and font family of the overall webpage
)

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)