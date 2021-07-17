# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
# Could just do numpy

# You should receive the exact same results as me if we seed the same.
random.seed(1)

print(random.random())

def roll1d6():
    roll = random.randint(1,6)
    return roll

def roll1dAny(rollMax):
    roll = random.randint(1,rollMax)
    return roll

def rollManyd6(rollNum):
    roll = 0
    for i in range(rollNum):
        roll += random.randint(1,6)
    return roll

def rollManydAny(rollNum,rollMax):
    roll = 0
    for i in range(rollNum):
        roll += random.randint(1,rollMax)
    return roll

class Die:
    def __init__(self,dieMax,dieMin = 1,dieName = None):
        # self.hidden_variable=False
        self.min = dieMin
        self.max = dieMax
        if dieName == None and dieMin == 1:
            self.name = "d"+str(self.max)
        elif dieName == None:
            self.name = "d"+str(self.min)+"-"+str(self.max)
        else:
            self.name = dieName
    def roll(self):
        return random.randint(self.min,self.max)
    def loudRoll(self):
        result = random.randint(self.min,self.max)
        print("%s roll: %d"%(self.name,result))
        return result

class DieGroup:
    def __init__(self,dieList,groupName=None):
        self.dice = dieList
        # Find a way to fix the program if I pass in non-dice?
        if groupName == None:
            self.name = ""
            for die in self.dice:
                self.name+=die.name
        else:
            self.name = groupName
    def roll(self):
        # A function CAN have the same name as a variable.
        result = 0
        for die in self.dice:
            result += die.roll()
        return result
    def loudRoll(self):
        result = 0
        for die in self.dice:
            result += die.loudRoll()
        print("%s roll: %d" % (self.name,result))