import json

# Load the first JSON file
with open('hiker_trail_names_2003-12.json', 'r') as file1:
    data1 = json.load(file1)

# Load the second JSON file
with open('hiker_trail_names.json', 'r') as file2:
    data2 = json.load(file2)

# Concatenate the data
merged_data = {}
for key in data1:
    if key in data2:
        merged_data[key] = data1[key] + data2[key]
    else:
        merged_data[key] = data1[key]

for key in data2:
    if key not in merged_data:
        merged_data[key] = data2[key]

# Save the merged data to a new JSON file
with open('merged_hiker_trail_names.json', 'w') as merged_file:
    json.dump(merged_data, merged_file, indent=4)

print("JSON files have been successfully concatenated into 'merged_hiker_trail_names.json'")
