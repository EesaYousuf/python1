import numpy as np
import plotly.graph_objs as go
from dash import Dash, dcc, html, Input, Output
# Sample curve data
x = np.linspace(0, 10, 500)
y = np.sin(x) + 1  # Shifted sine wave so area is positive

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='curve', config={'scrollZoom': True}),
    html.Div("Area under curve in view:", style={"marginTop": "20px"}),
    html.Div(id='area-output')
])
@app.callback(
    Output('curve', 'figure'),
    Input('curve', 'relayoutData')
)
def update_figure(relayout_data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='y = sin(x)+1'))

    fig.update_layout(title="Zoom in/out to update area")
    return fig

@app.callback(
    Output('area-output', 'children'),
    Input('curve', 'relayoutData')
)
def update_area(relayout_data):
    if relayout_data and 'xaxis.range[0]' in relayout_data:
        x_min = float(relayout_data['xaxis.range[0]'])
        x_max = float(relayout_data['xaxis.range[1]'])
        mask = (x >= x_min) & (x <= x_max)
        area = np.trapz(y[mask], x[mask])
        return f"{area:.4f}"
    return "Zoom in to calculate area."

if __name__ == '__main__':
    app.run_server(debug=True)