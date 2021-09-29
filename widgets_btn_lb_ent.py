#!/usr/bin/python
# -*- coding: utf-8 -*

from tkinter import *
from datetime import datetime as dt

# Button

# def change():
#     btn['text'] = 'Изменено'
#     btn['bg'] = '#000'
#     btn['activebackground'] = '#555555'
#     btn['fg'] = '#ffffff'
#     btn['activeforeground'] = '#ffffff'

# def take():
#     lab3['text'] = "Выдано"


root = Tk()

root.geometry("700x500+1000+300")
root['bg'] = 'lightblue'
root.title("Widgets")

# btn = Button(text='Изменить', width=15, height=5, command=change)
# btn.pack()


# Label - метка
# lab1 = Label(text='Машинное обучение', font="Arial 32")
# lab2 = Label(text='Распознавание образов', font=("Comic Sans MS", 24, "bold"))
# lab1.config(bd=20, bg='#ffaaaa')
# lab2.config(bd=20, bg='#aaffff')

# Label без переменной
# Label(text="Пункт выдачи").pack()
# Button(text="Взять", command=take).pack()
#
# lab3 = Label(width=10, height=1)
# lab3.pack()


# lab1.pack()
# lab2.pack()

# Entry - однострочное текстовое поле

"""
Текстовые поля предназначены для ввода информации пользователем,
но нередко используются и для вывода, если предпологается что текст из них будет
скопирован.
Из текстового поля можно взять текст за это отвечает: метод - get()
В текстовое поле можно вставить текст методом: insert()
Удалить текст методом: delete()
"""


# def insert_time():
#     t = dt.now().time()
#     ent.insert(END, t.strftime('%H:%M:%S '))
#
#
# ent = Entry(width=50)
# ent['justify'] = 'center'
# btn = Button(text="Время", command=insert_time)
# ent.pack()
# btn.pack()

root.mainloop()
