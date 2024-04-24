# this script will iterate through all the files in the designated folder,
# open each, remove any characters that are not ASCII, and then save the file
# again. This can move through a dataset quickly, though it does mean that
# some data is lost, such as words with ash symbols (the "ae" ligature) or
# words with accented letters.

# however, I still have further preprocessing to complete. I receive an error every
# 20 files or so I receive this error like this, with different positions:
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 3524: ordinal not in range(128)
# there is a character that was not handled well when the dataset was created, or more.
# As a result, I need to cut-and-paste each file that fails when I run the program (it
# is the last one printed) into the test.py file and search for the position that
# caused the error. Then, I need to go into the file and delete the offending character.


# to read multiple text files from a directory, from
# https://www.geeksforgeeks.org/how-to-read-multiple-text-files-from-folder-in-python/
# Import Module
import os

# Folder Path
path = "C:/Users/snowka/PycharmProjects/nlp/data"

# Change the directory
os.chdir(path)

# Read text File


def read_text_file(file_path):
    with open(file_path, 'r', encoding="ascii") as f:
        print(file_path)
        content = f.read()
        text_before_processing = content
        # the .encode() method turns the string to bytes and ignores any characters
        # that are not ASCII
        text_after_processing_bytes = text_before_processing.encode(encoding="ascii", errors="ignore")
        # the .decode() method turns the bytes back into a string
        text_after_processing_string = text_after_processing_bytes.decode(encoding="ascii", errors="ignore")
        with open(file_path, "w") as n:
            n.write(text_after_processing_string)


# iterate through all files in the directory
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}/{file}"
        # call read text file function
        read_text_file(file_path)

