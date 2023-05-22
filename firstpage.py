import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

window = tk.Tk()
window.geometry("700x700")
window.resizable(width=False, height=False)
window.tk.call("wm", "iconphoto", window._w, PhotoImage(file="Images/padlock.png"))
window.title("Password Saver")

frame = tk.Frame(width=50, height=50)
frame.pack()
frame.place(anchor='s', relx=0.5, rely=0.5)
img = ImageTk.PhotoImage(Image.open("Images/padlock-icon.jpg"))
label5 = tk.Label(frame, image=img)
label5.pack()

labe1 = tk.Label(text="Welcome to Group 2 Password Saver", font=("Arial", 17))
btn1 = tk.Button(text="Sign Up", width=10, bg="blue")
btn2 = tk.Button(text="Log in ", width=10, bg="blue")

labe1.pack()
btn1.place(x=200, y=400)
btn2.place(x=360, y=400)

window.mainloop()