import _tkinter
from tkinter import messagebox

# import pyperclip as pc
from PIL import ImageTk, Image
from backend import Backend
import random_pass_gen as rpg
import tkinter as tk


window = tk.Tk()
window.geometry("700x700")
window.resizable(width=False, height=False)
window.title("Password saver")
bk = Backend


def saver():
    get_website = entry.get().lower()
    get_username = entry4.get().lower()
    get_password = entry2.get()
    if len(get_website) != 0 and len(get_username) != 0 and len(get_password) != 0:
        answer = messagebox.askyesno(title="Confirm Details", message=f"""
        Please confirm details
        Username: {get_username}
        Password: {get_password}
        """)
        if answer:
            bk.create_password(get_website, get_username, get_password)
            messagebox.showinfo(title="Successful", message="Password added successfully")
            entry.delete(0, "end")
            entry4.delete(0, "end")
            entry2.delete(0, "end")
            entry.focus()
    else:
        messagebox.showerror(title="No blank spaces", message="No space should be left blank")
        entry.focus()


def random_pass():
    try:
        entry2.delete(0, "end")
        length = int(entry3.get())
        password = rpg.pass_gen(length)
        # pc.copy(password)
        entry2.insert(tk.END, password)
        entry3.delete(0, "end")
    except ValueError:
        messagebox.showwarning(title="Please input a length", message="Password length cannot be empty")


def search():
    try:
        searcher = entry.get().lower()
        searched = bk.view_any(searcher)
        entry2.delete(0, "end")
        entry.delete(0, "end")
        if searched is None:
            messagebox.showerror(title="not found", message="Password not found")
        else:
            messagebox.showinfo(title="Successful", message=f"Your {searcher} password is {searched}")
    except _tkinter.TclError:
        entry2.delete(0, "end")
        messagebox.showerror(title="Website not found", message="Website not found")


def remove():
    deleter = entry.get().lower()
    answer = messagebox.askokcancel(title="askokcancel", message="Are you sure you want to delete?")
    if answer:
        bk.delete(deleter)
        entry.delete(0, "end")
        messagebox.showinfo(title="Deleted", message="Deleted Successfully")


frame = tk.Frame(width=50, height=50)
frame.pack()
frame.place(anchor='s', relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open("Images/padlock-icon.jpg"))
label5 = tk.Label(frame, image=img)
label5.pack()


label = tk.Label(text="Website:", font=("Arial", 17, "bold"))
entry = tk.Entry(width=20)
label4 = tk.Label(text="Username:", font=("Arial", 17, "bold"))
entry4 = tk.Entry(width=20)
label2 = tk.Label(text="Password:", font=("Arial", 17, "bold"))
entry2 = tk.Entry(width=20)
label3 = tk.Label(text="Length of Password:", font=("Arial", 17, "bold"))
entry3 = tk.Entry(width=5)
btn = tk.Button(text="Generate Random Password", width=32, command=random_pass)
btn2 = tk.Button(text="Save", width=12, command=saver)
btn3 = tk.Button(text="Search", width=12, command=search)
btn4 = tk.Button(text="Delete", width=12, command=remove, bg="red")


label.place(x=160, y=360)
entry.place(x=280, y=365)
label4.place(x=160, y=400)
entry4.place(x=283, y=406)
label2.place(x=160, y=440)
entry2.place(x=280, y=445)
label3.place(x=160, y=480)
entry3.place(x=400, y=485)
btn.place(x=160, y=530)
btn2.place(x=160, y=570)
btn3.place(x=318, y=570)
btn4.place(x=240, y=620)

window.mainloop()
