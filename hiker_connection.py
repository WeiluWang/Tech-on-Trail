import pandas as pd
import json
from collections import defaultdict

# Load the JSON file containing hiker names
with open('hiker_trail_names.json', 'r') as json_file:
    hiker_data = json.load(json_file)

hiker_names = hiker_data["Hiker trail names"]

# Load the CSV file
df = pd.read_csv('test.csv')

# Create a dictionary to store the frequency count
hiker_connections = defaultdict(dict)

# Initialize the dictionary with zeros
for hiker in hiker_names:
    for other_hiker in hiker_names:
        hiker_connections[hiker][other_hiker] = 0

# Count the occurrences of each hiker name in the "Journal Story" column
for hiker in hiker_names:
    hiker_journal_entries = df[df['Hiker trail name'] == hiker]['Journal Story'].dropna()
    for entry in hiker_journal_entries:
        for other_hiker in hiker_names:
            hiker_connections[hiker][other_hiker] += entry.lower().count(other_hiker.lower())

# Save the results to a new JSON file
with open('hiker_connections.json', 'w') as json_file:
    json.dump(hiker_connections, json_file, indent=4)

print("Hiker connections JSON file created successfully!")
