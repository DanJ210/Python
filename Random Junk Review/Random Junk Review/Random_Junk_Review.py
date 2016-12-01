from tkinter import *
from random import *

master = Tk()


#print("{0:X}".format(11))

#print("{0:x}".format(255))

#print("R".zfill(5))

#print("".zfill(5))

red = "{:X}".format(randrange(256)).zfill(2)
green = "{:X}".format(randrange(256)).zfill(2)
blue = "{:X}".format(randrange(256)).zfill(2)
myRandColor = "#" + red + green + blue

w = Canvas(master, width=800, height=600, bg=myRandColor)
w.pack()
