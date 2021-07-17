# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:59:41 2021

@author: Daniel Mishler
"""

"""

        variableName
        
        VariableName
        
        variable_name

        variablename
"""

def addThree(a)
    return a+3

# Takes in a string of the form "(1+1d4)" or "(1d4)"
# Returns the damage modifier for such a string
def getDamageMod(inStr):            
    fullList = inStr.split()
    if len(fullList > 1): # Then we have something of style A+BdC
        return int(fullList[0])
    else:
        return 0


try:
    newFile = open("newFile.txt","r")
    print(newFile.read())
except:
    print("File not found!")


myName = "Python Student"
print("My name is" + myName, "!")


myNewList = [2,1,0,-1,-2]
print(myNewList.index(0) + myNewList[0])
        