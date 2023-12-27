from tkinter import *

root = Tk()
root.geometry("200x300")
num1 = IntVar()
num2 = IntVar()

t1 = Label(text="enter the value 1")
t1.pack()
n1 =Entry(root, textvariable=num1)
n1.pack()
name = "mohini"

t2 = Label(text="enter the value 2")
t2.pack()
n2 =Entry(root, textvariable=num2) 
n2.pack()

def add():
    newnum = num1.get()
    newnum2 = num2.get()
    sum_num = newnum2+newnum
    print(sum_num)
    root.geometry(f"{newnum}x{newnum2}")#size change automatically when we change value in both boxes
    s = Label(text=f'sum of two number is = {sum_num}')
    s.pack()

btn = Button(text="submit",command=add)
btn.pack()

root.mainloop()