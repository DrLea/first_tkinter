import tkinter as tk
from playsound import playsound


# ---------------------------- CONSTANTS ------------------------------- #
SOUND = "D:\\my projects\\py projects\\100 day of code\\tkinter\\pomodoro\\sound.wav"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    global done, reps, save, saved
    window.after_cancel(counter)
    canvas.itemconfig(timer, text="00:00")
    timerLabel.config(text="TIMER", fg=GREEN)
    done = 0
    reps = 0
    save = 0
    saved = 0
    checkMark.config(text="✔"*done)
    startButton.config(text="S\nt\na\nr\nt", command=start)




# ---------------------------- TIMER MECHANISM ------------------------------- # 
reps = 0
counter = None
saved = 0

def start():
    global done, reps, saved
    startButton.config(text="S\nt\no\np", command=stop)
    reps+=1
    if reps % 8 ==0:
        done+=1
        checkMark.config(text="✔"*done)
        timerLabel.config(text="BREAK", fg=RED)
        arg = LONG_BREAK_MIN*60
        if saved:
            arg = saved
            saved = 0
        countDown(arg)
        done=0
    elif reps % 2==0:
        done+=1
        checkMark.config(text="✔"*done)
        timerLabel.config(text="BREAK", fg=PINK)
        arg = SHORT_BREAK_MIN*60
        if saved:
            arg = saved
            saved = 0
        countDown(arg)
    else:
        arg = WORK_MIN*60
        if saved:
            arg = saved
            saved = 0
        countDown(arg)
        timerLabel.config(text="WORK", fg=GREEN)


def stop():
    global reps,saved
    saved = save
    window.after_cancel(counter)
    timerLabel.config(text="Pause", fg=GREEN)
    startButton.config(text="S\nt\na\nr\nt", command=start)
    if reps !=0:
        reps-=1

        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
save = 0
done = 0

def countDown(count):
    global counter,save
    canvas.itemconfig(timer, text="%02d:%02d"%(count//60,count%60))
    if count > 0:
        save = count
        counter = window.after(1000,countDown,count-1)
    else:
        checkMark.config(text="✔"*done)
        playsound(SOUND)
        start()



# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=50,pady=20, bg=YELLOW)
window.minsize(516,450)
window.iconbitmap("D:\\my projects\\py projects\\100 day of code\\tkinter\\pomodoro\\tomico.ico")

canvas = tk.Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
img = tk.PhotoImage(file = "D:\\my projects\\py projects\\100 day of code\\tkinter\\pomodoro\\tomato.png")
canvas.create_image(100,112, image=img)
timer = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1,row=1, padx=20)

timerLabel = tk.Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timerLabel.grid(column=1,row=0)

checkMark =tk.Label(text="✔"*done, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkMark.place(x=150,y=350)

startButton = tk.Button(text="S\nt\na\nr\nt", width=5, height=10, fg=RED, bg=GREEN, font=(FONT_NAME, 20, "bold"), highlightthickness=0, command= start)
startButton.grid(column=0,row=1)

resetButton = tk.Button(text="R\ne\ns\ne\nt", width=5, height=10, fg=GREEN, bg=RED, font=(FONT_NAME, 20, "bold"), highlightthickness=0, command=reset)
resetButton.grid(column=2,row=1)


window.mainloop()