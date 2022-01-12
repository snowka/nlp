#!/usr/bin/env python
# coding: utf-8

# In[1]:

# The following was largely created by Brian Tarpley of the Center of Digital Humanities Research (CoDHR) and
# included as part of their "Python for Humanists" course. I have made my own adjustments while learning
# to use the NLTK package for literary analysis.

# Word Freq'ing

# The following expands on the "Book" class we
# created during our last class session by adding
# new properties and methods to enable a) the removal
# of Project Gutenberg boilerplate text via regular
# expressions, and b) the running of a simple word
# frequency analysis, introducing us to the concepts
# of tokenizing, removing stop words, part-of-speech
# tagging, lemmatizing, and frequency distributions.

import os
import re

# The import statement above imports the "re" library,
# which supports the use of Regular Expressions in Python.
# The term "Regular Expressions" can refer to specific
# pattern-matching specifications for matching or capturing
# parts of a string. It also, however, refers to the
# _syntax_ you use to construct those specifications.
#
# We'll touch on them in an introductory way today and
# cover them more fully when we dive into XML later in
# the course.

import nltk

# The above line imports the "nltk," or "Natural Language Toolkit"
# library. Unlike the libraries we've used so far, however, nltk is
# _not_ part of the Python Standard Library, and so, like all external
# libraries, it must be installed on your computer before you can
# import it into your code, and should be understood in terms of how
# to import and use it appropriately.
#
# Most external Python libraries (like nltk) are registered with
# PyPI (the Python Package Index). You can search PyPI here:
#
# https://pypi.org/
#
# If a Python library is registered with PyPI, and if you happen to
# have Python installed on your computer, you can install an external
# library using your computer's command prompt (or Mac terminal) using the
# following command:
#
# pip install [name-of-library-in-PyPI]
#
# Note that some libraries have names in the PyPI index that differ
# from the name you use in your import statement. With nltk, however,
# its PyPI name is the same as its import name, so to install it, run:
#
# pip install nltk
#
# nltk is unusual, however, in that it is a rather large library
# with several optional modules and datasets that require further
# steps to install. You can read about all the optional modules here:
#
# https://www.nltk.org/py-modindex.html
#
# For the purposes of our class, I have made sure our
# learning environment has several nltk modules installed. I
# installed them using the following command:
#
# python -m nltk.downloader punkt stopwords wordnet averaged_perceptron_tagger

import matplotlib

# The "matplotlib" library is a classic Python library that is
# used to create simple visualizations of data. It is designed
# to function like a plotter, which is a kind of giant printer
# used to print things like blueprints, big posters, etc.
#
# It is also an external library, and can be installed like so:
#
# pip install matplotlib

