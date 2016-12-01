# Daniel Jackson - Assignment 14 - Rock, Paper, Scissor
#----- I put dashes like this in front of my comments to easily differentiate.

from random import *
#------ Imporeted sys just to exit upon inputing a 0
import sys

# userPick function gets a valid choice from the user and returns it
def userPick():
    userChoice = 4
    userChoice = int(input("\nEnter a (1) for rock, (2) for paper, (3) for scissors, or (0) to quit:\n"))
    if (userChoice == 0):
        sys.exit(0)
    while(userChoice < 0 or userChoice > 3):
        print("Invalid choice. Try again.\n")
        break
    return userChoice

# compPick function gets a valid choice from the computer and returns it
def compPick():
    return randrange(1, 3)

# displayPick function takes a 1, 2, or 3, and returns the string "rock", "paper", "scissors"
#   if an invalid value is received, it returns "nothing"
def displayPick(value):
    if(value == 1):
        return "rock"
    elif(value == 2):
        return "paper"
    elif(value == 3):
        return "scissors"
    else:
        return "invalid"

# determineWinner function takes a 1, 2, or 3 from 2 players and comparese based on:
#   1 = rock, 2 = paper, 3 = scissors
#   rock beats scissors, paper beats rock, and scissors beats paper
# The function returns a 1 if player 1 wins, 2 if player 2 wins, and 0 if a tie
# If one of the values is not valid, that player loses. If both numbers are invalid, it is a tie.

#------- I deleted some code the added a return of 4 for another output.
def determineWinner(player1Choice, player2Choice):
    if(player1Choice == 1):
        if(player2Choice == 1):
            return 3
        elif(player2Choice == 2):
            return 2
        else:
            return 1
    elif(player1Choice == 2):
        if(player2Choice == 1):
            return 1
        elif(player2Choice == 2):
            return 3
        else:
            return 2
    elif(player1Choice == 3):
        if(player2Choice == 1):
            return 2
        elif(player2Choice == 2):
            return 1
        else:
            return 3
    else:
        return 4

# playGame function takes the number of rounds and plays that many rounds.
#  It keeps track of the score, and returns the scores.
#------- The 4 returned above comes in play here, actually anything would trigger it, but if user input
#------- is invalid then I let the player no and still give CPU a point by default.
def playGame(rounds):
    userScore = 0
    compScore = 0
    for turn in range(rounds):
        winner = playRound()
        if(winner==1):
            userScore += 1
            print("--You win this round")
        elif(winner==2):
            compScore += 1
            print("--Computer wins this round")
        elif(winner==3):
            print("--Tie this round")
        else:
            compScore += 1
            print("Invalid Choice - Computer defaults a point.")
    print()
    #------ I saw that you were already returning two values at once which is when I figured out
    #------ the double games being played and each value was being stored one at a time.
    return userScore, compScore

# playRound function calls the functions to get the user's and the computer's selection.
#   It returns the 0, 1, or 2 to determine tie, user win, or computer win.
def playRound():
    userChoice = userPick()
    compChoice = compPick()
    print("You chose " + displayPick(userChoice))
    print("The computer chose " + displayPick(compChoice))
    return determineWinner(userChoice, compChoice)
    
def main():
    numRounds = int(input("Enter the number of rounds: "))
    while(numRounds < 1):
        print("Number must be positive.")
        numRounds = int(input("Enter the number of rounds: "))
    #----- I finally figured this issue out and became very happy
    userScore, compScore = playGame(numRounds)
    print("Your score: {}\nComputer score: {}".format(userScore, compScore))
    if(userScore > compScore):
        print("You Win!!")
    elif(compScore > userScore):
        print("Computer Wins!!")
    else:
        print("Tie Game")


main()
