import turtle
import pandas
import tkinter as tk
from tkinter import ttk


with open("./states.txt") as file:
    states_list = file.read().splitlines()


mylist = []
final = []


def pos(x, y):
    print(x, y)
    mylist.append((x, y))
    screen.exitonclick()
 
def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=("Helvetica", 10))
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
for i in range(len(states_list)):
    msg = f"Click Where {states_list[i]} is Located"
    popupmsg(msg)

    screen = turtle.Screen()
    screen.title("Click the screen Twice to make input")
    picture = "../map.gif"
    screen.bgpic(picture)
    screen.update()
    # screen.addshape(picture)
    # turtle.shape(picture)
    screen.onscreenclick(pos)
    
    screen.mainloop()
    
    
    print(states_list[i])

    final.append({"state": states_list[i], "x": mylist[i][0], "y": mylist[i][1]})

df = pandas.DataFrame(final)
df.to_csv("28_States.csv")
