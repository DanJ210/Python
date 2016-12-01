# Daniel Jackson - Assignment 16

from random import *
lotteryNumbers = []

# Calling below function writes to file as if to print the results.
def printTicket(arrayFile):  
    file = "LotteryResults.txt"
    lotteryResults = open(file, "w+")
    lotteryResults.write(str(arrayFile))
    # I had trouble with files, closing it would give an error when I used ().
    lotteryResults.close
 
# Really didn't need a function for this.   
def randomLottery():
    index = 0
    userChoice = 6
    #userChoice = int(input("How many random numbers would you like? "))
    while (index < userChoice):
        randomNumber = randrange(1, userChoice)
        lotteryNumbers.append(randomNumber)
        index += 1

def duplicateSwap(lottoNums):
    # Print statement below only confirmed length
    #print(len(lottoNums))
    index = 0
    for element in range(len(lottoNums)):
        # Remove comment from print below to help see how program works.
        #print(element)
        loop1 = 0
        numberCheck = 0
        while(loop1 < (len(lottoNums) - 1)):
            if (element == numberCheck):
                    numberCheck += 1
            elif(numberCheck < len(lottoNums)):
                if (lottoNums[element] == lottoNums[numberCheck]):
                    # Remove comment from print below.
                    #print("duplicate")
                    lottoNums.remove(lottoNums[element])
                    lottoNums.insert(element,randrange(1,10))
                    # Remove comment from print statement below to help see how program works.
                    #print(lottoNums)
                    loop1 = 0
                    numberCheck = 0
                else:
                    numberCheck += 1
                    loop1 += 1
            else:
                numberCheck = 0
                loop1 += 1 

def bubbleSort(lottoNums):
    loop1 = 0
    while (loop1 < (len(lottoNums) - 1)):                    
        if (lottoNums[loop1] > lottoNums[loop1 + 1]):
            temp = lottoNums[loop1]
            lottoNums[loop1] = lottoNums[loop1 + 1]
            lottoNums[loop1 + 1] = temp
            loop1 = 0
        else:
            loop1 += 1

def main():
    randomLottery()
    duplicateSwap(lotteryNumbers)
    bubbleSort(lotteryNumbers)
    duplicateSwap(lotteryNumbers)

main()
print(lotteryNumbers)
    


