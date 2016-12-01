# Code I copied for creating a die
import random 
class die(): 
    def __init__(self, sides): 
        self._sides = sides 
    def roll(self): 
        return random.randint(1, self._sides)
    def roll2(self):
        return 20

sides = int(input( "How many sides? " )) 
rolls = int(input( "How many rolls? " )) 

# make the die 
myDie = die(sides)
print(myDie.roll())
print(myDie.roll2())
# set array of counters, one per side, to zero 
totals = [0 for side in range(0, sides)]
#fileName = open("Totals List", "w+")
#fileName.write(str(totals))
#fileName.close() 

# roll the die and count the results 
for roll in range(0,rolls): 
    totals[myDie.roll() - 1] += 1
    fileName = open("Totals List", "w+")
    fileName.write(str(totals))
    fileName.close() 

# show the results 
for side in range(0,sides): 
    if totals[side]: 
        print (side+1, "was rolled", totals[side], "times")


# Creating a Dice Class
#import random

#class Die:
#    def __init__(self, number):
#        self.value = number
#    def __init__(self):
#        self.roll()
#    def roll(self):
#        self.value = random.randrange(1, 7)


#d1 = Die()
##d1 = d1 + 3
#print(d1.value)
#for count in range(20):
#    d1.roll()
#    print(d1.value)


# Method for clearing student elements

#def clear(aStudent):
#    aStudent.firstName = ""
#    aStudent.lastName = ""

#class Student:
#    firstName = input("Enter First Name ")
#    lastName = input("Enter Last Name ")
#    def clear(self):
#        self.firstName = ""
#        self.lastName = ""

#s1 = Student()
#print(s1.lastName + ", " + s1.firstName)
#s1.clear()
#print(s1.lastName, s1.firstName)
