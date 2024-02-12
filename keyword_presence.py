import pandas as pd

# Load the CSV file
df = pd.read_csv('results.csv')

# Update the list of keywords with "magic"
keywords = [
    "Tramily", "family", "friend", "pet", "fest", "festival",
    "trail magic", "trail angel", "community", "event",
    "spouse", "gang", "conversation", "couple", "together", "call", "magic"
]

# Lowercase the keywords for case-insensitive matching
keywords = [keyword.lower() for keyword in keywords]

def check_keyword_presence(row, keywords):
    # Check if 'cleaned data' is not a string (e.g., NaN)
    if not isinstance(row['cleaned data'], str):
        return ''  # Return an empty string if 'cleaned data' is not a string
    
    # Tokenize the cleaned data for the row and lowercase
    tokens = row['cleaned data'].lower().split()
    # Create a set for unique tokens for efficient searching
    tokens_set = set(tokens)
    
    # Initialize a list to track the found keywords
    found_keywords = []
    
    # Special case handling for "trail magic" and "magic"
    if "trail magic" in tokens_set and "magic" in tokens_set:
        tokens_set.remove("trail magic")  # Remove "trail magic" if both present
    
    for keyword in keywords:
        # Check and add the keyword if it's in the tokens set
        if keyword in tokens_set:
            found_keywords.append(keyword)
    
    # Return the found keywords as a comma-separated string
    return ', '.join(found_keywords)

# Apply the function to each row in the DataFrame to create the new column
df['keyword presence'] = df.apply(check_keyword_presence, keywords=keywords, axis=1)

# Save the updated DataFrame to a new CSV file
df.to_csv('results_with_keywords.csv', index=False)
