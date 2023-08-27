from tkinter import *

root = Tk()

root.geometry("500x500")
num1 = IntVar()
num2 = IntVar()

t1 = Label(text="Enter the value 1")
t1.pack()
n1 = Entry(root, textvariable=num1)
n1.pack()
# pack Grid place
name = "saif"

t2 = Label(text="Enter the value 2")
t2.pack()
n2 = Entry(root,  textvariable=num2)
n2.pack()

def add():
    newnum = num1.get()
    newnum2 = num2.get()
    sum_num = newnum2+newnum
    print(sum_num)
    s = Label(text=f'two number sum is = {sum_num}')
    s.pack()

btn = Button(text="submit", command=add)
btn.pack()
root.mainloop()