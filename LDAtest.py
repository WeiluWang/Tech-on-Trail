import pandas as pd
import gensim
from gensim import corpora
from gensim.models.coherencemodel import CoherenceModel
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('amili.csv')  # Replace 'hostel_shelter.csv' with your file path

# Function to convert preprocessed text to list
def convert_to_list(text):
    return text.split()

# Convert the preprocessed 'cleaned data' column to lists
df['cleaned data'] = df['cleaned data'].apply(convert_to_list)

# Prepare the dictionary and corpus for LDA
dictionary = corpora.Dictionary(df['cleaned data'])
doc_term_matrix = [dictionary.doc2bow(doc) for doc in df['cleaned data']]

# Create the LDA model
lda_model = gensim.models.ldamodel.LdaModel(corpus=doc_term_matrix,
                                            id2word=dictionary,
                                            num_topics=8,
                                            random_state=100,
                                            update_every=1,
                                            chunksize=100,
                                            passes=20,
                                            alpha='auto',
                                            per_word_topics=True)

# Visualize the topics
topics = lda_model.print_topics(num_words=10)
for topic in topics:
    print(topic)

# Save the model
lda_model.save('lda_model_results.model')
