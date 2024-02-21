import pandas as pd

# Load the cleaned data
df = pd.read_csv('results.csv')

# List of keywords
keywords = ["fest", "magic", "amili", "town", "angel", "shelter", "hostel", "camp"]

# Function to filter and save data based on a keyword
def save_filtered_data(keyword):
    # Filter data containing the keyword in the 'cleaned data' column
    filtered_df = df[df['cleaned data'].str.contains(keyword, case=False, na=False)]

    # Save the filtered data to a CSV file named after the keyword
    filtered_df.to_csv(f'{keyword}.csv', index=False)

# Iterate over the keywords and save the corresponding data
for keyword in keywords:
    save_filtered_data(keyword)
