number1 = int(input("Enter first number "))
number2 = int(input("Enter second number "))
number3 = int(input("Enter third number "))

if (number1 < number2 and number1 < number3):
    print(number1)
    if (number2 < number3):
        print(number2)
        print(number3)
    else:
        print(number3)
        print(number2)
else:
    if(number2 < number1 and number2 < number3):
        print(number2)
        if(number3 < number1):
            print(number3)
            print(number1)
        else:
            print(number1)
            print(number2)
    else:
        print(number3)
        if(number1 < number2):
            print(number1)
            print(number2)
        else:
            print(number2)
            print(number1)
