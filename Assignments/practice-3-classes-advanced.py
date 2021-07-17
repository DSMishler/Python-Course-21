# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 09:49:26 2021

@author: Daniel Mishler
"""

# Practice set 3: advanced classes

# Practice problem 1:
# Go ahead and copy the code for the generic monster class that we made in class.




# Now initialize three zombies (health 22, damage 1+1d6)
# (Pst... if you can't run the code after just copying the zombie init code,
          # think about what class you might be missing in this file still)




# Now create an list called zombies that contains the three zombies you made.


# Now use a for loop to iterate through the list
    # and print the stats of each zombie.



# Practice problem 2:
# Remember that "fight" function that we made earlier?
# We're going to make a similar function called "fightMany"
# It takes in two arguments:
    # The first is a single strong monster
    # The second is a list of many other monsters teaming up against it
# Remember that in order to make this function you'll have to have *all*
# of the other creatures act and do their damage each round.
# Write your function here:

# Do some experimentation now & run the code as needed to check:
    # How many zombies does it take to beat a troll?
        # Trolls have 84 HP and do 28 damage.
    # (yes, there is some randomness, but 3 is not enough.)


# Practice problem 3:
# Go back up to the generic monster class. Copy and paste it here.
# Change the class name to "rollingMonster".
# We need to add two data values:
    # Attack bonus (name it whatever you want)
    # Armor class (name it watever you want)
# Both of these data values will need to be passed as
        # arguments to the class in __init__()

# You should *also* make a new method called "attack."
# This method will simply roll a d20 and add the monster's attack bonus.
# Write the class here



# Also, go ahead and initialize a rolling zombie:
    # HP 22
    # Damage 1+1d6
    # Attack bonus +3
    # Armor class 8
# And a rolling skelton:
    # HP 15
    # Damage 2+1d6
    # Attack bonus +4
    # Armor class 13





# Practice problem 4:
# Remember that "fight" function that we made in class?
# We're going to make yet another similar function called "fightRoll"
# It takes the same structure of arguments that the one in class takes,
# Except these monsters must both be rolling monsters.
# This function will add the iconic step of D&D combat into the mix:
    # A monster will first roll.
    # If the monster's attack score is >= the opponent's Armor Class:
        # Then do damage
    # Otherwise
        # No damage is dealt.
    # Action passes to the other monster
    # Repeat until we have a winner
# Write that function here



# Go ahead and fight a zombie and a skeleton again.
# Let the skeleton go first. Is it still a zombie win every time?






# Practice problem 5:
# Let's bring it all together: make a function called "fightManyRoll"
# That allows a single rolling monster to fight many rolling monsters.
# Go ahead and make a "rollingTroll" monster too (AC of 15, +7 to hit)
# write it here and set a troll up in a fight with a bunch of zombies.
# How many zombies does it take to win now?