class Book(object):
    # properties
    contents = ""
    stopped_words = []
    lemmas = []
    pos_tagged = []
    punctuation = [
        '.',
        ',',
        ';',
        '!',
        '?',
        "-",
        '"',
        "'",
    ]

    # methods
    def __init__(self, path_to_book=None):

        # With the line above, we are creating a method called
        # "__init__" (double underscores on both sides), which
        # is a special method that the interpreter _always calls_
        # when instantiating an object. When you do this:
        #
        # my_book = Book()
        #
        # ...you are actually calling the Book class' .__init__()
        # method. If you don't explicitly define an .__init__()
        # method, the interpreter calls the .__init__() method
        # of the class you inherit in your class definition,
        # which in this case is the "object" class, which as
        # I mention in my lecture notes, is a kind of blank
        # template you can inherit from when creating your own
        # classes.
        #
        # In most object oriented programming languages, the
        # method that gets called when the object is instantiated
        # is referred to as the object's "constructor." In Python,
        # then, the .__init__() method is most commonly referred
        # to as the constructor for your object.
        #
        # In the case above, we're stipulating that the constructor
        # can take a parameter, which in the current code-block can
        # be accessed using the variable name "path_to_book."

        if path_to_book and os.path.exists(path_to_book):
            # The above line first checks if path_to_book is
            # set to something, and then uses the exists()
            # function to see if the string stored in
            # path_to_book actually resolves to a path in our
            # filesystem. The exists() function is part of the
            # "path" namespace, which itself is part of the
            # "os" namespace. You can read about os.path here:
            #
            # https://docs.python.org/3.7/library/os.path.html

            with open(path_to_book, 'r') as my_file:
                # open() is a built-in function that takes
                # two parameters: the path to the file you
                # wish to open, and the "mode" in which you'd
                # like to open it. The options in terms of
                # mode are:
                #
                # 'r': read
                # 'w': write (will delete file contents)
                # 'a': append (will allow you to add to
                #      existing content)
                #
                # The open() function returns an object
                # that represents an open file. Leaving
                # files open is bad practice and can
                # lead to problems, so you normally have
                # to call the file object's .close()
                # method to close the file.
                #
                # The most common method of reading or
                # writing files in Python, however is
                # by using the "with" statement, which
                # tells the interpreter to take whatever
                # the function after the "with" keyword
                # returns and refer to it as the name
                # that appears after the "as" keyword
                # within the code-block the "with"
                # statement designates.
                #
                # After the code-block designated by the
                # "with" statement executes, the
                # interpreter automatically "destroys"
                # the object referred to by the "as"
                # keyword. How an object "destroys"
                # itself is complicated to explain,
                # but in this case the interpreter
                # will take our file object,
                # referred to as "my_file",
                # and gracefully close the file before
                # destroying it.

                self.contents = my_file.read()

                # Here we're setting the "content"
                # property of our Book object to what
                # the .read() method of the file object
                # returns (in this case, a string
                # containing the contents of our file).

    # The .word_count() method takes as a parameter a word to count in
    # .contents. It then strips punctuation, lower-cases, and returns
    # the instances of word_to_count

    def word_count(self, word_to_count):
        total_instances = 0
        text = self.contents

        for punct in self.punctuation:
            text = text.replace(punct, ' ')

        words = text.split()

        for word in words:
            if word.lower() == word_to_count.lower():
                total_instances += 1

        return total_instances

    # The .strip_gutenberg_boilterplate() method hunts for a
    # pattern, using regular expressions, which will be used
    # as a delimiter for the actual contents of the novel. It
    # then splits the text up by that delimiter and only keeps
    # the contents of the novel in .contents

    def strip_gutenberg_boilerplate(self):
        pattern = r'\*\*\* [^ ]* OF THIS PROJECT GUTENBERG EBOOK [^\*]*\*\*\*'

        # The above line makes light use of regular
        # expressions to create a pattern that will
        # match strings that look like this:
        #
        # *** START OF THIS PROJECT GUTENBERG EBOOK EMMA ***
        # *** END OF THIS PROJECT GUTENBERG EBOOK PERSUASION ***
        #
        # This enables parts of the string (START/END, the name
        # of the novel) to be variable and still match the pattern
        # we're looking for.
        #
        # Regular expressions are complicated, and we could spend
        # at least an entire class period learning the syntax. Alas,
        # the following two resources will have to suffice:
        #
        # Regular Expression Cheat Sheet:
        # http://www.rexegg.com/regex-quickstart.html
        #
        # Regular Expression Testing Web App:
        # https://regex101.com/

        book_parts = re.split(pattern, self.contents)

        # The above line uses the .split() function of the "re"
        # library, which takes as two parameters: the pattern you want
        # to delimit your chunks by, and the text you want to split.
        # The function returns a list of the the strings chopped up
        # by your delimiting pattern.

        if len(book_parts) == 3:
            # The if statement above checks to make sure there are
            # now three items in our book_parts list. The first item
            # should be a string containing all the boilerplate above
            # a pattern match, the second the contents of our text,
            # and the third the boilerplate below the matching pattern.

            self.contents = book_parts[1]

            # Since we only want to keep the contents of our text,
            # we can simply set our class' "contents" property to the
            # second item in our list, thereby discarding the
            # boilerplate text :)

    # .create_stopped_words() will lower-case and split
    # .contents into a list of words. It will then iterate
    # over that list of words, removing any words that belong
    # to the default list of English stopwords provided by the
    # NLTK library. The method will also take as an optional
    # parameter a list of additional stopwords to use. The
    # results will be stored in the .stopped_words property
    # as a list.

    def create_stopped_words(self, additional_stopwords=[]):

        # Notice how there's an optional parameter here. The
        # additional_stopwords parameter is "optional" because
        # we've specified a default value for it (an empty list).

        self.stopped_words = []

        # Just in case we call this function multiple times, let's
        # be sure to empty out our list of stopped words!

        lower_cased_content = self.contents.lower()

        # We're lower-casing the contents of the book and storing
        # the results in a new variable called "lower_cased_content."

        for punct in self.punctuation:
            lower_cased_content = lower_cased_content.replace(punct, " ")

        # We're replacing all punctuation marks with spaces in
        # lower_cased_content

        tokens = lower_cased_content.split()

        # We're creating a new variable called "tokens" which
        # contains a list of words delimited by whitespace

        stop_words = list(nltk.corpus.stopwords.words('english'))
        stop_words = stop_words + additional_stopwords

        # Here we're extracting the default English stopword list
        # from the NLTK library, and combining it with the optional
        # list passed in as a parameter, storing the results as a new
        # variable called "stop_words"

        for stop_word_index in range(0, len(stop_words)):
            stop_words[stop_word_index] = stop_words[stop_word_index].lower()

        # The above for-loop makes use of the built-in range() function,
        # which takes two parameters: where you'd like to start and stop
        # your range of numbers, and returns a list of those numbers.
        # We're taking advantage of range() to produce a list of all the
        # indexes in our "stop_words" list, and then iterating over
        # those indexes so we can lower-case each stop word.

        for token in tokens:
            if token not in stop_words:
                self.stopped_words.append(token)

        # Finally, we're iterating through the tokens we created above,
        # and only adding that token to the .stopped_words property if
        # it's not in our stopword list.

    # .create_pos_tagged() will take the list of words in the
    # .stopped_words property, tag them according to their part-of-speech,
    # and then store the results in the .pos_tagged property. We're also
    # creating an optional parameter called "pos_filters," which can take
    # a list of only the parts-of-speech you're interested in collecting.

    def create_pos_tagged(self):

        if self.stopped_words:
            self.pos_tagged = nltk.pos_tag(self.stopped_words)

            # The above line invokes the pos_tag() function of
            # the NLTK library. It returns a list of "tuples,"
            # which for our purposes are just lists with two
            # items. The first item is the word in question,
            # and the second item is a POS tag, like NN for
            # noun, VB for verb, etc. A full list of those
            # tags can be found here:
            #
            # https://pythonprogramming.net/natural-language-toolkit-nltk-part-speech-tagging/

    # .create_lemmas() will take the list of words in the
    # .stopped_words property and find the lemma for each word
    # using a lemmatizer from the NLTK library, storing the results
    # as a list in the .lemmas property.

    def create_lemmas(self):

        pos_tag_map = {
            'JJ': 'a',
            'JJR': 'a',
            'JJS': 'a',
            'RB': 'r',
            'RBR': 'r',
            'RBS': 'r',
            'VB': 'v',
            'VBD': 'v',
            'VBG': 'v',
            'VBN': 'v',
            'VBP': 'v',
            'VBZ': 'v',
        }

        # Whereas the .pos_tag() function of the NLTK library returns
        # a highly granular list of part-of-speech tags, the lemmatizer
        # we'll use below is not so granular. It only broadly understands
        # nouns ('n'), adjectives ('a'), adverbs ('r'), and verbs ('v');
        # or by default assumes everything is a noun.
        #
        # As such, in order to treat the word in question as something
        # other than a noun, we need to pass in the appropriate part of
        # speech to the lemmatizer, and for that we need a way to map
        # the granular pos-tags from the .pos_tag() function to the
        # simpler pos-tags the lemmatizer can understand. For this reason,
        # we create the above "pos_tag_map" dictionary.

        if self.pos_tagged:

            # Since this method relies on .pos_tagged having
            # already been created, we check above to make sure
            # .stopped_words is not empty.

            self.lemmas = []

            lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()

            # The above line creates an instance of the
            # "WordNetLemmatizer" class called "lematizer"

            for word_tag_pair in self.pos_tagged:
                word = word_tag_pair[0]
                tag = word_tag_pair[1]

                # So far in this for-loop, we're iterating over the
                # list of tuples in .pos_tagged and separating out
                # the two items in the tuple into "word" and "tag"
                # variables.

                simplified_tag = pos_tag_map.get(tag, 'n')

                # Since we have the granular
                # pos-tag stored in "tag" and we need the simplified
                # version stored in our "pos_tag_map" dictionary, we're
                # calling the .get() method of the dictionary object
                # which attempts to look up the key you provide as the
                # first parameter in order to return that key's value.
                # Since we're only providing a subset of the possible
                # granular pos-tags in our pos_tag_map dictionary, we
                # also pass into the .get() method a default value to
                # return should that key not exist in the dictionary.
                # In this case, should the granular pos-tag not exist
                # as a key in our pos_tag_map dictionary,
                # "simplified_tag" will be set to 'n' for noun.

                self.lemmas.append(
                    lemmatizer.lemmatize(
                        word,
                        simplified_tag
                    )
                )

                # Finally, we're appending to our .lemmas list
                # the results of our call to the .lematize()
                # method of the "lemmatizer" object we instantiated
                # earlier. The .lematize() function takes two parameters:
                # the word you want to lemmatize, and the optional,
                # simplified pos-tag corresponding to that word.

    # .create_word_freq_analysis() will take four parameters:
    # 1) The path to the .png file you'd like to create, which
    #     will be your word frequency analysis visualization.
    # 2) The width of the resulting image file in inches.
    # 3) The height of the resulting image file in inches.
    # 4) The number of frequent words you'd like to
    #     visualize results for.
    #
    # The method will make use of the nltk library to produce
    # a "frequency distribution" and in turn use matplotlib
    # to save the data as a chart to an image file.

    def create_word_freq_analysis(
            self,
            image_file,
            width=20,
            height=10,
            num_terms=50):

        if self.lemmas and image_file:
            import matplotlib.pyplot as plt

            # Even though we already imported the matplotlib
            # library above, we'll have to import a submodule
            # of that library (pyplot) and give it another
            # name using the "as" keyword. The reason for this
            # is because the NLTK FreqDist object has a method
            # called .plot(), and the code for that method calls
            # plt.show(), which normally does not save the image
            # it generates (it tries to show it using a GUI).
            # To actually save our image when we call that
            # .plot() method, we have to do some tricky stuff
            # and override plt.show(), making it save the image
            # as well. This is definitely a "hacky" solution,
            # and may not be necessary as the NLTK library
            # evolves.

            freq_dist = nltk.probability.FreqDist(self.lemmas)

            # The above line creates an instance of the FreqDist
            # class (part of the nltk.probability module), which
            # you can read about here:
            #
            # http://www.nltk.org/api/nltk.html?highlight=freqdist#nltk.probability.FreqDist
            #
            # This class takes as a parameter in its constructor
            # a list of words (or tokens), and it counts the number
            # of times each word appears in the text, such that the
            # resulting data is a kind of dictionary where there's a
            # key for every unique word (or type), and the value for
            # that key is the number of times that word appears in
            # the list of tokens passed into the constructor.

            freq_dist.pprint(num_terms)

            # The above line makes use of the .pprint() method of the
            # FreqDist class. "pprint" almost always means "pretty print,"
            # and in this case it prints the resulting data as a dict
            # to the console. .pprint() takes as an optional parameter
            # the number of terms (sorted by frequency in descending
            # order) you'd like to print out.

            plt.show = lambda: plt.savefig(image_file)

            # The above line is another "hacky" part of this method.
            # The last line of this method calls the .plot() method
            # of the FreqDist class, which in turn calls "plt.show()".
            # Here, we're actually overriding the code that gets
            # executed when "plot.show()" gets executed. The "lambda"
            # keyword indicates to the interpreter that you're creating
            # a function, and what follows the ":" after "lambda" is
            # the code of that function. Essentially, we're replacing
            # the contents of the .show() method with our own code.

            # "plt.savefig()" is a function that tells the "plotter"
            # (or the matplotlib library) that we want to spit out the
            # contents of our visualization to a file. plt.savefig()
            # takes as a parameter the path to the image file we want
            # to save our visualiztion to (contents of existing file
            # at that path will be overwritten).

            plt.figure(figsize=(width, height), tight_layout=True)

            # "plt.figure()" is a function that allows you to convey
            # to the "plotter" (or matplotlib library) certain
            # specifications about the resulting visualization, such
            # as the width and height (passed in as a tuple), and
            # whether you want the layout to be "tight," which affects
            # the margins of the visualization.

            freq_dist.plot(num_terms, cumulative=False)

            # This last line calls the .plot() method of the FreqDist
            # class, which takes as a parameter the number of terms
            # (sorted by frequency descending) you'd like to include
            # in your visualization, and whether or not you want the
            # the distribution to be calculated cumulatively.
            #
            # By setting cumulative to False, our chart will simply
            # display the number of times a word appears. If you're
            # interested instead in seeing the _probability_ that
            # a word will appear in the text, set cumulative to True.
            #
            # To learn more about cumulative distributions, see here:
            #
            # https://en.wikipedia.org/wiki/Cumulative_distribution_function


