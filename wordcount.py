#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
__author__ = "Andrew Fillenwarth, help from Doug Enas"

import sys
import itertools
import collections
from string import whitespace, punctuation

def create_word_dict(filename):
    """Returns a word/count dict for the given file without punctuation."""
    word_count_dict = {}
    clean_word_list = []
    counts = collections.Counter()
    with open(filename) as book:
        for line in book.readlines():
            for word in line.lower().split():                   
                word_char_list = list(word)                     #Create a list of lowercase characters for each word
                for position in range(len(word_char_list)):     #Loop through and examine each character 
                    if word_char_list[position] in punctuation: #Check if the current character appears in the punctuation list     
                        word_char_list[position] = ''           #Remove the character if it does appear in the list 
                clean_word = ''.join(word_char_list)            #Join the list of characters into a string 
                clean_word_list.append(clean_word)              #Add that string to a list of lowercase words without punctuation 
        counts.update(clean_word_list)                          #Update the Counter Object with the list of clean words  
        word_count_dict = dict(counts)                          #Convert Counter object to a dictionary 
    return word_count_dict


def print_words(filename):
    """Prints one per line '<word> : <count>', sorted
    by word for the given file.
    """
    new_dict = create_word_dict(filename)
    dict_items = new_dict.items()
    sorted_items = sorted(dict_items)                                           #Thanks to Doug for the walk through!
    for word in sorted_items:
        print(str(word[0]) + ': ' + str(word[1]))
    return sorted_items


def print_top(filename):
    """Prints the top count listing for the given file."""
    new_dict = create_word_dict(filename)                                       #Thanks to Doug for the walk through!
    dict_items = new_dict.items()
    sorted_items = sorted(dict_items, key=lambda x: x[1], reverse=True)
    for word in sorted_items[:20]:
        print(str(word[0]) + ': ' + str(word[1]))
    return sorted_items

#print(print_words('books/alice.txt'))

# This basic command line argument parsing code is provided and calls
# the print_words() and print_top() functions which you must implement.
def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
