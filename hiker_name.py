import pandas as pd
import json

# Load the CSV file
df = pd.read_csv('TJ_emotion_data_2003_2012_04_22_2024.csv')

# Extract the unique names from the "Hiker trail name" column
unique_names = df['Hiker trail name'].dropna().unique().tolist()

# Create a dictionary to store the names
data = {"Hiker trail names": unique_names}

# Write the unique names to a JSON file
with open('hiker_trail_names_2003-12.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("JSON file created successfully!")
