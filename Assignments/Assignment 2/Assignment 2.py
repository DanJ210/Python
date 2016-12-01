from tkinter import *
master = Tk()

Canvas = Canvas(master, width=600, height=600)
Canvas.pack()

Canvas.create_rectangle(150,150,450,500, outline="red") #Drawing the house structure

Canvas.create_rectangle(350,200,400,250, fill="yellow") #Creating Windows
Canvas.create_rectangle(300,200,350,250, fill="yellow")
Canvas.create_rectangle(300,250,350,300, fill="yellow")
Canvas.create_rectangle(350,250,400,300, fill="yellow")

Canvas.create_rectangle(200,350,300,500, outline="orange") #Creating door
Canvas.create_text(225,400, text="10", fill="red") #Door number

Canvas.create_oval(295,400,285,415, fill="blue") #Door Knob

Canvas.create_line(75,150,500,150,300,100,75,150, fill="red") #Creating Roof

Canvas.create_line(200,500,160,600, fill="orange") #Creating Sidewalk
Canvas.create_line(300,500,325,600, fill="orange")


Canvas.create_rectangle(320,525,480,570, fill="brown") #Drawing flower bed first

bushFlowers1 = PhotoImage(file="bushFlowers1.gif") #Creating Flower Garden
Canvas.create_image(350,550, image=bushFlowers1)   #Inserting images

bushFlowers = PhotoImage(file="bushFlowers.gif")
Canvas.create_image(400,550, image=bushFlowers)

bushFlowers2 = PhotoImage(file="bushflowers2.gif")
Canvas.create_image(450,550, image=bushFlowers2)
