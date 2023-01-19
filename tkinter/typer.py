from tkinter import *

root = Tk()
root['bg'] = '#585266'
root.title("Type faster bitch")
root.geometry("900x700")

file = open("file.txt")
a = file.read()
x = 0

def move():
    global x
    x = x - 0.1
    title.place(rely = 0.05, relx = x)
def movelef():
    global x
    x = x + 0.1
    title.place(rely = 0.05, relx = x)
def check():
    b = cin.get()
    i = 0
    t= True
    while(i<len(b)-1):
        i=i+1
        if a[i]!=b[i]:
            title = Label( root, text = "Error: "+ str(i), bg = 'red' , font = 48)
            title.place(rely = 0.15, relx = 0.15)
            t=False
            break
    if t==True:
        title = Label( root, text = "Correct ", bg = 'green' , font = 48)
        title.place(rely = 0.15, relx = 0.15)
    


#text
title = Label( root, text = a, bg = 'gray' , font = 48)
title.place(rely = 0.05, relx = 0.05)

#button
btn = Button( root, text = "->" ,  bg = '#ed5f8a', command = move)
btn.place(relx = 0.9, rely = 0.45)

#button
btn = Button( root, text = "<-" ,  bg = '#ed5f8a', command = movelef)
btn.place(relx = 0.8, rely = 0.45)

#button
btn = Button( root, text = "<>" ,  bg = '#96e065', command = check)
btn.place(relx = 0.85, rely = 0.45)

#entry
cin = Entry(root, bg = '#ded3d6', font = 60)
cin.place(relx = 0.05, rely = 0.3, relwidth = 0.9, relheight = 0.1)

        


#end repeater
root.mainloop()
