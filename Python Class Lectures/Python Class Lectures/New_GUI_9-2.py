from tkinter import *
master = Tk()

w = Canvas(master, width=800, height=600,)
w.pack()

w.create_rectangle(5,5,600,30, fill="orange", outline="green")
w.create_oval(5,5,600,30)

w.create_oval(300,200,500,400)


w.create_polygon(0,600,800,0,400,200, fill="purple", width=10, outline="blue")

superNova = PhotoImage(file="supernova.gif")
w.create_image(100,300, image=superNova)
