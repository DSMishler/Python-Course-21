# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 18:09:48 2021

@author: Daniel Mishler
"""

import utils
import json

def monsterFromFile(filename):
    f = open(filename,"r")
    text = f.read()
    monsterDict = json.loads(text)
    name = monsterDict['name']
    
    ACtext = monsterDict['otherArmorDesc']
    ACSeparated = ACtext.split()
    AC = int(ACSeparated[0])
    
    conPoints = int(monsterDict['conPoints'])
    if (conPoints % 2) == 1: # if conPoints is odd
        conPoints -= 1 # Make it even
    conMod = (conPoints - 10) / 2
    hitDice = int(monsterDict['hitDice'])
    hitPointsFloat = hitDice*(4.5+conMod) # Assume all monsters use D8
    # Average of D8 is 4.5. What if it needs rounded?
    hitPointsRound = round(hitPointsFloat,0) # Round up
    HP = int(hitPointsRound)
    
    actions = monsterDict['actions']
    if type(actions) is list:
        # Then should check every one or just first one.
        attack = actions[0]
    elif type(actions) is dict:
        attack = actions
    else:
        print("Bad monster file")
        return None
    details = attack['desc']
    
    # Attack bonus
    firstPlus = details.find("+")
    prunedText = details[firstPlus+1:]# Get everything after the +
    prunedTextList = prunedText.split()
    attackBonusSolo = prunedTextList[0]
    attackBonus = int(attackBonusSolo)
    
    # Damage bonus
    # Find the info in parantheses ().
    
    openParen = details.find('(')
    closeParen = details.find(')')
    dieAndBonus = details[openParen+1:closeParen]
    dieAndBonusArray = dieAndBonus.split()
    die = dieAndBonusArray[0]
    bonus = dieAndBonusArray[-1]
    damageBonus = int(bonus)
    
    dieArray = die.split('d')
    
    dieCount = int(dieArray[0])
    dieType = int(dieArray[1])
    
    dice = []
    for i in range(dieCount):
        dice.append(utils.Die(dieType))
    
    damageDie = utils.Dice(dice)
    
    f.close()
    monster = utils.rollingMonster(HP,damageDie,damageBonus,
                                   attackBonus,AC,name)
    return monster

newMonster = monsterFromFile("skeleton.monster")
newMonster.show()
newMonster2 = monsterFromFile("zombie.monster")
newMonster2.show()