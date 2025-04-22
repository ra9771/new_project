import dash
from dash import dcc, html
import requests
import plotly.graph_objs as go
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Real-Time Heart Rate Monitor"),
    dcc.Graph(id='live-graph'),
    dcc.Interval(id='interval-component', interval=2000, n_intervals=0)
])

@app.callback(Output('live-graph', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_graph(n):
    try:
        hr_data = requests.get("http://127.0.0.1:5000/api/heart-rate").json()
        heart_rate = hr_data["heart_rate"]
    except:
        heart_rate = 0  # fallback

    return {
        'data': [go.Indicator(
            mode="gauge+number",
            value=heart_rate,
            title={"text": "Heart Rate (BPM)"},
            gauge={
                "axis": {"range": [0, 180]},
                "bar": {"color": "red"},
                "steps": [
                    {"range": [60, 100], "color": "lightgreen"},
                    {"range": [100, 140], "color": "yellow"},
                    {"range": [140, 180], "color": "orange"}
                ]
            }
        )]
    }

if __name__ == '__main__':
    app.run_server(debug=True)
