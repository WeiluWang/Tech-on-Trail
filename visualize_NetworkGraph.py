import json
import networkx as nx
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Load JSON data
file_path = 'accumulated_hiker_connections_2018.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Create a graph
G = nx.Graph()

# Add edges to the graph
for key, count in data.items():
    hiker1, hiker2 = key.split(' <-> ')
    G.add_edge(hiker1.strip(), hiker2.strip(), weight=count)

# Define node positions using a layout with a larger value of 'k' for more space
pos = nx.spring_layout(G, dim=3, k=1.5, iterations=100)  # Increase 'k' for more spread out nodes

# Extract node and edge positions
edge_trace = []
for edge in G.edges(data=True):
    x0, y0, z0 = pos[edge[0]]
    x1, y1, z1 = pos[edge[1]]
    edge_trace.append(go.Scatter3d(
        x=[x0, x1, None], y=[y0, y1, None], z=[z0, z1, None],
        mode='lines',
        line=dict(color='lightblue', width=edge[2]['weight'] / 10),
        hoverinfo='none'
    ))

node_trace = go.Scatter3d(
    x=[], y=[], z=[], mode='markers+text',
    textposition='top center',
    marker=dict(
        size=6,
        color='red'
    ),
    text=[]
)

# Prepare hover text for each edge
edge_hover_text = []
for edge in G.edges(data=True):
    hiker1, hiker2, attr = edge
    edge_hover_text.append(f"{hiker1} <-> {hiker2}<br>Count: {attr['weight']}")

# Add node and edge positions to traces
for node in G.nodes():
    x, y, z = pos[node]
    node_trace['x'] += (x,)
    node_trace['y'] += (y,)
    node_trace['z'] += (z,)
    node_trace['text'] += (node,)

fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])

for i, trace in enumerate(edge_trace):
    trace.hovertext = edge_hover_text[i]
    trace.hoverinfo = 'text'
    fig.add_trace(trace)

fig.add_trace(node_trace)

fig.update_layout(
    title='Hiker Interaction Network',
    showlegend=False,
    scene=dict(
        xaxis=dict(showbackground=False),
        yaxis=dict(showbackground=False),
        zaxis=dict(showbackground=False)
    )
)

fig.show()
