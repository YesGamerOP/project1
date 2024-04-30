from tkinter import*

calculator=Tk()
#calculator.geometry("320x175")
calculator.title("Python Calculator")

ex=""
equation=StringVar()
def press(num):
    global ex
    ex=ex+str(num)
    equation.set(ex)

def clear():
    global ex
    ex=""
    equation.set(ex)

def result():
    global ex
    answer=str(eval(ex)) #eval=evaluate
    equation.set(answer)

def delete():
    global ex
    ex=ex[0:-1]
    equation.set(ex)

u=Entry(calculator,width=40,bd=5,textvariable=equation)
u.place(x=32,y=0)
b21=Button(calculator,text="⌫",width=3,command=delete)
b21.place(x=285,y=0)

b17=Button(calculator,text="(",width=10,command=lambda:press("("))
b17.place(x=0,y=40)
b18=Button(calculator,text=")",width=10,command=lambda:press(")"))
b18.place(x=80,y=40)
b19=Button(calculator,text="x²",width=10,command=lambda:press("**"))
b19.place(x=160,y=40)
b20=Button(calculator,text="AC",width=10,command=clear)
b20.place(x=240,y=40)
    
b1=Button(calculator,text="7",width=10,command=lambda:press(7),background="gray",foreground="white",activebackground="gray",activeforeground="white")
b1.place(x=0,y=67)
b2=Button(calculator,text="8",width=10,command=lambda:press(8),background="gray",foreground="white",activebackground="gray",activeforeground="white")
b2.place(x=80,y=67)
b3=Button(calculator,text="9",width=10,command=lambda:press(9),background="gray",foreground="white",activebackground="gray",activeforeground="white")
b3.place(x=160,y=67)
b4=Button(calculator,text="÷",width=10,command=lambda:press("/"))
b4.place(x=240,y=67)

b5=Button(calculator,text="4",width=10,command=lambda:press(4),background="gray",foreground="white",activebackground="gray",activeforeground="white")
b5.place(x=0,y=94)
b6=Button(calculator,text="5",width=10,command=lambda:press(5),background="gray",foreground="white",activebackground="gray",activeforeground="white")
b6.place(x=80,y=94)
b7=Button(calculator,text="6",width=10,command=lambda:press(6),background="gray",foreground="white",activebackground="gray",activeforeground="white")
b7.place(x=160,y=94)
b8=Button(calculator,text="*",width=10,command=lambda:press("*"))
b8.place(x=240,y=94)

b9=Button(calculator,text="1",width=10,command=lambda:press(1),background="gray",foreground="white",activebackground="gray",activeforeground="white")
b9.place(x=0,y=121)
b10=Button(calculator,text="2",width=10,command=lambda:press(2),background="gray",foreground="white",activebackground="gray",activeforeground="white")
b10.place(x=80,y=121)
b11=Button(calculator,text="3",width=10,command=lambda:press(3),background="gray",foreground="white",activebackground="gray",activeforeground="white")
b11.place(x=160,y=121)
b12=Button(calculator,text="-",width=10,command=lambda:press("-"))
b12.place(x=240,y=121)

b13=Button(calculator,text="0",width=10,command=lambda:press(0),background="gray",foreground="white",activebackground="gray",activeforeground="white")
b13.place(x=0,y=148)
b14=Button(calculator,text=".",width=10,command=lambda:press("."),background="gray",foreground="white",activebackground="gray",activeforeground="white")
b14.place(x=80,y=148)
b15=Button(calculator,text="=",width=10,command=result,background="cyan",activebackground="cyan")
b15.place(x=160,y=148)
b16=Button(calculator,text="+",width=10,command=lambda:press("+"))
b16.place(x=240,y=148)
calculator.mainloop()
