#!/usr/bin/python
# -*- coding: utf-8 -*

from tkinter import *

root = Tk()

# root.geometry("900x1000+1000+300")
# root['bg'] = 'lightblue'
# root.title("method pack()")

# Расположение во фреймах
# f_top = Frame(root)
# f_bot = Frame(root)

# Расположение фрейм с подписью
# f_top = LabelFrame(text="Верх", padx=10, pady=10) # внешние отступы
# f_bot = LabelFrame(text="Низ")
#
#
# lab1 = Label(f_top, width=17, height=8, bg="yellow", text="1", font=16, fg="black")
# lab2 = Label(f_top, width=17, height=8, bg="orange", text="2", font=16, fg="white")
# lab3 = Label(f_bot, width=17, height=8, bg="green", text="3", font=16, fg="white")
# lab4 = Label(f_bot, width=17, height=8, bg="blue", text="4", font=16, fg="white")

# Расположение по центру
# lab1.pack()
# lab2.pack()
# lab3.pack()
# lab4.pack()

# Расположение снизу
# lab1.pack(side=BOTTOM)
# lab2.pack(side=BOTTOM)
# lab3.pack(side=BOTTOM)
# lab4.pack(side=BOTTOM)

# Расположение слева по центру

# lab1.pack(side=LEFT)
# lab2.pack(side=LEFT)
# lab3.pack(side=LEFT)
# lab4.pack(side=LEFT)

# Расположение во фреймах
# f_top.pack()
# f_bot.pack(ipadx=10, ipady=10) # Внутренние отступы
# lab1.pack(side=LEFT)
# lab2.pack(side=LEFT)
# lab3.pack(side=LEFT)
# lab4.pack(side=LEFT)

# Свойства: fill(заполнение[значения: BOTH, x, y]) и expend(расширение[значения: 0, 1])
root.geometry("700x400+800+400")

# lab1 = Label(text="This is a label", width=30, height=10, bg="lightgreen")
# lab1.pack()
# lab1.pack(expand=1) # По середине
# lab1.pack(expand=1, fill=Y) # По середине, заполнение по у
# lab1.pack(expand=1, fill=BOTH) # Полностью весь лист залит

#Свойство anchor-якорь(N-север, S-юг, W-запад, E-восток)
lab1 = Label(text="This is a label", width=30, height=10, bg="lightgreen")

lab1.pack(expand=1, anchor=SE)

root.mainloop()
