# This script will help find collocations in a text, that is, pairs of words that come up within a text.
# from https://realpython.com/nltk-nlp-python/#making-a-frequency-distribution

# In the example below, insert the name of your text or text file for "text8".
lemmatized_words = [lemmatizer.lemmatize(word) for word in text8]
new_text = nltk.Text(lemmatized_words)
new_text.collocations()




