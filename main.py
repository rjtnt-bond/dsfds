from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from datetime import *
from math import *
import pymysql
import time
from tkinter import messagebox
from math import*

class Login_window:

    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN WINDOW")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        self.root.maxsize(1350, 700)
        self.root.minsize(1350, 700)
        root.wm_iconbitmap('login.ico')

        # Background colors
        left_lb1 = Label(self.root, bg="#08A3D2", bd=0)
        left_lb1.place(x=0, y=0, relheight=1, width=600)

        self.right_lb1 = ImageTk.PhotoImage(file="bglg.jpg")
        bg = Label(self.root, image=self.right_lb1).place(x=250, y=0, relwidth=1, relheight=1)
        # right_lb1 = Label(self.root, bg="#031F3C", bd=0)
        # right_lb1.place(x=600, y=0, relheight=1, relwidth=1)

        # Frames=========
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_frame,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
        email=Label(login_frame, text="EMAIL", font=("times new roman", 17, "bold"), bg="white",
                      fg="gray").place(x=250, y=150)

        self.txt_email = Entry(login_frame, font=("times new roman", 15),
                      bg="lightgray")
        self.txt_email.place(x=250, y=180,width=350, height=35)

        pass_= Label(login_frame, text="PASSWORD", font=("times new roman", 17, "bold"), bg="white",
                      fg="gray").place(x=250, y=250)
        self.txt_pass_ = Entry(login_frame, font=("times new roman", 15),
                          bg="lightgray")
        self.txt_pass_.place(x=250, y=280, width=350, height=35)

        btn_reg=Button(login_frame,text="Register new Account",command=self.register_window,font=("times new roman",14),bg="white",bd=0,fg="#B00857",cursor="hand2").place(x=250, y=320)


        btn_login = Button(login_frame, text="LOGIN",command=self.login, font=("times new roman", 14,"bold"), bg="#B00857",cursor="hand2",
                         fg="white").place(x=250, y=360)


        # clock
        self.lb1 = Label(self.root,text="DEAR CAMELIA",font=("Arial Black",25,"bold"),fg="Red",compound=BOTTOM, bg="#081923", bd=0)
        self.lb1.place(x=90, y=120, height=450, width=350)
        self.working()

    def register_window(self):
        self.root.destroy()
        import registar



    def login(self):

        if self.txt_email.get()=="" or self.txt_pass_.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)

        elif self.txt_email.get()=="tasmimtaraz98@gmail.com" and self.txt_pass_.get()=="123456":
            self.root.destroy()
            import dettails

        elif self.txt_email.get() == "bondhonbondhon342@gmail.com" and self.txt_pass_.get() == "12345":
            self.root.destroy()
            import bond

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="employ2")
                cur=con.cursor()
                cur.execute("select * from emp where email=%s and password=%s",(self.txt_email.get(),self.txt_pass_.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error", "Invalid USERNAME & PASSWORD", parent=self.root)

                else:
                    messagebox.showerror("Welcome", "It's client not a Volunteer or moderator", parent=self.root)

                con.close()
            except Exception as es:
                messagebox.showinfo("Error",f"Error Due to:{str(es)}",parent=self.root)


    def clock_image(self, hr, min, sec):
        clock = Image.new("RGB", (400, 400), (255, 255, 255))
        draw = ImageDraw.Draw(clock)

        # clock Image
        bg = Image.open("clock.png")
        bg = bg.resize((300, 300), Image.ANTIALIAS)
        clock.paste(bg, (50, 50))

        # Formula To Rotate the AntiClock
        # angle_in_radians = angle_in_degrees * math.pi/180
        # line_length = 100
        # center_x = 250
        # center_y =250
        # end_x = center_x + line_length * math.cos(angle_in_radians)
        # end_y = center_y - line_length * math.sin(angle_in_radians)

        # Hour Image line #
        #     x1,y1,x2,y2
        origin = 200, 200
        draw.line((origin, 200 + 50 * sin(radians(hr)), 200 - 50 * cos(radians(hr))), fill="black", width=4)
        # Min Image line#
        draw.line((origin, 200 + 80 * sin(radians(min)), 200 - 80 * cos(radians(min))), fill="green", width=3)
        # Sec Image line#
        draw.line((origin, 200 + 100 * sin(radians(sec)), 200 - 100 * cos(radians(sec))), fill="blue", width=4)

        draw.ellipse((195, 195, 210, 210), fill="black")

        clock.save("clock_new.png")

    def working(self):
        h = datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr = (h / 12) * 360
        min = (m / 60) * 360
        sec = (s / 60) * 360
        self.clock_image(hr, min, sec)
        self.img = ImageTk.PhotoImage(file="clock_new.png")
        self.lb1.config(image=self.img)
        self.lb1.after(200, self.working)



root = Tk()
obj = Login_window(root)
root.mainloop()
