import tkinter as tk

window = tk.Tk()
window.geometry("700x700")
window.resizable(width=False, height=False)
window.title("Password saver")

labe1 = tk.Label(text="Welcome to Group 2 Password Saver", font=("Arial", 17))
btn1 = tk.Button(text="Sign Up", width=10, bg="blue")
btn2 = tk.Button(text="Log in ", width=10, bg="blue")

labe1.pack()
btn1.pack()
btn2.pack()

window.mainloop()