import csv
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt

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
# Function to print total counts of each keyword
def print_total_keyword_counts(df):
    total_keyword_counts = Counter()
    
    # Process each row's 'keyword' data
    for keyword_data in df['keyword']:
        # Split the keyword data by '; ', then split each pair by ': ' and convert count to int
        keyword_counts = keyword_data.split('; ')
        for keyword_count in keyword_counts:
            if keyword_count:  # Check if not an empty string
                keyword, count = keyword_count.split(': ')
                total_keyword_counts[keyword] += int(count)
    
    plot_keyword_frequencies_with_proportions(total_keyword_counts)
    # Print the total counts for each keyword
    for keyword, count in total_keyword_counts.items():
        print(f"{keyword}: {count}")
def plot_keyword_frequencies_with_proportions(total_keyword_counts):
    # Prepare data for the bar chart
    keywords = list(total_keyword_counts.keys())
    counts = list(total_keyword_counts.values())

    # Create the bar chart
    plt.figure(figsize=(12, 8))
    bars = plt.bar(keywords, counts, color='skyblue')

    # Adding titles and labels
    plt.title('Frequency of Keywords in Journal Entries with Proportions')
    plt.xlabel('Keywords')
    plt.ylabel('Counts')
    plt.xticks(rotation=45, ha='right')

    # Calculate total for proportions
    total = sum(counts)

    # Annotate proportions above bars
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height, f'{count / total:.2%}', ha='center', va='bottom')

    # Show the plot
    plt.tight_layout()
    plt.show()
# Read the CSV file
# Read the CSV file with a different encoding
try:
    df = pd.read_csv('./TJ_data_GROUP.csv', encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv('./TJ_data_GROUP.csv', encoding='latin-1')  # or 'ISO-8859-1' or 'cp1252'

# Ensure that 'journal' contains only string data
df = df[df['Journal Story'].apply(lambda x: isinstance(x, str))]

# Apply the function to the 'journal' column and create a new 'keyword' column
df['keyword'] = df['Journal Story'].apply(lambda text: count_keywords(text))

# Convert the Counter objects in 'keyword' column to string
df['keyword'] = df['keyword'].apply(lambda x: '; '.join([f'{k}: {v}' for k, v in x.items()]))

# Save the modified DataFrame to a new CSV file
df.to_csv('temp_journal_with_keywords.csv', index=False)

# Call the function to print out the total counts of each keyword
print_total_keyword_counts(df)
