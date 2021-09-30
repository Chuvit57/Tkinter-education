#!/usr/bin/python
# -*- coding: utf-8 -*

from tkinter import *

vocabulary_worlds = []


def write_entry():
    w_eng = ent1.get()
    w_ru = ent2.get()
    w_eng_key = str(w_eng.capitalize())
    w_ru_value = str(w_ru.capitalize())
    wr = w_eng_key + " ***** " + w_ru_value
    voc = vocabulary_worlds.append(wr)
    print(wr, type(wr))
    print(vocabulary_worlds, type(vocabulary_worlds))
    with open('vocabulary.txt', 'a', encoding="utf-8") as file:
        file.write(wr)


def clear_entry():
    ent1.delete(0, END)
    ent2.delete(0, END)


root = Tk()

root.title("Vocabulary")
root.geometry("500x300+700+300")
root['bg'] = "lightblue"

# English world
lab1 = Label(text="Enter english world: ")
lab1.place(x=30, y=50)

# Enter En
ent1 = Entry(font=18, width=15)
ent1.place(x=30, y=80)

# Russian world

lab2 = Label(text="Enter russian world: ")
lab2.place(x=330, y=50)
# Enter Ru
ent2 = Entry(font=18, width=15)
ent2.place(x=330, y=80)

btn_write = Button(text="Write to dictionary", command=write_entry)
btn_write.place(x=120, y=130)

btn_clear = Button(text="Clear all", command=clear_entry)
btn_clear.place(x=300, y=130)

root.mainloop()
