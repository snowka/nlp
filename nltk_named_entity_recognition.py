# This script will identify named entities in a text.
# from https://realpython.com/nltk-nlp-python/#using-named-entity-recognition-ner

import nltk
from nltk.tokenize import word_tokenize

# The commented-out script is for a simple example at the start of the execise.
# nltk.download("averaged_perceptron_tagger")
# lotr_quote = "It's a dangerous business, Frodo, going out your door."
# words_in_lotr_quote = word_tokenize(lotr_quote)
#
# lotr_pos_tags = nltk.pos_tag(words_in_lotr_quote)
# print(lotr_pos_tags)
# nltk.download("maxent_ne_chunker")
# nltk.download("words")
# tree = nltk.ne_chunk(lotr_pos_tags)
# tree.draw()

quote = """
Men like Schiaparelli watched the red planet—it is odd, by-the-bye, that
for countless centuries Mars has been the star of war—but failed to
interpret the fluctuating appearances of the markings they mapped so well.
All that time the Martians must have been getting ready.

During the opposition of 1894 a great light was seen on the illuminated
part of the disk, first at the Lick Observatory, then by Perrotin of Nice,
and then by other observers. English readers heard of it first in the
issue of Nature dated August 2."""

def extract_ne(quote):
    words = word_tokenize(quote, language="english")
    tags = nltk.pos_tag(words)
    tree = nltk.ne_chunk(tags, binary=True)
    return set(
        " ".join(i[0] for i in t)
        for t in tree
        if hasattr(t, "label") and t.label() == "NE"
    )

print(extract_ne(quote))