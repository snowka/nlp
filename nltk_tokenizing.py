# These functions from the NLK package will allow you to tokenize text by sentence or by word
# Taken from https://realpython.com/nltk-nlp-python/

from nltk.tokenize import sent_tokenize, word_tokenize

example_string = """
Muad'Dib learned rapidly because his first training was in how to learn.
And the first lesson of all was the basic trust that he could learn.
It's shocking to find how many people do not believe they can learn,
and how many more believe learning to be difficult."""

print("This is the text tokenized by sentence.")
print(sent_tokenize(example_string))

print("This is the text tokenized by word.")
print(word_tokenize(example_string))