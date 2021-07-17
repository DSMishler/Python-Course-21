# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 20:33:16 2021

@author: Daniel Mishler
"""

# Goal: fight two monsters
# Will take six weeks
# Week 1: the basics
# The only week where we do not directly work towards the above goal.

# What is Python?
# Python is a coding language designed for people who don't understand computers
# However, it is still useful to experts.

# What is a function?
# something that takes zero or more inputs and does something.
# In python, all functions are called with ()
# This means print() is a function, but print will not work

# What is a variable
# Everything else that is not defined as a function or some other
# Token in Python is reserved to you the user as a variable.

# int: integer
# str: string (one or more words, usually denoted by quotes)
# float: a real number, usually not an integer. Stands for "floating point"

# All lines with a "#" in front are ignored

print(10)

# Whenever you run this file, all the things in this file are run
# Because of this, it's usually good practice not to have a lot of things
# in a single file.

# Variables and variable names
myVariable = 1
# What to name my variables?
# "print" is a terrible name for your variable, for example
# Because print() is already a function!
# If your variable name highlights itself, change it!

# XXXX: my Variable = 2

# Camel Case: myVariable
# Pascal Case: MyVariable
# Snake Case: my_variable

mySecondVariable = 2

print(myVariable)
print(mySecondVariable)
print() # Just adds a line of space

myVariable = 3

print(myVariable)
print(mySecondVariable)
print() # Just adds a line of space

myVariable = mySecondVariable
# The equals sign takes what is on the right and stores it
# in what is on the left without changing what is on the right

print(myVariable)
print(mySecondVariable)
print() # Just adds a line of space

mySecondVariable = 6

print(myVariable)
print(mySecondVariable)
print() # Just adds a line of space

# Golden rule of variables:
    # A variable will NEVER change unless you explicitly change it


# whenever you write a function, it's available for all time after
# it is defined.
# The "argument" could be anything.
def Yell(argument):
    # Begin the scope
    # Everything at this indentation is part of the function
    # "Yell" will take a string and print it uppercased.
    # The string will be called "argument"
    # This is a new variable that only exists in the scope of the function
    print(argument.upper())
    # Python is full of googling and stack overflow.
    # Strings all have a built-in "method" called upper(). They
    # have other methods too!
# Returning to this indentation level means the function is complete.

Yell("Hello")

def Cubed(number):
    # Take a number and cube it
    answer = number*number*number
    # We could "print" the answer, but usually unless you're
    # specifically told to print, we use "return" instead.
    return answer

myVariable = Cubed(2)

print(myVariable)
print(mySecondVariable)
print() # Just adds a line of space

myVariable = Yell("hello")

print(myVariable)
print(mySecondVariable)
print() # Just adds a line of space


"""
def Spell(number):
    # Take a 1, 2, or 3. And print "One", "Two", or "Three"
    if number == 1:
        # == means comparison!
        print("One")
    if number == 2:
        print("Two")
    if number == 3:
        print("Three")
"""

def Spell(number):
    # Take a 1, 2, or 3. And print "One", "Two", or "Three"
    if number == 1:
        # == means comparison!
        print("One")
    elif number == 2:
        print("Two")
    elif number == 3:
        print("Three")

# More variable types

# int
# floats
# strings

# list
myList = [1,2,3]

# arrays exist, but just pretend everything is a list for now.

print(myList)
print(myList[1]) # key takeaway: We index from 0 here
print(myList[0])
print(myList[2])
print(myList[-1])

# tuple
myTuple = (4,5)
# Think of a tuple as a nerfed list.
print(myTuple[1])
print(myTuple[-1])
# Tuples are thought of as ordered pairs (or triplets)

# dictionary. They exist but won't be important today

# "Raised to the power of": **






