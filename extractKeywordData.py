import pandas as pd

# Load the cleaned data
df = pd.read_csv('results_with_custom_stopwords.csv')

# Grouped keywords
grouped_keywords = {
    "hostel_shelter": ["hostel", "shelter"],
    "angel_magic": ["angel", r'\bmagic\b']
}

# Other individual keywords
individual_keywords = ["fest", "amili", "town", "camp"]

# Function to filter and save data based on grouped keywords
def save_filtered_data_grouped(group_name, keywords):
    # Filter data containing any of the keywords in the 'cleaned data' column
    filtered_df = df[df['cleaned data'].str.contains('|'.join(keywords), case=False, na=False)]

    # Save the filtered data to a CSV file named after the group
    filtered_df.to_csv(f'{group_name}.csv', index=False)

# Function to filter and save data based on an individual keyword
def save_filtered_data_individual(keyword):
    # Filter data containing the keyword in the 'cleaned data' column
    filtered_df = df[df['cleaned data'].str.contains(keyword, case=False, na=False)]

    # Save the filtered data to a CSV file named after the keyword
    filtered_df.to_csv(f'{keyword}.csv', index=False)

# Iterate over the grouped keywords and save the corresponding data
for group_name, keywords in grouped_keywords.items():
    save_filtered_data_grouped(group_name, keywords)

# Iterate over the individual keywords and save the corresponding data
for keyword in individual_keywords:
    save_filtered_data_individual(keyword)
