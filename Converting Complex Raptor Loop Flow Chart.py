number1 = int(input("Enter number 1: "))
number2 = 25
number3 = 8

while(number1 < 0):
    number1 = int(input("Enter number 1: "))
while(number1 < 10):
    print("Number 1:" , number1)
    number2 = number2 - 10 + number1
    while(number2 < 35):
        print("number 2: " , number2)
        if(number2 % 2 == 0):
            print("Skipping Number 2")
        else:
            number3 = number2 - 17
            while(number3 > 5):
                print("Number 3: " , number3)
                number3 = number3 - 1
        number2 = number2 + 1
    number1 = number1 + 2
    
