#getThree
#    isPrime (1,2,3,5,7,11,13,17,19)
#calcSum
#calcAverage
#displayResult - print the sum and average

number1 = int(input("Enter first number"))
number2 = int(input("Enter Second Number"))
number3 = int(input("Enter Third Number"))

def isPrime():

    if number1 != (1,2,3,4,7,11,13,17,19):
        print("Sorry you need prime numbers")
    if number2 != (1,2,3,4,7,11,13,17,19):
        print("Sorry you need prime numbers")
    if number3 != (1,2,3,4,7,11,13,17,19):
        print("Sorry you need prime numbers")
    return

isPrime(number1)

def calcAverage():
    theAverage = (number1 + number2 + number3)/3
    return theAverage


def calcSum():
    theSum = (number1 + number2 + number3)
    return theSum
print(calcSum())
print(calcAverage())

#def getThree(isPrime):
#    if number1 =
    