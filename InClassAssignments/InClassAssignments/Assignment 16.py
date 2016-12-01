from random import *
lotteryNumber = []

def main():
    index = 0
    lotteryResults = open("LotteryResults.txt", "w")
    while (index <= 8):
        randomNumber = randrange(1, 9)
        lotteryNumber.append(randomNumber)
        index += 1
        
    lotteryResults.close
        
#def duplicateCheck(lottoNums):
 #   for number in range(len(lottoNums)):
   #     if (lottoNums[number] == lottoNums[number + 1]):

main()
print(lotteryNumber)
    


