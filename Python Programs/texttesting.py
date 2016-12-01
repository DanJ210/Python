from tkinter import *
master = Tk()

w = Canvas(master, width=800, height=600,)
w.pack()


w.create_text(1,1,text="Testing Text", anchor=NW)
