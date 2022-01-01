# This provides the most basic elements of a program using spaCY.
# Information from https://realpython.com/natural-language-processing-spacy-python/
# Before this, you must import spaCY with "pip install spacy" and
# download the models and date for the English language with
# python -m spacy download en_core_web_sm

# Using these examples from Real Python
# Variable names ending with the suffix _text are Unicode string objects.
# Variable name ending with the suffix _doc are spaCy’s language model objects.

import spacy
nlp = spacy.load('en_core_web_sm')
about_text = ('Gus Proto is a Python developer currently'
              ' working for a London-based Fintech'
              ' company. He is interested in learning'
              ' Natural Language Processing.')
about_doc = nlp(about_text)
sentences = list(about_doc.sents)
x = len(sentences)

# This part of the script iterates through the about_doc variable
# and tokenizes the text and includes the following attributes
# text_with_ws prints token text with trailing space (if present).
# is_alpha -- detects if the token consists of alphabetic characters or not.
# is_punct -- detects if the token is a punctuation symbol or not.
# is_space -- detects if the token is a space or not.
# shape_ -- prints out the shape of the word.
# is_stop -- detects if the token is a stop word or not.

# If need be, the tokenizer can be customized by altering the tokenizer property of the nlp object.
# See https://realpython.com/natural-language-processing-spacy-python/

for token in about_doc:
    print (token, token.idx, token.text_with_ws,
           token.is_alpha, token.is_punct, token.is_space,
           token.shape_, token.is_stop)