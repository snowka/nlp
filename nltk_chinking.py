# This script will chink a text.
# Chinking is used together with chunking, but while chunking is used to include a pattern,
# chinking is used to exclude a pattern.

# from https://realpython.com/nltk-nlp-python/

import nltk
from nltk.tokenize import word_tokenize
nltk.download("averaged_perceptron_tagger")
lotr_quote = "It's a dangerous business, Frodo, going out your door."
words_in_lotr_quote = word_tokenize(lotr_quote)

lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)
print(lotr_pos_tags)

grammar = """
Chunk: {<.*>+}
       }<JJ>{"""

chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(lotr_pos_tags)
tree.draw()
