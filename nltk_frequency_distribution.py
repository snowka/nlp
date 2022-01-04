# This script will provide graph of the word frequency in a text.
# https://realpython.com/nltk-nlp-python/#making-a-frequency-distribution

from nltk import FreqDist

frequency_distribution = FreqDist(insert name of text file here)
print(frequency_distribution)

meaningful_words = [
    word for word in text8 if word.casefold() not in stop_words
]
frequency_distribution = FreqDist(meaningful_words)
frequency_distribution.most_common(20)

frequency_distribution.plot(20, cumulative=True)