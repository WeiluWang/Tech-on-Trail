import pandas as pd
from collections import Counter
import re

# Function to check if a token is an English word and not a symbol
def is_english_word(word):
    return re.fullmatch(r'[A-Za-z]+', word) is not None

# Load the results.csv file
df = pd.read_csv('results.csv')

# Concatenate all cleaned data into a single string
all_cleaned_data = ' '.join(df['cleaned data'].dropna())

# Tokenize the string into words
words = all_cleaned_data.split()

# Filter out non-English words and symbols
filtered_words = [word for word in words if is_english_word(word)]

# Count the frequency of each word
word_freq = Counter(filtered_words)

# Get the top 50 most common words
top_50_words = word_freq.most_common(500)

# Convert to DataFrame
top_50_df = pd.DataFrame(top_50_words, columns=['Word', 'Count'])

# Save to a new CSV file
top_50_df.to_csv('frequency.csv', index=False)
