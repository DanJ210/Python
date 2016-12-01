from random import *

currentPlayer = 0 #0 = Human, 1 = Computer
scoreH = 0
scoreC = 0
dice = 0

# Defining a function that rolls a dice, pretty much gets a random number in a range of 6.
def rolling(dice):
    dice = 0
    dice = randrange(6)
    return dice
# This loop will run while scores are less than 100.
while (scoreH < 100 and scoreC < 100):
    if(currentPlayer == 0):
        scoreH += rolling(dice)
        currentPlayer = 1
        # this if statement is to check if someone won before printing that it is the next person's turn otherwise it will print who won and their winning score.
        if(scoreH >= 100):
            print("Player score: {}".format(scoreH))
            print("Congratulations, you won")
            break
        #elif(scoreC >= 100):
            #break
        else:        
            print("Player score: {}".format(scoreH))
            print("Computer's turn...")
    if(currentPlayer == 1 and scoreC < 100):
        scoreC += rolling(dice)
        currentPlayer = 0
        # Same as the if statement above for scoreH, if the computer did win I want to print its score and the winning message, otherwise continue and print 
        #next players turn.
        if(scoreC >= 100):
            print("Computer score: {}".format(scoreC))
            print("Sorry, computer won")
            break
        else:
            print("Computer score: {}".format(scoreC))
            print("Your turn...")