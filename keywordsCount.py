import csv
import pandas as pd
from collections import Counter

# Define the keywords
keywords = [
    "Tramily", "family", "friend", "pet", "fest", "festival",
    "trail magic", "trail angel", "community", "event",
    "spouse", "gang", "conversation", "couple", "together"
]

# Function to count keywords in the text
def count_keywords(text):
    # Create a counter for the keywords
    keyword_counter = Counter()
    
    # For each keyword, check if it's in the text and count the appearances
    for keyword in keywords:
        count = text.lower().count(keyword.lower())
        if count > 0:
            keyword_counter[keyword] = count
    return keyword_counter

# Read the CSV file
df = pd.read_csv('./journal.csv')

# Apply the function to the 'journal' column and create a new 'keyword' column
df['keyword'] = df['journal'].apply(lambda text: count_keywords(text))

# Convert the Counter objects in 'keyword' column to string
df['keyword'] = df['keyword'].apply(lambda x: '; '.join([f'{k}: {v}' for k, v in x.items()]))

# Save the modified DataFrame to a new CSV file
df.to_csv('journal_with_keywords.csv', index=False)
