from math import *

#Input statements collecting our variables
name = input("Enter your first name: ")
age = int(input(name + "Enter your age: "))
cookieAverage = float(input("How many cookies do you eat per day? "))

name = "mud"
radius = 7
diameter = radius * 2
area = pi * radius ** 2

ridiculousNumber = cookieAverage / 7.777777

print("Your name is now ", end="")
print(name + ".")

print("The area of a circle with radius " + str(radius) + " is " + str(area))

print("A ridiculous number is {0:.3f} ".format(ridiculousNumber))

counter = 1 #Showing incremental expression in two different ways
print("Counter is " + str(counter))
counter += 1

print("Counter is " + str(counter))
counter = counter + 1

print("Counter is " + str(counter))
counter += 1
