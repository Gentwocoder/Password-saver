import _tkinter

import backend as bk
import random_pass_gen as rpg
import tkinter as tk
from tkinter import *


window = tk.Tk()
window.geometry("600x600")
window.resizable(width=False, height=False)
window.title("Password saver")


def saver():
    get_website = entry.get()
    get_password = entry2.get()
    bk.create_password(get_website, get_password)
    entry.delete(0, "end")
    entry2.delete(0, "end")
    entry.focus()


def random_pass():
    length = int(entry3.get())
    password = rpg.pass_gen(length)
    msg = "Your password is {}"
    msg_format = msg.format(password)
    text_box.insert(tk.END, msg_format)


def search():
    try:
        searcher = entry.get()
        searched = bk.view_any(searcher)
        entry2.insert(tk.END, searched)
        # entry2.delete(0, "end")
    except _tkinter.TclError:
        entry2.insert(tk.END, "Website not found!")


label = tk.Label(text="Website:", font=("Arial", 17, "bold"))
entry = tk.Entry(width=20)
label2 = tk.Label(text="Password:", font=("Arial", 17, "bold"))
entry2 = tk.Entry(width=20)
label3 = tk.Label(text="Length of Password:", font=("Arial", 17, "bold"))
entry3 = tk.Entry(width=5)
label4 = tk.Label()
btn = tk.Button(text="Generate Random Password", width=32, command=random_pass)
btn2 = tk.Button(text="Save", width=12, command=saver)
btn3 = tk.Button(text="Search", width=12, command=search)

text_box = Text(height=2, width=30)

label.place(x=150, y=150)
entry.place(x=270, y=155)
label2.place(x=150, y=200)
entry2.place(x=270, y=205)
label3.place(x=150, y=240)
entry3.place(x=390, y=245)
label4.pack()
text_box.pack()
btn.place(x=150, y=290)
btn2.place(x=150, y=330)
btn3.place(x=308, y=330)

window.mainloop()
