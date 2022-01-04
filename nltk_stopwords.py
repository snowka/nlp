# This script filters out stop words
# from https://realpython.com/nltk-nlp-python/
# Leave out the first line of the example [nltk.download("stopwords")] --
# it does not work and is not necessary.

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

worf_quote = "Sir, I protest. I am not a merry man!"

words_in_quote = word_tokenize(worf_quote)

stop_words = set(stopwords.words("english"))

filtered_list = []

filtered_list = [
    word for word in words_in_quote if word.casefold() not in stop_words
]

print(filtered_list)