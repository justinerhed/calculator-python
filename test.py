from tkinter import *
top = Tk()

def calculate_score():
    num1 = int(E1.get())
    num2 = int(E2.get())
    total_score = num1 + num2
    E3.insert(0, str(total_score))
def calculate_score2():
    num1 = int(E1.get())
    num2 = int(E2.get())
    total_score2 = num1 - num2
    E3.insert(0, str(total_score2))

def calculate_score3():
    num1 = int(E1.get())
    num2 = int(E2.get())
    total_score3 = num1 * num2
    E3.insert(0, str(total_score3))

def calculate_score4():
    num1 = int(E1.get())
    num2 = int(E2.get())
    total_score4 = num1 / num2
    E3.insert(0, str(total_score4))

def clear_text():
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
    

L1 = Label(top, text="Number 1: ")
L1.place(x=10,y=10)
E1 = Entry(top, bd =5)
E1.place(x=60,y=10)

L2=Label(top,text="Number 2: ")
L2.place(x=10,y=50)
E2=Entry(top,bd=5)
E2.place(x=60,y=50)



L3=Label(top,text="Total: ")
L3.place(x=10,y=150)
E3=Entry(top,bd=5)
E3.place(x=60,y=150)

B = Button(top, text ="+", command = calculate_score)
B.place(x=60, y=100)

B = Button(top, text ="-", command = calculate_score2)
B.place(x=85, y=100)

B = Button(top, text ="x", command = calculate_score3)
B.place(x=40, y=100)

B = Button(top, text ="/", command = calculate_score4)
B.place(x=20, y=100)

B = Button(top, text ="Clear All", command = clear_text )
B.place(x=110, y=100)
top.geometry("300x300")
top.mainloop()
