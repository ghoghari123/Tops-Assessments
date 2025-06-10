from tkinter import *

screen = Tk()
screen.geometry("700x700")
screen['bg'] = "#808080"
screen.title("Hotel Management")

lb = Label(screen,text="Welcome",fg="#000000",font=("Arieal", 30),bg="#808080")
lb.place(x = 250, y = 15)
btn1 = Button(screen,text="[ 1 ] CHECK INN",width=40,height=2)
btn1.place(x = 180, y = 100)
btn2 = Button(screen,text="[ 2 ] SHOW GUEST LIST",width=40,height=2)
btn2.place(x = 180, y = 150)
btn3 = Button(screen,text="[ 3 ] CHECK OUT",width=40,height=2)
btn3.place(x = 180, y = 200)
btn4 = Button(screen,text="[ 4 ] GET INFO OF ANY GUEST",width=40,height=2)
btn4.place(x = 180, y = 250)
btn5 = Button(screen,text="[ 5 ] EXIT",width=40,height=2)
btn5.place(x = 180, y = 300)

screen.mainloop()
