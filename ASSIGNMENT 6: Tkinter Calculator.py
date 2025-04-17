from tkinter import *

#gui interraction
window = Tk()

#adding inputs
window.title("Calculator")
window.geometry("460x450")
window.config(bg="orange")

e = Entry(window, width=400, bg='white', font=("Arial", 30, "bold"), fg='black')
e.place(x=0, y=0)

#button
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

b=Button(window, text="1", width=5, height=3, bg='white', fg='black', command = lambda:click(1))
b.place(x=10, y=60)
b=Button(window, text="2", width=5, height=3, bg='white', fg='black' , command = lambda:click(2))
b.place(x=100, y=60)
b=Button(window, text="3", width=5, height=3, bg='white', fg='black' , command = lambda:click(3))
b.place(x=190, y=60)
b=Button(window, text="4", width=5, height=3, bg='white', fg='black' , command = lambda:click(4))
b.place(x=280, y=60)
b=Button(window, text="5", width=5, height=3, bg='white', fg='black', command = lambda:click(5))
b.place(x=370, y=60)        
b=Button(window, text="6", width=5, height=3, bg='white', fg='black', command = lambda:click(6))
b.place(x=10, y=150)    
b=Button(window, text="7", width=5, height=3, bg='white', fg='black', command = lambda:click(7))
b.place(x=100, y=150)   
b=Button(window, text="8", width=5, height=3, bg='white', fg='black',   command = lambda:click(8))
b.place(x=190, y=150)
b=Button(window, text="9", width=5, height=3, bg='white', fg='black', command = lambda:click(9))
b.place(x=280, y=150)
b=Button(window, text="0", width=5, height=3, bg='white', fg='black', command = lambda:click(0))
b.place(x=370, y=150)

def clear():
    e.delete(0, END)
b=Button(window, text="C", width=5, height=3, bg='white', fg='black', command = lambda: e.delete(0, END))
b.place(x=10, y=240)

#operators
def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, i + int(n2))
    elif math == "subtraction":
        e.insert(0, i - int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))
    elif math == "division":
        e.insert(0, i / int(n2))
    
b=Button(window, text="=", width=5, height=3, bg='white', fg='black', command = equal)
b.place(x=100, y=240)

def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i= int(n1)
    e.delete(0, END)
b=Button(window, text="+", width=5, height=3, bg='white', fg='black' ,command = add)
b.place(x=190, y=240)

def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i= int(n1)
    e.delete(0, END)
b=Button(window, text="-", width=5, height=3, bg='white', fg='black', command = sub)
b.place(x=280, y=240)

def mult():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i= int(n1)
    e.delete(0, END)
b=Button(window, text="*", width=5, height=3, bg='white', fg='black', command = mult)
b.place(x=370, y=240)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i= int(n1)
    e.delete(0, END)
b=Button(window, text="/", width=5, height=3, bg='white', fg='black', command = div)
b.place(x=10, y=330)




#main loop
window.mainloop()