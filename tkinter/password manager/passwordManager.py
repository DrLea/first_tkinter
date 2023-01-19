import tkinter as tk
from tkinter import messagebox
from random import sample, shuffle, randint
import pyperclip


#--------------KEYBOARD ---------------------#
# def next(a):
#     a.widget.tk_focusNext().focus()


#---------------RANDOM GENERATOR-------------#
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet += alphabet.upper()
nums = "0123456789"
signs = "!@#$%^&*+-=?~" + nums

def generate():
    a = randint(5,8)
    b = 10-a
    pa = sample(alphabet,a)
    pa+= sample(signs,b)
    shuffle(pa)
    password = "".join(pa)
    pyperclip.copy(password)
    passwordEntry.delete(0,tk.END)
    passwordEntry.insert(0,password)






#-------------- SAVING/READING ---------------#
emails = {}

def add():
    if len(webEntry.get())==0 or len(emailEntry.get())==0 or len(passwordEntry.get())==0:
        messagebox.showinfo(title="Warning", message="One or more fields are empty")
    else:
        ok = messagebox.askyesno(title="Confirmation", message=f"Website: {webEntry.get()}\nEmail/User: {emailEntry.get()}\nPassword: {passwordEntry.get()}\nSave it?")
        if ok:
            with open ("password.txt", "a") as file:
                file.write(f"Website: {webEntry.get()}\nEmail/User: {emailEntry.get()}\nPassword: {passwordEntry.get()}\n\n")
            webEntry.delete(0,tk.END)
            passwordEntry.delete(0,tk.END)

def commonMail():    
    with open ("password.txt") as file:
        for i in file.readlines():
            if "Email/User: " in i:
                try:
                    emails[i.split("Email/User: ")[1].split("\n")[0]]+=1
                except:
                    emails[i.split("Email/User: ")[1].split("\n")[0]]=1

        common = 0
        highest = 0

        for i in emails:
            if emails[i]>common:
                common = emails[i]
                highest = i

        emails.clear()
        return highest


#-------------- UI design --------------------#



window = tk.Tk()
window.config(padx = 50 ,pady=50)
window.title("Password manager")

# window.bind("<Enter>", next)

canvas = tk.Canvas(width=200,height=200)
try:
    img = tk.PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=img)
except:
    pass
canvas.grid(column=1, row=0)

webLabel = tk.Label(text="Website: ")
webLabel.grid(column=0,row=1)

emailLabel = tk.Label(text="Email/Username: ")
emailLabel.grid(column=0,row=2)

passwordLabel = tk.Label(text= "Password: ")
passwordLabel.grid(column=0,row=3)

webEntry = tk.Entry(width=52)
webEntry.focus()
webEntry.grid(column=1,row=1, columnspan=2)
emailEntry = tk.Entry(width=52)
try:
    if commonMail():
        emailEntry.insert(0,commonMail())
except:
    pass
emailEntry.grid(column=1,row=2, columnspan=2)
passwordEntry = tk.Entry(width=34)
passwordEntry.grid(column=1,row=3)

addButton = tk.Button(text="Add", width=44, command=add)
addButton.grid(column=1,row=4, columnspan=2)

generateButton = tk.Button(text="generate password", command= generate)
generateButton.grid(column=2, row=3)





window.mainloop()