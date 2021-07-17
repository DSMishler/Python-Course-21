# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 20:00:39 2021

@author: Daniel Mishler
"""

# Practice problem 1a:
# Remember the try-except block we learned in class?
# Take a look at this division function

def ironDivision(a,b):
    quotient= a/b
    return quotient

# Go back into that function and use some if statements to handle the
# following:
    # if b is equal to 0, just return "None"
    # if a is not an integer or float, just return "None"
    # if b is not an integer or float, just return "None"

# Practice problem 1b:
# Let's tackle the same problem in a different way

def lazyDivision(a,b):
    quotient= a/b
    return quotient

# This time, fix all of the above problems, except do it
# WITHOUT if statements and do it in no more than 5 lines!

# Practice problem 2:
# Last week, I was hard on you with monsterFromFile. This week, we're
# going to finish it out now.
# You should already have the AC and name of the creature down pat.

# HP:
    # The HP of the monster is calulated as follows:
        # (number of hit dice) * (hit dice average roll + constitution mod)
    # The number of hit dice and the constitution mod are in the monster Dict!
    # The hit dice type is found in the monster's size. If the monster is:
        # Tiny: d4 (average 2.5)
        # Small: d6 (average 3.5)
        # Medium: d8 (average 4.5)
        # Large: d10 (average 6.5)
        # Huge: d12 (average 10.5)
        # Gargantuan: d20
    # Finally, round up if you found something that ends in 0.5

# Attack Bonus:
    # Take a look at the "actions" key. It might be an array, it might
    # be another dict. Figure out how you're going to handle this!
    # Then, once you have a string that has an attack bonus in it,
    # Find out how to pick out that number.
    # I'd recommend looking into the .find() method for strings
    # and knowing how to splice!

# Damage bonus:
    # Just like you found the attack bonus, hunt down the damage bonus
    # in the same string. It can be found in the open and close parentheses!

# Damage diece:
    # Be cautious with this one: it's found next to the damage bonus,
    # but be sure you parse the NUMBER of dice and the TYPE of die correctly,
    # and be ready to create a utils.Dice() array of all the dice used!
    # If you're having trouble, just start with one die instead, and go
    # from there.



# Practice problem 3:
# We're going to bring it all home:
# write a function called "fightFinal" that will:
    # Have a group of monsters fight a second group of monsters.
        # Turn order goes as the following:
            # First alive group A monster attacks first alive group B monster
            # First alive group B monster attacks first alive group A monster
            # Second alive group A monster attacks first alive group B monster
            # Second alive group B monster attacks first alive group A monster
            # Third alive group A monster attacks first alive group B monster
            # Third alive group B monster attacks first alive group B monster
            # ...
            # And so on. If a monster group only has 3 versus 7, then the
            # group with more monsters gets to all act before the next round
            # starts. So a fighting order with [A1,A2,A3] vs. [B1,B2,B3...B8]
            # might look like:
                # A1 -> B1
                # B1 -> A1
                # A2 -> B1 (kills it)
                # B2 -> A1
                # A3 -> B2
                # B3 -> A1
                # B4 -> A1 (kills it)
                # B5 -> A2
                # B6 -> A2
                # B7 -> A2
                # B8 -> A2
    # The monsters are all rolling monsters, of course.
    # Also: still print the results of the fight like last assignment,
    # now accounting for the groups.
# You should be able to properly read
    # Zombie
    # Skeleton
    # Acolyte

# Practice problem 4a:
# Have 3 zombies and 3 skeletons fight 6 skeletons.

# Empirically show who wins if the zombies and skeletons array is
# organized so that the zombies act and are hit first.
# A mathematical argument is not good enough. Use python to prove it.
# (one fight is not enough)

# 4b: do the same for if the skeletons act and are hit first.



# Practice problem 5:
"""
Make an extension to our code to include something we don't have yet!
"""
# Suggestion:
# Note that the "Troll" is a class that exists sort of outside the
# normal generic monster class. That's because the troll is special:
# our code infrastructure isn't really designed to handle all these
# special abilities in a generic rolling monster.
# However, we made the troll regenerate before it attacks
# so that it fits into our fight function.
# (shoot, actually there's a bug where it does it before it hits,
# why don't you go ahead and fix that?)
# Pick any monster that has a special ability like the troll.
# (Hell, even the Zombie's undead fortitude is good enough)
# And make a monster class for it.

# Suggestion:
# Add an initiative system for the monsters

# Suggestion:
# Implement a mechanic of ranged attacks versus melee attacks

# Suggestion:
# Implement ciritical attacks (roll 20 = autohit and double dice)
# alongisde critical fails (roll 1 = miss your attack)

# Or anything else that you wish!
# Submit any relevant changes to known files to me as well.
# For this assignment, it is okay if you change utils.py