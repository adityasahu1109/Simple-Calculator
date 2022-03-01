"""
This program is made by Aditya Sahu
This is program is just a demonstration of tkinter module and some basic python 
mathematic operations.

This is just a basic calculator


"""
from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)


    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        
        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text )
        screen.update()


root =Tk()
root.geometry("450x560")
root.title("Simple Calculator By Aditya Sahu")

# root.wm_iconbitmap("1.ico")                      # to add icon

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar = scvalue, font = "lucida 40 bold")
screen.pack(fill = X, ipadx =8,pady = 10, padx = 10)

# 9 8 7
f = Frame(root, bg = "light green")


b = Button(f , text ="9", padx = 6, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

b = Button(f , text ="8", padx = 6, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

b = Button(f , text ="7", padx = 6, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

f.pack()
# 6 5 4
f = Frame(root, bg = "light green")


b = Button(f , text ="6", padx = 6, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

b = Button(f , text ="5", padx = 6, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

b = Button(f , text ="4", padx = 6, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

f.pack()

# 3 2 1
f = Frame(root, bg = "light green")


b = Button(f , text ="3", padx = 6, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

b = Button(f , text ="2", padx = 6, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

b = Button(f , text ="1", padx = 6, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

f.pack()

f = Frame(root, bg = "light green")


b = Button(f , text ="0", padx = 8, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

b = Button(f , text ="-", padx = 8, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

b = Button(f , text ="*", padx = 8, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

f.pack()
f = Frame(root, bg = "light green")


b = Button(f , text ="/", padx = 5, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

b = Button(f , text ="%", padx = 5, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

b = Button(f , text ="=", padx = 7, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

f.pack()

f = Frame(root, bg = "light green")


b = Button(f , text ="C", padx = 3, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

b = Button(f , text =".", padx = 3, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

b = Button(f , text ="00", padx = 3, pady = 3, font = "lucida 24 bold")
b.pack(side = LEFT, padx = 18, pady = 5)
b.bind("<Button-1>", click )

f.pack()






root.mainloop()
