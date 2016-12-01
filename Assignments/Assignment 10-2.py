# Daniel Jackson - Assignment 10
# For some reason I wanted to require the numbers entered be positive.

#Declaring my Variables.
number = 0
sumAll = 0 #In raptor for the assignment before this, I used "sum", but I should've known it was used already.
average = 0
count = 0
#Gathering my LCD with an input prompt so I can set their first values as the input.
number = float(input("Please Enter a Positive Decimal Number: "))
maximum = number
minimum = number

#Creating a loop using a sentinel as the end switch. The loop runs when the
#LCD is not equal to the sentinel, once matched, loop will end.
while(number != -1):
    if(number < 0):
        number = float(input("You are required to enter a postive number. \nPlease try again:"))
    if(number != -1): 
        count += 1
        sumAll += number
    if(number != -1 and number < minimum):
        minimum = number
    if(number != -1 and number > maximum):
        maximum = number
    #Right below this is the update to the LCD.
    number = float(input("\nPlease Enter Next Positive Decimal Number: "))
#This is the end of my above loop body.
if(sumAll == 0):
    print("No Data to Summarize")
else:
#print(" ") Omg I can't remember how to use /n.
    average = sumAll / count
    print("\nMinimum" , minimum)
    print("Maximum" , maximum)
    print("Average" , average)