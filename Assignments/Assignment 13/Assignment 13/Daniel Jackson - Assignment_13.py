# Daniel Jackson - Assignment 13


# This function I did after class in class, just a different way.
def numbers(userNumber):
    count = 1
    print("\nNumbers: ", end="")
    while(count <= userNumber):        
        if(count < userNumber):           
            print(str(count) +  ", " , end="")
            count += 1
        else:
            print(str(count))
            count += 1

def testAdd(enteredValue):
    count = 1
    result = 0
    theSum = 0
    while(count <= enteredValue):
        theSum += count
        count += 1
    return theSum

def product(enteredValue2):
    count = 1
    theProduct = 1
    while(count <= enteredValue2):
        theProduct *= count
        count += 1 
    return theProduct
# Wanted a nice format to print out
def result(theSum, theProduct):
    print("Sum: {0} \nProduct: {1}".format(theSum, theProduct))
 
# I did create a "main" cause all the cool kids were doing it :)
def main():
    runAgain = 0
    # As understood in the assignment, do the math after each valid number
    # input, continuously run until 0 is entered and the entire program
    # ends at that point.
    while (runAgain == False):
        inputNumber = 1
        while (inputNumber != 0):
            inputNumber = 1
            inputNumber = int(input("Please enter a number between 1 and 20\n "))
            if (inputNumber < 0 or inputNumber > 20):
                print("Please try again.")
                break
            elif(inputNumber != 0 ):
                # Where I call my functions.
                numbers(inputNumber)
                result(testAdd(inputNumber), product(inputNumber))
                print("")
            elif(inputNumber == 0):
                runAgain = True

main()