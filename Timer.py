#coding for a timer which show current time with seconds,mintues and hours
from tkinter import *
import tkinter.font as Font
from tkinter.ttk import *
from time import *

root=Tk()
root.title("Timer")

def increase_font_size():
    font.config(size=font.actual()['size'] + 2)

def decrease_font_size():
    font.config(size=max(8, font.actual()['size'] - 2)) 
def func():
    s=strftime("Day : %a \nDate : %d / %b / %Y  \nTime : %H : %M : %S %p")
    label.config(text=s)
    label.after(1000,func)

font = Font.Font(family="Times", size=40)
label = Label(root, text="Resizable Text", font=font,background="black",foreground="green") 
label.pack()

increase_button = Button(root, text="Increase Font Size", command=increase_font_size) 
increase_button.pack()

decrease_button = Button(root, text="Decrease Font Size", command=decrease_font_size)
decrease_button.pack()
func()
root.mainloop()