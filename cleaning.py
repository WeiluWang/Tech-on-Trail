import pandas as pd
import nltk


from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Ensure you have the necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

def clean_text(text):
    if not isinstance(text, str):
        return ''  # Return an empty string or some default text if needed
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Apply stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
    
    # Apply lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in stemmed_tokens]
    
    # Join the tokens back into a string
    cleaned_text = ' '.join(lemmatized_tokens)
    
    return cleaned_text

# Load the CSV file
df = pd.read_csv('data.csv', dtype={'Journal Story': str}, encoding='Windows-1252')  # Try Windows-1252 encoding


# Clean the data
df['cleaned data'] = df['Journal Story'].apply(clean_text)

# Save the new DataFrame to a CSV file
df[['Journal Story', 'cleaned data']].to_csv('results.csv', index=False)
