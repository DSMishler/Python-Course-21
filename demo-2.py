# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:37:06 2021

@author: Daniel Mishler
"""

# Demo 2: Classes and random numbers

import random
# import is for libraries
# libraries are extra functions that are still part of python!
# you just access them differently.

# print(random.randint(1,2)) # random number between 1 and 2

# Where is Python in this big list of numbers?
# It's at the *Seed*
random.seed(6)
print(random.randint(1,2))
print(random.randint(1,2))
print(random.randint(1,2))

def d6():
    return random.randint(1,6)

# Classes
# A class is an object in Python that has data (variables) and methods

class D6:
    # every time you make a class, you have to use this function.
    # And the first argument has to be "self"
    def __init__(self):
        return
    def roll(self): # Always use "self" as first argument!
        return random.randint(1,6)

# Once a class exists, you can make many of that class.
# You store the class in a variable!
myD6 = D6()
print(myD6.roll())

class Die:
    def __init__(self,dieMax):
        self.max = dieMax
        self.name = "d"+str(self.max)
        return
    def roll(self): # Always use "self" as first argument!
        return random.randint(1,self.max)
    def loudRoll(self):
        result = random.randint(1,self.max)
        print(self.name,"rolls",result)
        return result

myDie = Die(9)

class Dice:
    def __init__(self,dieList):
        self.dice = dieList
        return
    def rollCall(self):
        for i in self.dice: # For each die
            print(i.name)
    def roll(self):
        result = 0
        for i in self.dice:
            result += i.roll()
        return result
    def loudRoll(self):
        result = 0
        for i in self.dice:
            result += i.loudRoll()
        print("group total:",result)
        return result

mySecondDie = Die(7)
myList = [myDie,mySecondDie]
myDice = Dice(myList)