# In[2]:


path_to_work = "libertas.txt" # place the file you want to analyze in the same folder as this program and change the filename here
work = Book(path_to_work)
# work.strip_gutenberg_boilerplate() # removed as the source is not from Gutenberg

print("First 200 characters:")
print(work.contents[:200])

print("Last 200 characters:")
print(work.contents[-200:])

# You'll notice that in two of the print statements above, I'm
# using the slicing convention for extracting contents of a list,
# but in the first of those print statements I'm leaving out where
# the slice starts, and in the second, I'm leaving out where the
# slice ends. When you omit the first number for a slice, the
# Python interpreter assumes you mean to start your slice at the
# beginning of your list, and when you omit the second number for a
# slice, the interpreter assumes you mean to end your slice at the
# end of your list.
#
# You'll also note that in that second print statement, I'm using a
# negative number for the start of the slice. When using a list
# accessor, negative numbers are interpreted as "this many slots
# from the end of your list." As such, the second print statement
# prints a slice that starts 200 characters before the end of the
# list, and since there is no ending number specified, it ends at
# the end of the list.

work.create_stopped_words()
print("First 50 stopped words:")
print(work.stopped_words[:50])

work.create_pos_tagged()
print("First 50 POS-tagged words:")
print(work.pos_tagged[:50])

work.create_lemmas()
print("First 50 lemmatized words:")
print(work.lemmas[:50])

analysis_image_file = 'work.png'
work.create_word_freq_analysis(analysis_image_file)


