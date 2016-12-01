def writeFile(name, weight, price):
    file = open("metallist.txt","w")
    loop = 0
    #while (loop < 4):
    file.write(name), ("")
    file.write(weight), ("\n")
    file.write(price), ("\n")
    file.close()

def main():
    metalName = input("Please enter commodity")
    weight = input("Please enter the weight")
    price = input("Please neter price you paid")
    writeFile(metalName, weight, price)

main()

#def checkFile(array):
#    scoreFile = open("lowscore.txt", "r")
#    for line in range(len(array)):
#        lastLine = (scoreFile.readline())
#        array[line] = lastLine.strip()
#        #print(lastLine)
#    scoreFile.close()

#def writeFile(array):
#    file = open("lowscore.txt", "w")
#    for line in range(len(array)):
#        file.write(str(array[line]) + "\n")
#    file.close()
