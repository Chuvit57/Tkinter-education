#!/usr/bin/python
# -*- coding: utf-8 -*

from tkinter import *

root = Tk()

root.geometry("900x1000+1000+300")
root['bg'] = 'lightblue'
root.title("Widgets")


# Расположение по центру
lab1 = Label(width=17, height=8, bg="yellow", text="1", font=16, fg="black")
lab2 = Label(width=17, height=8, bg="orange", text="2", font=16, fg="white")
lab3 = Label(width=17, height=8, bg="green", text="3", font=16, fg="white")
lab4 = Label(width=17, height=8, bg="blue", text="4", font=16, fg="white")

lab1.pack()
lab2.pack()
lab3.pack()
lab4.pack()





root.mainloop()