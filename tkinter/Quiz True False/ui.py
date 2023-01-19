import tkinter as tk
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"
class Window:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.configure(bg=THEME_COLOR, padx=20,pady=20)

        self.canvas = tk.Canvas(width=300,height=200)
        self.question = self.canvas.create_text(150,100,text="Hello mzfucka", width=280, font=("Arial",16,"normal"))
        self.score = self.canvas.create_text(270,15,text="0", font=("Arial",20,"bold"))
        self.canvas.grid(column=0,row=0,columnspan=2)

        trueImg = tk.PhotoImage(file="true.png")
        self.trueButton = tk.Button(image=trueImg, command = self.true)
        self.trueButton.grid(column=0,row=1, pady=20)

        falseImg = tk.PhotoImage(file="false.png")
        self.falseButton = tk.Button(image=falseImg, command = self.false)
        self.falseButton.grid(column=1,row=1)

        self.canvas.itemconfig(self.question, text= self.quiz.next_question())

        self.window.mainloop()
    

    def next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question, text= self.quiz.next_question())
        else:
            try:
                self.canvas.itemconfig(self.question, text= f"Score: {self.quiz.score}/{self.quiz.question_number}")
            except:
                pass
            del self.canvas


    def answer(self, ans):
        if self.quiz.check_answer(ans):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.itemconfig(self.score, text=f"{self.quiz.score}/{self.quiz.question_number}")


    def false(self):
        self.answer("False")
        self.window.after(1000,self.next)
    
    def true(self):
        self.answer("True")
        self.window.after(1000,self.next)



