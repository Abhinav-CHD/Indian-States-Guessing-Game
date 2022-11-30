import turtle
import pandas
import tkinter as tk
from tkinter import ttk
try:
    file = pandas.read_csv("./Game Building files/28_States.csv")
except:
    file = pandas.read_csv("backup.csv")
screen = turtle.Screen()
picture = "./map.gif"
screen.addshape(picture)
turtle.shape(picture)
screen.title("Indian States Guessing Game")
turtle = turtle.Turtle()
turtle.penup()
turtle.hideturtle()

all_states = file["state"].tolist()

correct_guess = 0
correct_answer = []
while correct_guess < 28:
    
    user_input = screen.textinput(title=f"Score {correct_guess}/28", prompt="Enter the next state")
    if user_input == None:
        break
    user_input = user_input.title()

    if user_input in all_states and user_input not in correct_answer:
        x_pos = int(file[file.state == user_input]["x"])
        y_pos = int(file[file.state == user_input]["y"])
        turtle.goto(x_pos, y_pos)
        turtle.write(arg=f"{user_input}", align="center", font=("Arial", 8, "normal"))
        correct_guess += 1
        correct_answer.append(user_input)
screen.bye()

not_able_to_guess = [answer for answer in all_states if answer not in correct_answer]

df = pandas.DataFrame(not_able_to_guess, columns=["These are all the states that you were not able to guess"])

df.to_csv("Incomplete_states.csv")

title_message = f"In total you were able to guess {correct_guess}/28 states"

not_able_to_guess_string = "States that you were not able to guess\n"
for state in not_able_to_guess:
    not_able_to_guess_string+= f"{state}\n"
if len(not_able_to_guess) ==0:
    not_able_to_guess_string="Yay! You Guessed all the states"

def popupmsg():
    popup = tk.Tk()
    popup.minsize(400,100)
    popup.wm_title(title_message)
    label = ttk.Label(popup, text=not_able_to_guess_string, font=("Helvetica", 10))
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

popupmsg()