import dash
from dash import dcc, html
import requests
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("💓 Real-Time Health Monitoring System", style={'textAlign': 'center'}),
    
    html.Div([
        html.H3("Heart Rate (BPM):", style={'display': 'inline-block'}),
        html.Div(id='heart-rate', style={'display': 'inline-block', 'fontSize': '24px'}),
    ], style={'textAlign': 'center'}),
    
    html.Div([
        html.H3("Body Temperature (°C):", style={'display': 'inline-block'}),
        html.Div(id='temperature', style={'display': 'inline-block', 'fontSize': '24px'}),
    ], style={'textAlign': 'center'}),

    html.Div([
        html.H3("SpO2 (%):", style={'display': 'inline-block'}),
        html.Div(id='spO2', style={'display': 'inline-block', 'fontSize': '24px'}),
    ], style={'textAlign': 'center'}),

    html.Div([
        html.H3("Health Risk:", style={'display': 'inline-block'}),
        html.Div(id='health-risk', style={'display': 'inline-block', 'fontSize': '24px'}),
    ], style={'textAlign': 'center'}),

    dcc.Graph(id='live-graph'),
    
    dcc.Interval(id='interval-component', interval=2000, n_intervals=0)
])

@app.callback(
    [Output('heart-rate', 'children'),
     Output('temperature', 'children'),
     Output('spO2', 'children'),
     Output('health-risk', 'children'),
     Output('live-graph', 'figure')],
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    try:
        vital_data = requests.get("http://127.0.0.1:5000/api/vital-signs").json()
        heart_rate = vital_data["heart_rate"]
        temperature = vital_data["temperature"]
        spO2 = vital_data["spO2"]
        risk = vital_data["risk"]
    except:
        heart_rate = 0
        temperature = 0
        spO2 = 0
        risk = "Unknown"
    
    # Update the gauge graph
    figure = {
        'data': [go.Indicator(
            mode="gauge+number",
            value=heart_rate,
            title={"text": "Heart Rate (BPM)"},
            gauge={'axis': {'range': [0, 150]}}
        )],
        'layout': go.Layout(margin=dict(t=50, b=0, l=0, r=0))
    }

    return heart_rate, temperature, spO2, risk, figure

if __name__ == '__main__':
    print("Starting Dash dashboard...")
    app.run_server(debug=True)
