import pandas as pd
import json
from collections import defaultdict
import re

# Load the JSON file containing hiker names
with open('hiker_trail_names.json', 'r') as json_file:
    hiker_data = json.load(json_file)

hiker_names = hiker_data["Hiker trail names"]

# Load the CSV file
df = pd.read_csv('2018_hiker_journal.csv')

# Create a dictionary to store the frequency count
hiker_connections = defaultdict(lambda: defaultdict(int))
print("start analyzing!")

# Count the occurrences of each hiker name in the "Journal Story" column
for hiker in hiker_names:
    hiker_journal_entries = df[df['Hiker trail name'] == hiker]['Journal Story'].dropna()
    for entry in hiker_journal_entries:
        for other_hiker in hiker_names:
            if hiker != other_hiker:  # Ignore self-references
                # Use regex to find whole word matches
                pattern = re.compile(r'\b' + re.escape(other_hiker) + r'\b')
                match_count = len(pattern.findall(entry))
                if match_count > 0:
                    hiker_connections[hiker][other_hiker] += match_count
                    hiker_connections[other_hiker][hiker] += match_count  # Count interaction bidirectionally

# Accumulate interactions and filter out zero interactions
accumulated_interactions = defaultdict(int)
for hiker, connections in hiker_connections.items():
    for other_hiker, count in connections.items():
        if hiker < other_hiker:  # To avoid double counting
            accumulated_interactions[(hiker, other_hiker)] += count

# Convert to a simpler dictionary structure
simplified_interactions = {
    f"{h1} <-> {h2}": count for (h1, h2), count in accumulated_interactions.items() if count > 0
}

# Save the results to a new JSON file
with open('accumulated_hiker_connections_2018.json', 'w') as json_file:
    json.dump(simplified_interactions, json_file, indent=4)

print("Accumulated hiker connections JSON file created successfully!")
