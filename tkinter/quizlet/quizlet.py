import tkinter as tk
import pandas as pd
from random import choice


BACKGROUND_COLOR = "#B1DDC6"
FROMLANG = "french"

#__________DATA IMPORT____________#

try:
    df = pd.read_csv(f"{FROMLANG}_remainder.csv")
except:
    df = pd.read_csv(f"{FROMLANG}_words.csv")
cards = df.to_dict(orient="records")
fromlang = list(df)[0]
tolang = list(df)[1]
# french = df["French"].tolist()
# english = df["English"].tolist()
# cards = {f:e for (f,e) in zip(french,english)}




#__________CLICK LOGIC____________#
card = {}
a = 0
first = True

def nextcard():
    global card, a
    window.after_cancel(a)
    try:
        card = choice(cards)
    except:
        window.quit()
    cardCanvas.itemconfig(lang, text=fromlang, fill="black")
    cardCanvas.itemconfig(word, text=card[fromlang], fill="black")
    cardCanvas.itemconfig(back, image=frontImg)
    a = window.after(3000, flipcard)

    
def flipcard():
    global a, first
    window.after_cancel(a)
    if first:
        cardCanvas.itemconfig(lang, text=tolang, fill="white")
        cardCanvas.itemconfig(word, text=card[tolang], fill="white")
        cardCanvas.itemconfig(back, image=backImg)
        first = False
    else:
        cardCanvas.itemconfig(lang, text=fromlang, fill="black")
        cardCanvas.itemconfig(word, text=card[fromlang], fill="black")
        cardCanvas.itemconfig(back, image=frontImg)
        first = True
    
    a = window.after(3000, flipcard)


def know():
    cards.remove(card)
    print(len(cards))
    wordsLeft = pd.DataFrame(cards)
    wordsLeft.to_csv(f"{fromlang}_remainder.csv", index=False)
    nextcard()




#_____________UI DESIGN____________#

window = tk.Tk()
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50,pady=50)
a = window.after(3000, flipcard)

cardCanvas = tk.Canvas()
frontImg = tk.PhotoImage(file="card_front.png")
backImg = tk.PhotoImage(file="card_back.png")
cardCanvas.config(width=800,height=526 ,bg=BACKGROUND_COLOR, highlightthickness=0)
back = cardCanvas.create_image(400,263,image= frontImg)
lang = cardCanvas.create_text(400,150,text="Title",font=("Ariel", 40, "italic"))
word = cardCanvas.create_text(400,263,text = "Word" ,font=("Ariel", 60, "bold"))
cardCanvas.grid(column=0,row=0, columnspan=2)

yesImg = tk.PhotoImage(file="right.png")
yesButton = tk.Button(image=yesImg, highlightthickness=0, command=know)
yesButton.grid(column=1,row=1)

noImg = tk.PhotoImage(file="wrong.png")
noButton = tk.Button(image=noImg, highlightthickness=0, command=nextcard)
noButton.grid(column=0,row=1)

nextcard()


window.mainloop()