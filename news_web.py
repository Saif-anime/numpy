from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('750x500')

img_li = [{'img':'banner_1.jpg', 'title':"Web Developer", 'para':"This is web developer post. we are talk about web developer"}, {'img':'banner_2.jpg', 'title':"Web Developer", 'para':"This is web developer post. we are talk about web developer"}]


n = 4  
n1 = 5
for x in img_li:
    img = ImageTk.PhotoImage(Image.open(x['img']).resize((150, 200)) )
    la = Label(root, image=img)
    la.place(x=n, y=n1)
    n+=160



root.mainloop()