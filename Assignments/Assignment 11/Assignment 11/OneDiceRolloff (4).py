from random import *

currentPlayer = 0 #0 = Human, 1 = Computer
scoreH = 0
scoreC = 0
dice = 0

# Daniel Jackson - Assignment 11 - Random Dice Game
#I am playing around trying to learn what I read with functions. ]
#Fun I can't help it! I know that to a programmer this is probably a mess but It works tho!

# Defining a function that rolls a dice, pretty much gets a random number in a range of 6.
def rolling(dice):
    dice = 0
    dice = randrange(1,7)
    return dice

# The two function below are called to print the roll for that turn except if it's
#greater than or equal to 5, I have it print with an exclamation mark.
def humanRoll(rollNumber):
    if (roll >= 5):
        print("You rolled a " + str(roll) + "!")
    else:
        print("You rolled a " + str(roll))
    return

def cpuRoll(rollnumber):
    if(roll >= 5):
        print("The CPU rolled a " + str(roll) + "!")
    else:
        print("The CPU rolled a " + str(roll))
    return

# This loop will run while scores are less than 100.
while(scoreH < 100 and scoreC < 100):
    if(currentPlayer == 0):
        roll = rolling(dice)
        humanRoll(roll)
        scoreH += roll
        currentPlayer = 1
        # this if statement is to check if someone won before printing that it is the next person's turn otherwise it will print who won and their winning score.
        if(scoreH >= 100):
            print("\nPlayer score: {}".format(scoreH))
            print("\nCongratulations, you won")
            break
        elif(scoreC >= 100):
            break
        else:        
            print("Player score: {}".format(scoreH))
            print("Computer's turn...\n")
    if(currentPlayer == 1 and scoreC < 100):
        roll = rolling(dice)
        cpuRoll(roll)
        scoreC += roll
        currentPlayer = 0
        # Same as the if statement above for scoreH, if the computer did win I want to print its score and the winning message, otherwise continue and print 
        #next players turn.
        if(scoreC >= 100):
            print("Computer score: {}".format(scoreC))
            print("\nSorry, computer won")
            break
        else:
            print("Computer score: {}".format(scoreC))
            print("Your turn...\n")