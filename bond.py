from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
from math import *
import pymysql
import time
from tkinter import messagebox
from math import*

class details:

    def login(self):
        self.root.destroy()
        import main

    def client(self):
        self.root.destroy()
        import client


    def __init__(self, root):
        self.root = root
        self.root.title("Volunteer")
        self.root.geometry("400x500+80+0")
        self.root.maxsize(400, 500)
        self.root.minsize(400, 500)
        root.wm_iconbitmap('v.ico')
        self.root.config(bg="white")

        self.left = ImageTk.PhotoImage(file="bond.jpg")
        left = Label(self.root, image=self.left).place(x=5, y=5, width=200, height=201)

        f_name = Label(self.root, text="Name: Bondhon", font=("times new roman", 18, 'bold'),bg="white").place(
            x=0, y=210)

        Age = Label(self.root, text="Age: 22", font=("times new roman", 18, 'bold'),bg="white").place(
            x=0, y=240)

        Volunteer= Label(self.root, text="Volunteer: Dear Camelia ", font=("times new roman", 18, 'bold'), bg="white").place(
            x=0, y=270)

        Join_date = Label(self.root, text="Joining_date: 21-09-20 ", font=("times new roman", 18, 'bold'),
                          bg="white").place(
            x=0, y=300)

        Home_district = Label(self.root, text="Home district: Rangpur", font=("times new roman", 18, 'bold'),
                          bg="white").place(
            x=0, y=350)

        Current_city = Label(self.root, text="Current city: Rangpur", font=("times new roman", 18, 'bold'),
                          bg="white").place(
            x=0, y=380)

        btn_login = Button(self.root, text="BACK", command=self.login, font=("times new roman", 14, "bold"),
                           bg="#B00857", cursor="hand2",
                           fg="white").place(x=0, y=430)


        btn_login = Button(self.root, text="CLINT", command=self.client, font=("times new roman", 14, "bold"),
                           bg="#B00857", cursor="hand2",
                           fg="white").place(x=210, y=430)



root=Tk()
object=details(root)
root.mainloop()
