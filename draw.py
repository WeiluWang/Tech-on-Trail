import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Load the CSV file
df = pd.read_csv('results_with_keywords.csv')

# Parse the "keyword presence" column to list all keywords
all_keywords = []
for item in df['keyword presence'].dropna():
    # Assuming keywords are stored as a string of comma-separated values
    keywords_list = item.split(', ')
    all_keywords.extend(keywords_list)

# Count occurrences of each keyword
keyword_counts = Counter(all_keywords)

# Remove empty string entry if exists
keyword_counts.pop('', None)

# Calculate total number of entries that contain at least one keyword
total_keyword_entries = sum(keyword_counts.values())

# Prepare data for plotting
keywords = list(keyword_counts.keys())
counts = list(keyword_counts.values())
proportions = [count / total_keyword_entries for count in counts]
proportion_texts = [f'{p:.2%}' for p in proportions]

# Plotting
plt.figure(figsize=(len(keywords) * 1.5, 8))  # Dynamic width based on number of keywords
bars = plt.bar(keywords, counts, color='lightblue')

# Annotate proportions on the bars
for bar, proportion_text in zip(bars, proportion_texts):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height, proportion_text, ha='center', va='bottom')

plt.xticks(rotation=90)  # Rotate labels to prevent overlap
plt.xlabel('Keywords')
plt.ylabel('Count')
plt.title('Count and Proportion of Each Keyword Presence')
plt.tight_layout()  # Adjust layout to make room for the rotated x-axis labels
plt.show()
