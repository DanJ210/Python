read():
    global hitByPosition
    inFile = open("battingaverage.txt","w")
    recordCount = 1
    position = inFile.readline()
    while(position != -1):
        recordCount += 2
        hit = inFile.readline()
        hitByPosition[position] += hit
        atBatByPosition[position] += 1
        position = inFile.readline()
    close(inFile)
    return recordCount

summary():
    print(pairCount + " pairs of data read.")
    print()
    for position in range(10):
        if(position != 0):
            print("The batting average for:")
            average = str(hitByPosition[position]) / atBatByPosition[position]
            print(" position " + position
                  + " is " + average)
    
main():
    read()
    summary(pairs)

hitByPosition = [10] * 10
atBatByPosition = [10] * 10

