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


newfile = open("newfile.txt","w")
for i in range(5):
    newfile.write(str(i)+'\n')
newfile.close()

readfile = open("newfile.txt","r")
text = readfile.read()
words = text.split()
for line in words:
    print(line)


monsterFile = open("zombie.monster","r")
data = monsterFile.read()
print(data)
import json
dictionary = json.loads(data)
print(dictionary)
