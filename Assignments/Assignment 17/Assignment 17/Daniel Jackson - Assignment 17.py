# Daniel Jackson - Assignment 17

def read():
    inFile = open("battingaverage.txt","r")
    recordCount = 0
    position = int(inFile.readline())
    while(position != -1):
        recordCount += 1
        hit = int(inFile.readline())
        hitByPosition[position] += hit
        atBatByPosition[position] += 1
        position = int(inFile.readline())
    inFile.close()
    return recordCount

def summary(pairCount):
    print(str(pairCount) + " pairs of data read.")
    print()
    for position in range(10):
        if(position != 0):
            print("The batting average for:")
            average = str(hitByPosition[position] / atBatByPosition[position])
            print(" position " + int(position)
                  + " is " + str(average))
            position += 1
        else:
            position += 2
    
def main():
    global hitByPosition
    global atBatByPosition
    hitByPosition = [0] * 10
    atBatByPosition = [0] * 10
    pairs = read()
    summary(pairs)
    

main()



