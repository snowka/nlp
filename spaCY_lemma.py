# This provides the most basic elements of a program using spaCY.
# Information from https://realpython.com/natural-language-processing-spacy-python/
# Before this, you must import spaCY with "pip install spacy" and
# download the models and date for the English language with
# python -m spacy download en_core_web_sm

import spacy
nlp = spacy.load('en_core_web_sm')
conference_help_text = ('Gus is helping organize a developer'
    'conference on Applications of Natural Language'
    ' Processing. He keeps organizing local Python meetups'
    ' and several internal talks at his workplace.')
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    print (token, token.lemma_)