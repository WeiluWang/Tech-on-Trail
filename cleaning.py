import pandas as pd
import nltk
from langdetect import detect, DetectorFactory
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string

# Ensure reproducibility in langdetect
DetectorFactory.seed = 0

# Ensure you have the necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False

def clean_text_with_custom_stopwords(text, additional_stop_words):
    if not isinstance(text, str):
        return ''
    
    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove punctuation
    tokens = [word for word in tokens if word.isalpha()]
    
    # Extend the stopwords list with additional words
    stop_words = set(stopwords.words('english')).union(additional_stop_words)
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Apply stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]
    
    # Apply lemmatization
    #lemmatizer = WordNetLemmatizer()
    #lemmatized_tokens = [lemmatizer.lemmatize(word) for word in stemmed_tokens]
    
    # Join the tokens back into a string
    cleaned_text = ' '.join(stemmed_tokens)
    
    return cleaned_text

# Additional stop words specified by you
additional_stop_words = {"trail", "climb", "year", "get", "could", "would", "can", "will", "today", "day"}

# Load the CSV file
df = pd.read_csv('data.csv', dtype={'Journal Story': str}, encoding='Windows-1252') 

# Assuming you have the CSV file loaded in df
df['cleaned data'] = df['Journal Story'].apply(lambda x: clean_text_with_custom_stopwords(x, additional_stop_words))

# Save the new DataFrame to a CSV file
df[['Journal Story', 'cleaned data']].to_csv('results_with_custom_stopwords.csv', index=False)



