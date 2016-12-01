#number1 = int(input("Please enter your first number. "))
#number2 = int(input("Please enter your second number. "))

##number1 = 4
##number2 = 2


#def subtract(number1, number2):
#    answer = number1 - number2
#    return answer

#def main():
#    print("The difference is: " , subtract(number1, number2))



def swap(value1, value2):
    temp = value1
    value1 = value2
    value2 = temp
    #print(value1, value2)
    return value1, value2

def main():
    number3 = 5
    number4 = 10
    number3, number4 = (swap(number3, number4))
    print("This was the second value: " , number3)
    print("This was the first value: " , number4)

main()