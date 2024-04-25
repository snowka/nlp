# this script will iterate through all the files in the designated folder,
# open each, remove any characters that are not ASCII, and then save the file
# again. This can move through a dataset quickly, though it does mean that
# some data is lost, such as ash symbols (the "ae" ligature), smart quotes, some dashes, or
# words with accented letters.

# however, there can still be errors in the dataset that requires further preprocessing.
# i've included "print(file_path)" in the read_text_file() function, which prints the
# name of each file as it is opened. if there is an error when a file opens,
# you can correct this by opening the file in Notepad++ and going into the "encoding" tab
# and converting the encoding to "utf-8".

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
    with open(file_path, 'r', encoding="utf-8") as f:
        print(file_path) # print each file as it opens, in case there is an error
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

