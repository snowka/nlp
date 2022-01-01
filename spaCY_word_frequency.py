# This provides the most basic elements of a program using spaCY.
# Information from https://realpython.com/natural-language-processing-spacy-python/
# Before this, you must import spaCY with "pip install spacy" and
# download the models and date for the English language with
# python -m spacy download en_core_web_sm

import spacy
from collections import Counter

nlp = spacy.load('en_core_web_sm')

complete_text = ('Gus Proto is a Python developer currently'
    'working for a London-based Fintech company. He is'
    ' interested in learning Natural Language Processing.'
    ' There is a developer conference happening on 21 July'
    ' 2019 in London. It is titled "Applications of Natural'
    ' Language Processing". There is a helpline number '
    ' available at +1-1234567891. Gus is helping organize it.'
    ' He keeps organizing local Python meetups and several'
    ' internal talks at his workplace. Gus is also presenting'
    ' a talk. The talk will introduce the reader about "Use'
    ' cases of Natural Language Processing in Fintech".'
    ' Apart from his work, he is very passionate about music.'
    ' Gus is learning to play the Piano. He has enrolled '
    ' himself in the weekend batch of Great Piano Academy.'
    ' Great Piano Academy is situated in Mayfair or the City'
    ' of London and has world-class piano instructors.')

complete_doc = nlp(complete_text)
# Remove stop words and punctuation symbols
words = [token.text for token in complete_doc
         if not token.is_stop and not token.is_punct]
word_freq = Counter(words)
# 5 commonly occurring words with their frequencies
common_words = word_freq.most_common(5)
print (common_words)

# Unique words
unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
print (unique_words)