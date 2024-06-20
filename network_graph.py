import json
from pyvis.network import Network

# Load the data from a JSON file
with open('hiker_connections_2018.json', 'r') as f:
    data = json.load(f)

# Create a Pyvis Network with remote resources for compatibility
net = Network(notebook=False, width='100%', height='800px', directed=True, cdn_resources='remote')

# Add all nodes first
for hiker in data.keys():
    net.add_node(hiker, label=hiker)

# Add edges with weights
for hiker, interactions in data.items():
    for other_hiker, weight in interactions.items():
        if hiker != other_hiker and weight > 0:  # Ignore self-interactions and zero weights
            net.add_edge(hiker, other_hiker, value=weight, title=str(weight))

# Generate the network and save it to an HTML file
net.write_html('hiker_network.html')
