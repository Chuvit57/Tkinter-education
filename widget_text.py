#!/usr/bin/python
# -*- coding: utf-8 -*

from tkinter import *

# widget Text()
"""
Text - это многострочное текстовое поле.
Основные методы: get(), insert(), delete().
В случае многострочного надо указывать два-номера строки и номер символа в этой строке(номер столбца)
"""


# root = Tk()

# Размеры поля по умолчанию

# text = Text()
# print(text['width'], text['height'])
# text.pack()


# Example 1
# text = Text(width=125, height=5, bg="darkgreen", fg='white', wrap=WORD)
# text.pack(side=LEFT)
# scroll = Scrollbar(command=text.yview)
# scroll.pack(side=LEFT, fill=Y)
# text.config(yscrollcommand=scroll.set)

# Example 2

# def insert_text():
#     s = " "
#     text.insert(1.0, s)
#
#
# def get_text():
#     s = text.get(1.0, END)
#     label['text'] = s
#
#
# def delete_text():
#     text.delete(1.0, END)
#     label['text'] = ' '
#
#
#
# root = Tk()
# text = Text(width=25, height=5)
# text.pack()
#
# frame = Frame()
# frame.pack()
# Button(frame, text="Вставить", command=insert_text).pack(side=LEFT)
# Button(frame, text="Взять", command=get_text).pack(side=LEFT)
# Button(frame, text="Удалить", command=delete_text).pack(side=LEFT)
#
# label = Label()
# label.pack()

# Example 3
# Тэги придают оформление: tag_add and tag_config
root = Tk()



root.mainloop()
