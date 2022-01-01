# This provides the most basic elements of a program using spaCY.
# Information from https://realpython.com/natural-language-processing-spacy-python/
# Before this, you must import spaCY with "pip install spacy" and
# download the models and date for the English language with
# python -m spacy download en_core_web_sm

# To visualize a dependency parse or named entities from a text in a browser or Jupyter notebook.
# Despite the address in the console, the web address to see the results is
# http://127.0.0.1:5000

import spacy
from spacy import displacy

nlp = spacy.load('en_core_web_sm')

about_interest_text = ('He is interested in learning'
    ' Natural Language Processing.')
about_interest_doc = nlp(about_interest_text)
displacy.serve(about_interest_doc, style='dep')