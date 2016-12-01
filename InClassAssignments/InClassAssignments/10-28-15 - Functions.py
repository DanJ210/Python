def displayMessage():
    print("Hello from COP1000")

def displayMessage(theMessage):
    print(theMessage)

def add(addend1, addend2):
    total = addend1 + addend2
    return total

def divide(divisor, dividend):
    if (dividend != 0):
        quotient = divisor / dividend
        return True, quotient
    else:
        return False, 0

def main():

    #displayMessage("Wednesday")
    #displayMessage("Friday")

    #result = add
    #print(add(5,4))

    success, myAnswer = divide(9,5)
    if(success == True):
        print(myAnswer)
    
    else:
        displayMessage("Division by 0")

main()