# Daniel Jackson - Assignment 18 ------------ Did my best to expalin at least to try and help make it easier to read.

import random
# This class you yourself did in class, I took it out of an in class assignment and made it work. I could've done
#two die and I still kind of do, I create two die below in the turns for each player using this one class to generate.
#it could have an inputed value for its sides.
class Die():
    def __init__(self, sides):
        self._sides = sides
    def roll(self):
        return random.randint(1, self._sides)
# Ok so I've decided to make a score class out of nowhere and it's a little sketchy and took some tailoring but
#it does work and it is all my own, the above Die class. This may not even be done correctly but I am so happy
#about it! it's understanding it mentally that is the hard part.
class Score():
    def __init__(self, player=0, cpu=0):
        self.player = player
        self.cpu = cpu
    def pAdd(self, amount):
        self.player += amount
    def cpuAdd(self, amount):
        self.cpu += amount
    def runningTotal(self, amount):
        self.total += amount
# This reads in from the file to an array, I haven't test much  but I made the function able to work with any
#amount of elements, more than 6 elements could be in the file if desired. No issue so far.
def checkFile():
    scoreFile = open("lowscore.txt", "r")
    array = []
    for line in scoreFile:
        array.append(line.strip())
    scoreFile.close()
    return array
# Writes contents of array back to the file.
def writeFile(array):
    file = open("lowscore.txt", "w")
    for line in range(len(array)):
        file.write(str(array[line]) + "\n")
    file.close()
# This checks the last element of the array to do the score swap if necessary. In this case 6
#but the list could be any size except I've only tested larger. I'm using the class values here.
def checkScore(score, array):
    if (score.player > score.cpu):
        if (int(array[len(array) - 1]) > int(countOfRollsP1)):
            array[len(array) - 1] = countOfRollsP1
    else:
        if (int(array[len(array) - 1]) > int(countOfRollsP2)):
            array[len(array) - 1] = countOfRollsP2
# Rolls two die and returns the two values.
def rollDie(d):
    d1 = d.roll()
    d2 = d.roll()
    return d1, d2
# Rolls a 1/3 chance but still kinda 50/50 cause of "<=". Could do a whole lot more than this.
def firstRoll():
    p1, p2 = rollDie(Die(3))
    if (p1 >= p2):
        print ("Player goes first.\n")
        return 1
    else:
        print ("Computer goes first\n")
        return 2   
# Calls the turns while scores under desired amount. (100)
def playGame(roll, score):
    while (score.player < 100 and score.cpu < 100):
        if (roll == 1):
            roll = playerRoll(score)
        else:
            roll = computerRoll(score)
# Player's Turn
def playerRoll(score):
    global countOfRollsP1
    score.total = 0
    choice = 1
    while (choice == 1 and score.player + score.total < 100):
        d1, d2 = rollDie(Die(6))
        score.runningTotal(d1 + d2)
        countOfRollsP1 += 1
        if (d1 == 1 and d2 == 1):
            print("----------Player rolled Snake Eyes")
            print("Aww how sad, you lose all you points and your turn")
            score.total, score.player = 0, 0
            choice = 0
        elif (d1 == 1 or d2 == 1):
            print("----------Player rolled", d1, "and", d2)
            print("You lose your turn and round points")
            score.total = 0
            choice = 0
        else:
            answer = "bad"
            print("----------Player rolled", d1, "and", d2)
            if (countOfRollsP1 >= 1):
                print("Your current score is", score.player)
                print("You could bank", score.total)
                if (score.player != 0):
                    print("Totaling", score.total + score.player)
            while (answer != "good"):
                choice = int(input("Press 0 to bank and continue or 1 to add up and roll again: "))
                if (choice != 0 and choice != 1):
                    print("\nPlease try again")
                else:
                    answer = "good"
                    if (choice == 0):
                        score.pAdd(score.total)
                        print("You banked:", score.total, "\nYour score is now:", score.player)
                    elif (choice == 1):
                        print("\nRolling Again...") 
    if (score.player < 100):
        choice = 0
        print ("\n*********Computers turn now**********")
    input("\nPress enter to continue...\n")
    return 2
