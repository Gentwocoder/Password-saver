import tkinter as tk
import _tkinter
from tkinter import messagebox
from tkinter import *
from backend import Backend
from PIL import ImageTk, Image
import random_pass_gen as rpg

bk = Backend

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
        l2 = tk.Label(self, text="Already Have an Account?", font=("Arial", 13))
        user = tk.Label(self, text="Username:", font=("Arial", 12))
        username = tk.Entry(self, bd=4)
        mail = tk.Label(self, text="Email:", font=("Arial", 12))
        email = tk.Entry(self, bd=4)
        pass_ = tk.Label(self, text="Password:", font=("Arial", 12))
        password = tk.Entry(self, bd=4, show="*")
        confirm_pass = tk.Label(self, text="Confirm Password:", font=("Arial", 12))
        confirm_password = tk.Entry(self, bd=4, show="*")
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
        btn3.place(x=490, y=410)
        l2.place(x=300, y=540)
        btn1.place(x=300, y=570)

class Loginpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        l1 = tk.Label(self, text="LOGIN", font=("Arial Bold", 25))
        l2 = tk.Label(self, text="Don't have an Account?", font=("Arial", 13))
        user = tk.Label(self, text="Username:", font=("Arial", 12))
        username = tk.Entry(self, bd=5)
        pass_ = tk.Label(self, text="Password:", font=("Arial", 12))
        password = tk.Entry(self, bd=5, show="*")
        btn1= tk.Button(self, text="Signup", bg="blue", width=20, font=("Arial", 12), command=lambda: controller.show_frame(Signuppage))
        l1.place(x=300, y=50)
        user.place(x=200, y=200)
        username.place(x=400, y=200)
        pass_.place(x=200, y=300)
        password.place(x=400, y=300)
        btn4 = tk.Button(self, text="Login", bg="blue", font=("Arial", 12), command=lambda: controller.show_frame(Passwordsaver))
        btn4.place(x=500, y=360)
        l2.place(x=290, y=470)
        btn1.place(x=290, y=500)

class Passwordsaver(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        frame = tk.Frame(self, width=50, height=50)
        frame.pack()
        frame.place(anchor='s', relx=0.5, rely=0.5)
        img = ImageTk.PhotoImage(Image.open("Images/padlock-icon.jpg"))
        label5 = tk.Label(frame, image=img)
        label5.pack()

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
                    bk.create_password(self, get_website, get_username, get_password)
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
                searched = bk.view_any(self, searcher)
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
                bk.delete(self, deleter)
                entry.delete(0, "end")
                messagebox.showinfo(title="Deleted", message="Deleted Successfully")


        label = tk.Label(self, text="Website:", font=("Arial", 17, "bold"))
        entry = tk.Entry(self, width=20)
        label4 = tk.Label(self, text="Username:", font=("Arial", 17, "bold"))
        entry4 = tk.Entry(self, width=20)
        label2 = tk.Label(self, text="Password:", font=("Arial", 17, "bold"))
        entry2 = tk.Entry(self, width=20)
        label3 = tk.Label(self, text="Length of Password:", font=("Arial", 17, "bold"))
        entry3 = tk.Entry(self, width=5)
        btn = tk.Button(self, text="Generate Random Password", width=32, command=random_pass)
        btn2 = tk.Button(self, text="Save", width=12, command=saver)
        btn3 = tk.Button(self, text="Search", width=12, command=search)
        btn4 = tk.Button(self, text="Delete", width=12, bg="red", command=remove)


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

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=700)
        window.grid_columnconfigure(0, minsize=700)

        self.frames = {}
        for i in (Firstpage, Signuppage, Loginpage, Passwordsaver):
            frame = i(window, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Firstpage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()

app = Application()
app.mainloop()