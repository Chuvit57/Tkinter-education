#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


# def str_to_sort_list(event):
#     s = ent.get()
#     s = s.split()
#     s.sort()
#     lab['text'] = ' '.join(s)


# root = Tk()
# root.geometry("800x500+1000+300")
# root.title("Tkinter начало")

# ent = Entry(root, width=20)
# btn = Button(root, text="Преобразовать")
# lab = Label(root, width=20, bg='#000', fg='white')
#
# btn.bind('<Button-1>', str_to_sort_list)
# ent.pack()
# btn.pack()
# lab.pack()

# Этот же пример через ООП

# class Block:
#     def __init__(self, master, func):
#         self.ent = Entry(master, width=20)
#         self.btn = Button(master, text="Преобразовать")
#         self.lab = Label(master, width=20, bg='#000', fg='white')
#         self.btn['command'] = getattr(self, func)
#         self.ent.pack()
#         self.btn.pack()
#         self.lab.pack()
#
#     def str_to_sort(self):
#         s = self.ent.get()
#         s = s.split()
#         s.sort()
#         self.lab['text'] = ' '.join(s)
#
#     def str_reverse(self):
#         s = self.ent.get()
#         s = s.split()
#         s.reverse()
#         self.lab['text'] = ' '.join(s)
#
#
# root = Tk()
#
# root.geometry("800x500+1000+300")
# root.title("Tkinter начало")
#
# first_block = Block(root, 'str_to_sort')
# second_block = Block(root, 'str_reverse')
#
# root.mainloop()