# Computer's Turn - cpuMin/Max are its max turns max being 4
def computerRoll(score):
    global countOfRollsP2
    cpuMin, cpuMax = rollDie(Die(4))
    cpuMax, choice, count, score.total = 4, 1, 0, 0
   
    while (choice == 1 and (score.cpu + score.total < 100) and cpuMin < cpuMax):
        d1, d2 = rollDie(Die(6))
        print("*******Computer rolled", d1, "and", d2)
        score.runningTotal(d1 + d2)
        countOfRollsP2 += 1
        cpuMin += 1
        if (d1 == 1 and d2 == 1):
            print("Computer rolled snake eyes")
            print("-----------------Ultron----------- \nThat is some bullshit. Your human games are not smarter than ULTRON!!!\n")
            score.total = 0
            score.cpu = 0
            choice = 0
        elif (d1 == 1 or d2 == 1):
            print("\nComputer loses turn and round points")
            score.total = 0
            choice = 0
        else:
            if (score.player < 50 and cpuMin >= cpuMax):
                choice = random.randint(0,1)
            elif (score.player > 75 and score.cpu < 60 and cpuMin >= cpuMax):
                c1, c2 = rollDie(Die(10))
                count += 1
                if (c1 > 2):
                    choice = 1
                    print("----------------Ultron-----------\n------------------'You will not defeat me!!!'")
                else:
                    choice = 2
            elif (score.player > 50 and score.cpu < 30 and cpuMin >= cpuMax):
                c1, c2 = rollDie(Die(6))
                count += 1
                if (c1 > 2):
                    choice = 1
                    print("----------------Ultron------------\n----------------'I can\'t be defeated!!!'")
                else:
                    choice = 2
            else:
                choice = 0
    if (choice == 0):
        if (d1 != 1 and d2 != 1):
            print("------------- Ultron ----------")
            print("\n'I must bank'")
        else:
            print("------------- Ultron ----------")
            print("Ahhhhhhhhhhhhhhhh")
        score.cpuAdd(score.total)
        print("\nComputer banked", score.total, "\nComputer score is now", score.cpu)
        if (score.cpu < 100):
           print ("\n----------Player's turn now-----------\n")
        input("Press enter to continue...\n")
        return 1
# Could do a lot more with this but prints who won and how many rolls it took.
def summary(score):
    if (score.player > score.cpu):
        print("Player won with", score.player)
        print("It took the player", countOfRollsP1, "rolls to win")
    else:
        print("Computer won with", score.cpu)
        print("It took the computer", countOfRollsP2, "rolls to win")
# Sort after array creation and score swap.
def bubbleSort(array):
    loop1 = 0
    while (loop1 < (len(array) - 1)):                    
        if (int(array[loop1]) > int(array[loop1 + 1])):
            temp = array[loop1]
            array[loop1] = array[loop1 + 1]
            array[loop1 + 1] = temp
            loop1 = 0
        else:
            loop1 += 1
# To play again or not.
def play():
    game = "end"
    while (game == "end"):
        choice = input("\nWould you like to play again? (y/n)")
        if (choice == "y"):
            game = "play"
            return "y"
        elif (choice == "n"):
            return "n"
        elif (choice != "n" and choice != "y"):
            print("Invalid Response")
# I didn't plan on doing a main like this but it seemed like I could make the entire
#flow of code look better if I took out all the universal snippets that could stand
#as functions by themselves. Probably could've combined one or two.
def main():
    playAgain = "y"
    while (playAgain == "y"):
        global countOfRollsP1, countOfRollsP2
        countOfRollsP1, countOfRollsP2 = 0, 0
        sides = 6
        d1, d2 = rollDie(Die(sides))
        scoring = Score()
        print("\n------------ Hello, how about a game of pig? -----------\n------------ You don't have a choice anyway! -----------\n")
        input("...Press enter to continue...\n")
        first = firstRoll()
        lowScoresArray = checkFile()
        playGame(first, scoring)
        summary(scoring)
        checkScore(scoring, lowScoresArray)
        bubbleSort(lowScoresArray)
        writeFile(lowScoresArray)
        playAgain = play()

main()
