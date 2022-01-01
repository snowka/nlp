# This provides the most basic elements of a program using spaCY.
# Information from https://realpython.com/natural-language-processing-spacy-python/
# Before this, you must import spaCY with "pip install spacy" and
# download the models and date for the English language with
# python -m spacy download en_core_web_sm

import spacy
nlp = spacy.load('en_core_web_sm')
introduction_text = ('This tutorial is about Natural'
    ' Language Processing in Spacy.')
introduction_doc = nlp(introduction_text)
# Extract tokens for the given doc
print ([token.text for token in introduction_doc])