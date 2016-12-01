from random import *
from tkinter import *

root = Tk()
wide = randrange(600, 801)
tall = randrange(400, 601)
w = Canvas(root, width=wide, height=tall)
w.pack()

w.create_rectangle(20,20,wide-20,tall-20, fill="#FF0000")
