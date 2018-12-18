#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 13:15:17 2018

@author: jacobpelletier
"""
"""
original = "Why, man, he doth bestride the narrow world \
Like a Colossus, and we petty men \
Walk under his huge legs and peep about \
To find ourselves dishonourable graves. \
Men at some time are masters of their fates: \
The fault, dear Brutus, is not in our stars, \
But in ourselves, that we are underlings. \"
"""

madquote = """Why, man, he doth bestride the ADJECTIVE; world 
Like a Colossus, and we petty NOUN; 
VERB; under his huge BODYPART; and peep about 
To find ourselves ADJECTIVE; graves. 
Men at some time are masters of their PLURALnoun;: 
The fault, dear NAME;, is not in our stars, 
But in ourselves, that we are ADJECTIVE;."""

#write a function that replaces the target words from a string with parts of speech
def word_in_pos(word, parts_of_speech): #1
    for pos in parts_of_speech: #2
        if pos in word: #3
            return pos #4
    return None #5

parts_of_speech = ["ADJECTIVE;", "NOUN;", "BODYPART;", "PLURALnoun;", "NAME;", "VERB;"]
def madlib(madquote, parts_of_speech):
    replaced = []
    madquote = madquote.split()
    for word in madquote:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            user_input = (input("type in a " + replacement + " ") + " ")
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word + " ")
    replaced = "".join(replaced)
    return replaced
print (madlib(madquote,parts_of_speech))


