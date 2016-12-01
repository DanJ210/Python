from random import *

currentPlayer = 0 #0 = Human, 1 = Computer
score = 0

while(score < 100):
    if(currentPlayer = 0):
        roll == randrange(6)
        score -= roll
        print("Player score: {}".format(score))
        print("Computer score: {}".format(score))
        print("Computer's turn...")
    else(currentPlayer = 1):
        roll == randrange(6)
        score -= roll
        print("Your turn...") 

if(score = 100 && true):
    print("Congratulations, you won")
else:
    print("Sorry, computer won")
