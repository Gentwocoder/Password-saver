import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

# window = tk.Tk()
# window.geometry("700x700")
# window.resizable(width=False, height=False)
# window.tk.call("wm", "iconphoto", window._w, PhotoImage(file="Images/padlock.png"))
# window.title("Password Saver")

# frame = tk.Frame(width=50, height=50)
# frame.pack()
# frame.place(anchor='s', relx=0.5, rely=0.5)
# img = ImageTk.PhotoImage(Image.open("Images/padlock-icon.jpg"))
# label5 = tk.Label(frame, image=img)
# label5.pack()

# labe1 = tk.Label(text="Welcome to Group 2 Password Saver", font=("Arial", 17))
# btn1 = tk.Button(text="Sign Up", width=10, bg="blue")
# btn2 = tk.Button(text="Log in ", width=10, bg="blue")

# labe1.pack()
# btn1.place(x=200, y=400)
# btn2.place(x=360, y=400)

# window.mainloop()

class Firstpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Welcome to Group 2 Password Saver", font=("Arial", 17))
        label1.place(x=170, y=50)

        frame = tk.Frame(self, width=50, height=50)
        frame.pack()
        frame.place(anchor='s', relx=0.5, rely=0.5)
        img = ImageTk.PhotoImage(Image.open("Images/padlock-icon.jpg"))
        label5 = tk.Label(frame, image=img)
        label5.pack()

        btn1 = tk.Button(self, text="Sign Up", bg="blue", font=("Arial", 12), relief=GROOVE, command=lambda: controller.show_frame(Signuppage))
        btn1.place(x=240, y=450)
        btn2 = tk.Button(self, text="Login", bg="blue", font=("Arial", 12), relief=GROOVE, command=lambda: controller.show_frame(Loginpage))
        btn2.place(x=380, y=450)

class Signuppage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        l1 = tk.Label(self, text="SIGNUP", font=("Arial Bold", 25))
        user = tk.Label(self, text="Username:", font=("Arial", 12))
        username = tk.Entry(self, bd=4)
        mail = tk.Label(self, text="Email:", font=("Arial", 12))
        email = tk.Entry(self, bd=4)
        pass_ = tk.Label(self, text="Password:", font=("Arial", 12))
        password = tk.Entry(self, bd=4)
        confirm_pass = tk.Label(self, text="Confirm Password:", font=("Arial", 12))
        confirm_password = tk.Entry(self, bd=4)
        btn1= tk.Button(self, text="Login", bg="blue", width=20, font=("Arial", 12), command=lambda: controller.show_frame(Loginpage))
        l1.place(x=300, y=50)
        user.place(x=200, y=150)
        username.place(x=400, y=150)
        mail.place(x=200, y=220)
        email.place(x=400, y=220)
        pass_.place(x=200, y=290)
        password.place(x=400, y=290)
        confirm_pass.place(x=200, y=360)
        confirm_password.place(x=400, y=360)
        btn3 = tk.Button(self, text="Signup", bg="blue", font=("Arial", 12))
        btn3.place(x=350, y=500)
        btn1.place(x=300, y=570)

class Loginpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        l1 = tk.Label(self, text="LOGIN", font=("Arial Bold", 25))
        user = tk.Label(self, text="Username:", font=("Arial", 12))
        username = tk.Entry(self, bd=5)
        pass_ = tk.Label(self, text="Password:", font=("Arial", 12))
        password = tk.Entry(self, bd=5)
        btn1= tk.Button(self, text="Signup", bg="blue", font=("Arial", 12), command=lambda: controller.show_frame(Signuppage))
        l1.place(x=300, y=50)
        user.place(x=200, y=200)
        username.place(x=400, y=200)
        pass_.place(x=200, y=300)
        password.place(x=400, y=300)
        btn4 = tk.Button(self, text="Login", bg="blue", font=("Arial", 12))
        btn4.place(x=350, y=400)
        btn1.place(x=450, y=400)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=700)
        window.grid_columnconfigure(0, minsize=700)

        self.frames = {}
        for i in (Firstpage, Signuppage, Loginpage):
            frame = i(window, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Firstpage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

app = Application()
app.mainloop()