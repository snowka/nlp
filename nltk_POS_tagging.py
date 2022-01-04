# This script tags the parts of speech in a text.
# from https://realpython.com/nltk-nlp-python/

# To download and view the complete list of part of speech tags:
# import nltk
# nltk.download('tagsets')
# nltk.help.upenn_tagset()

import nltk
from nltk.tokenize import word_tokenize

sagan_quote = """
If you wish to make an apple pie from scratch,
you must first invent the universe."""

words_in_sagan_quote = word_tokenize(sagan_quote)
print(nltk.pos_tag(words_in_sagan_quote))




