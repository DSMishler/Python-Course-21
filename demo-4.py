# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 17:28:43 2021

@author: Daniel Mishler
"""
# Class 4:
# Files and dictionaries


# import. from, as, and standard
# utils.py
# test code (separate window)
# file I/O basics
    # Rolling many dice
    # Determining the range of the dice set and mean, median, mode from file!
# specific reading and writing
    # What is a dictionary? (Just kidding, we're covering them after all)
    # json and .monster files

# Three ways to import.
# Method 1 (Tied for most common)

import utils

# myNewDie = utils.Die(6)

# print(myNewDie.roll())

# Method 2 (Tied for most common)
"""
import utils as Ut
myNewDie = Ut.Die(6)
print(myNewDie.roll())
"""
# Method 3 (generally considered bad practice, but sometimes fine!)
"""
from utils import * # Star means "everything"
myNewDie = Die(6)
print(myNewDie.roll())
"""
# This is not great because we don't know where our classes, functions
# came from!



# Files

# Opening a file
newFile = open("newfile.txt","r")
# function(filename, [r,w,a])
# r: open file for reading
# w: open file for writing
# a: open file for appending
fileText = newFile.read()
print(fileText)
# ALWAYS close files when you're done with them
newFile.close()

newFile = open("newfile.txt", "a")
# Anything in the file will be removed when it is opened for writing!
# If you don't want to do this, then append to the file!
newFile.write("hello!\n") # You can ONLY write to files open for writing,
        # Likewise you can only read from files open for reading.
newFile.close()

# "\n" means newline!
# newFile = open("../eyecare.jpg","rb")
# "rb" means read binary, it's a way to tell python to ignore the fact
# that you probably don't know what you're doing.


# myDice = utils.Dice([utils.Die(8),utils.Die(6),utils.Die(4)])
# diceWrite = open("diceResults.txt","w")
# for i in range(1000):
#     result = myDice.roll()
#     diceWrite.write(str(result))
#     diceWrite.write("\n")

# diceWrite.close()

diceRead = open("diceResults.txt","r")
diceNumbers = diceRead.read()
numbersList = diceNumbers.split() # split splits along newlines and spaces
for number in numbersList:
    # The "number" you see is a copy of the "number" that exists in the array
    # This WOULD work for classes because they are "mutables"
    # A "mutable" only exists in one place
    # "copies" of a mutable are actually just other ways to access the same thing.
    number = int(number)

realNumbersList = []
for number in numbersList:
    realNumbersList.append(int(number))

diceRead.close()


# Dictionaries
myDict = {"Name": "Daniel", "Height": 71}
# A dictionary is a LIST that is INDEXED by its KEYS

import json

skellyfile = open("skeleton.monster","r")
text = skellyfile.read()
skellyDict = json.loads(text)
skellyfile.close()
