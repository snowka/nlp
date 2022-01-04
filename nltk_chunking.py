# This script will chunk a text. While tokenizing
# allows you to identify words and sentences, chunking allows you to identify phrases.

# from https://realpython.com/nltk-nlp-python/

import nltk
from nltk.tokenize import word_tokenize
nltk.download("averaged_perceptron_tagger")
lotr_quote = "It's a dangerous business, Frodo, going out your door."
words_in_lotr_quote = word_tokenize(lotr_quote)

lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)
print(lotr_pos_tags)

# You’ve got a list of tuples of all the words in the quote, along with their POS tag. In order to chunk, you first need to define a chunk grammar.
# Note: A chunk grammar is a combination of rules on how sentences should be chunked. It often uses regular expressions, or regexes.
# For this tutorial, you don’t need to know how regular expressions work, but they will definitely come in handy for you in the future if you want to process text.
# Create a chunk grammar with one regular expression rule:

grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(lotr_pos_tags)
tree.draw()

# Chinking
# Chinking is used together with chunking, but while chunking is used to include a pattern,
# chinking is used to exclude a pattern.

grammar = """
Chunk: {<.*>+}
       }<JJ>{"""

chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(lotr_pos_tags)
