import tkinter as tk


operation = "tomi"


#*0.62
def convert():
    num = float(a.get())
    if operation == "tomi":
        b.config(text = "%1.2f" %(num*0.62))
    elif operation == "tokm":
        b.config(text = "%1.2f" %(num/0.62))


def swa():
    global operation, swap
    if operation == "tomi":
        operation = "tokm"
        swap["text"] = "mi to km"
    else:
        operation = "tomi"
        swap["text"] = "km to mi"

window = tk.Tk()
window.title("Distance Converter")
window.minsize(width=300,height=200)
window.config(padx=100, pady=50)

swap = tk.Button(text="km to mi",command=swa)
swap.grid(column=1,row=1)

a = tk.Entry(width=5)
a.focus()
a.grid(column=0,row=0)

b = tk.Label(text="  0  ")
b.grid(column=2,row=0)



convert = tk.Button(text="--convert-->", command=convert)
convert.grid(column=1,row=0)


window.mainloop()