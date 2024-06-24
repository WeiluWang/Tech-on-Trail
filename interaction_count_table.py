import json
import pandas as pd

# Load the JSON file containing hiker names
with open('hiker_trail_names.json', 'r') as json_file:
    hiker_data = json.load(json_file)

hiker_names = set(hiker_data["Hiker trail names"])

# Load the filtered hiker connections JSON file
with open('filtered_hiker_connections_2018.json', 'r') as json_file:
    filtered_hiker_connections = json.load(json_file)

# Count hikers with and without interactions
hikers_with_interactions = set()
for hiker, connections in filtered_hiker_connections.items():
    for other_hiker in connections.keys():
        hikers_with_interactions.add(hiker)
        hikers_with_interactions.add(other_hiker)

num_hikers_with_interactions = len(hikers_with_interactions)
num_hikers_without_interactions = len(hiker_names - hikers_with_interactions)

print(f"Number of hikers with interactions: {num_hikers_with_interactions}")
print(f"Number of hikers without interactions: {num_hikers_without_interactions}")

# Generate the interaction table
interaction_data = []
for hiker, connections in filtered_hiker_connections.items():
    for other_hiker, count in connections.items():
        interaction_data.append([hiker, other_hiker, count])

interaction_df = pd.DataFrame(interaction_data, columns=['Hiker1', 'Hiker2', 'Interaction_Count'])
interaction_df.to_csv('hiker_connection_table.csv', index=False)

print("Hiker connection table CSV file created successfully!")
