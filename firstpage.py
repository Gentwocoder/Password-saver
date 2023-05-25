import tkinter as tk
import _tkinter
import sqlite3
from tkinter import messagebox
from tkinter import *
from backend import Backend, User
from PIL import ImageTk, Image
import random_pass_gen as rpg
import bcrypt

bk = Backend
us = User
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

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

        btn1 = tk.Button(self, text="Sign Up", bg="light blue", font=("Arial", 12), relief=GROOVE, command=lambda: controller.show_frame(Signuppage), cursor="hand2")
        btn1.place(x=240, y=450)
        btn2 = tk.Button(self, text="Login", bg="light blue", font=("Arial", 12), relief=GROOVE, command=lambda: controller.show_frame(Loginpage), cursor="hand2")
        btn2.place(x=380, y=450)

class Signuppage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def register():
            get_username = username.get()
            get_email = email.get().lower()
            get_password = password.get()
            if len(get_username) != 0 and len(get_email) != 0 and len(get_password) != 0:              
                cursor.execute("SELECT username FROM users WHERE username=?", (get_username,))
                if cursor.fetchone() is not None:
                    messagebox.showerror(title="Error", message="Username already exists.")
                else:
                    encoded_password = get_password.encode("utf-8")
                    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
                    us.create_user(self, get_username, get_email, hashed_password)
                    username.delete(0, END)
                    email.delete(0, END)
                    password.delete(0, END)
                    username.focus()
                    messagebox.showinfo(title="Successful", message="User Created Successfully!!")
                    controller.show_frame(Loginpage)
            else:
                messagebox.showerror(title="Error", message="No blank spaces!!")
        l1 = tk.Label(self, text="SIGNUP", font=("Arial Bold", 25))
        l2 = tk.Label(self, text="Already Have an Account?", font=("Arial", 13))
        user = tk.Label(self, text="Username:", font=("Arial", 12))
        username = tk.Entry(self, bd=4)
        mail = tk.Label(self, text="Email:", font=("Arial", 12))
        email = tk.Entry(self, bd=4)
        pass_ = tk.Label(self, text="Password:", font=("Arial", 12))
        password = tk.Entry(self, bd=4, show="*")
        btn1= tk.Button(self, text="Login", bg="light blue", width=20, font=("Arial", 12), command=lambda: controller.show_frame(Loginpage), cursor="hand2")
        l1.place(x=300, y=50)
        user.place(x=200, y=150)
        username.place(x=400, y=150)
        mail.place(x=200, y=220)
        email.place(x=400, y=220)
        pass_.place(x=200, y=290)
        password.place(x=400, y=290)
        btn3 = tk.Button(self, text="Signup", bg="light blue", font=("Arial", 12), command=register, cursor="hand2")
        btn3.place(x=490, y=410)
        l2.place(x=300, y=540)
        btn1.place(x=300, y=570)

class Loginpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def signin():
            get_username = username.get()
            get_password = password.get()
            checker = us.check_user(self, get_username)
            if len(get_password) != 0 and len(get_username) != 0:
                if checker is None:
                    messagebox.showerror(title="Not found", message="User not found!!")
                    username.delete(0, END)
                    password.delete(0, END)
                    username.focus()
                else:
                    # us.check_user(self, get_username)
                    controller.show_frame(Passwordsaver)
                    messagebox.showinfo(title="Successful", message="Login successful!!")
            else:
                messagebox.showerror(title="Error", message="No space should be left blank!!")
        l1 = tk.Label(self, text="LOGIN", font=("Arial Bold", 25))
        l2 = tk.Label(self, text="Don't have an Account?", font=("Arial", 13))
        user = tk.Label(self, text="Username:", font=("Arial", 12))
        username = tk.Entry(self, bd=5)
        pass_ = tk.Label(self, text="Password:", font=("Arial", 12))
        password = tk.Entry(self, bd=5, show="*")
        btn1= tk.Button(self, text="Signup", bg="light blue", width=20, font=("Arial", 12), command=lambda: controller.show_frame(Signuppage), cursor="hand2")
        l1.place(x=300, y=50)
        user.place(x=200, y=200)
        username.place(x=400, y=200)
        pass_.place(x=200, y=300)
        password.place(x=400, y=300)
        btn4 = tk.Button(self, text="Login", bg="light blue", font=("Arial", 12), command=signin, cursor="hand2")
        btn4.place(x=500, y=360)
        l2.place(x=290, y=470)
        btn1.place(x=290, y=500)

class Passwordsaver(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

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
                    messagebox.showerror(title="Not Found", message="Password not found")
                else:
                    messagebox.showinfo(title="Successful", message=f"Your {searcher} username and password is {searched}")
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

        def all():
            all_passwords = bk.view_all(self)
            messagebox.showinfo(title="All passwords", message=f"{all_passwords}")

        def change():
            get_website = entry.get().lower()
            get_username = entry4.get().lower()
            get_password = entry2.get()
            if len(get_website) != 0 and len(get_username) != 0 and len(get_password) != 0:
                answer = messagebox.askyesno(title="Confirm Details", message=f"""
                Please confirm new username and password
                Username: {get_username}
                Password: {get_password}
                """)
                if answer:
                    bk.update(self, get_username, get_password, get_website)
                    messagebox.showinfo(title="Successful", message="Password Updated Successfully!!")
                    entry.delete(0, "end")
                    entry4.delete(0, "end")
                    entry2.delete(0, "end")
                    entry.focus()
            elif get_website is None:
                messagebox.showerror(title="Not Found", message="Website does not exist!!")


        label = tk.Label(self, text="Website:", font=("Arial", 17, "bold"))
        entry = tk.Entry(self, width=20)
        label4 = tk.Label(self, text="Username:", font=("Arial", 17, "bold"))
        entry4 = tk.Entry(self, width=20)
        label2 = tk.Label(self, text="Password:", font=("Arial", 17, "bold"))
        entry2 = tk.Entry(self, width=20)
        label3 = tk.Label(self, text="Length of Password:", font=("Arial", 17, "bold"))
        entry3 = tk.Entry(self, width=5)
        btn = tk.Button(self, text="Generate Random Password", width=32, bg="light blue", command=random_pass, cursor="hand2")
        btn2 = tk.Button(self, text="Save", width=12, bg="light blue", command=saver, cursor="hand2")
        btn3 = tk.Button(self, text="Search", width=12, bg="light blue", command=search, cursor="hand2")
        btn4 = tk.Button(self, text="Delete", width=12, bg="red", command=remove, cursor="hand2")
        btn5 = tk.Button(self, text="View all", width=12, bg="light blue", command=all, cursor="hand2")
        btn6 = tk.Button(self, text="Update", width=12, bg="light blue", command=change, cursor="hand2")


        label.place(x=160, y=220)
        entry.place(x=280, y=222)
        label4.place(x=160, y=270)
        entry4.place(x=283, y=272)
        label2.place(x=160, y=320)
        entry2.place(x=280, y=322)
        label3.place(x=160, y=370)
        entry3.place(x=400, y=372)
        btn.place(x=160, y=430)
        btn2.place(x=160, y=490)
        btn3.place(x=318, y=490)
        btn5.place(x=160, y=540)
        btn6.place(x=318, y=540)
        btn4.place(x=240, y=600)

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
app.maxsize(700, 700)
app.title("Password Saver")
app.mainloop()