from tkinter import*
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
from PIL import  Image,ImageTk #pip install pillow
import pymysql #pip install pymysql
import  datetime
import time

class Register:

    def __init__(self,root):
       self.root = root
       self.root.title("Registration Window")
       self.root.geometry("1350x700+0+0")
       self.root.maxsize(1350, 700)
       self.root.minsize(1350, 700)
       self.root.config(bg="white")
       root.wm_iconbitmap('home-page.ico')

       self.bg = ImageTk.PhotoImage(file="photo.jpg")
       bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

       self.left = ImageTk.PhotoImage(file="prio.jpg")
       left = Label(self.root,image=self.left).place(x=80, y=100, width=400, height=700)

       frame1  = Frame(self.root,bg="white")
       frame1.place(x=480,y=100,width=700,height=700)
       title = Label(frame1,text='MODERATOR/VOLUNTEER - INFORMATION',font=("times new roman",20,'bold'),bg="white",fg="green").place(x=50,y=30)


       your_name = Label(frame1,text="YOUR NAME",font=("times new roman",15,'bold'),bg="white",fg='gray').place(x=0,y=100,width=230)

       self.your_name=Entry(frame1,font=("times new roman",15),bg="lightgray")
       self.your_name.place(x=50,y=130,width=230)

       your_sector = Label(frame1, text="MODERATOR/VOLUNTEER", font=("times new roman", 15,'bold'), bg="white", fg='gray').place(
          x=370, y=100)

       self.your_sector = Entry(frame1, font=("times new roman", 15), bg="lightgray")
       self.your_sector.place(x=370, y=130, width=230)


       date = Label(frame1, text="DATE", font=("times new roman", 15, 'bold'), bg="white", fg='gray').place(
          x=50, y=170)

       self.txt_date_entry = Entry(frame1, font=("times new roman", 15), bg="lightgray")
       self.txt_date_entry.place(x=50, y=200, width=230)

       self.Email_entry = Entry(frame1, font=("times new roman", 12), bg="lightgray")
       self.Email_entry.place(x=370, y=200, width=230,height=25)

       Email_name = Label(frame1, text="EMAIL", font=("times new roman", 15, 'bold'), bg="white", fg='gray').place(
          x=370, y=170)


       self.gender = ttk.Combobox(frame1, font=("times new roman", 12),state="readonly",justify=CENTER)

       self.gender ['values']=("Select","Female","Male","Others")

       self.gender .place(x=50, y=260, width=230)
       self.gender .current(0)
       gender = Label(frame1, text="GENDER", font=("times new roman", 15, 'bold'), bg="white", fg='gray').place(
          x=50, y=230)


       self.pass_word_entry  = Entry(frame1, font=("times new roman", 15), bg="lightgray")
       self.pass_word_entry.place(x=370, y=260, width=230)

       pass_word  = Label(frame1, text="PASSWORD", font=("times new roman", 15, 'bold'), bg="white",
                             fg='gray').place(
          x=370, y=230)

       your_detailes = Label(frame1, text="YOUR DETAILS", font=("times new roman", 15, 'bold'), bg="white", fg='gray').place(
          x=50, y=295)

       self.txt_detailes = Text(frame1, font=("times new roman", 14), bg="lightgray")
       self.txt_detailes.place(x=50, y=330, width=550, height=100)


       cpass_word = Label(frame1, text="CONFIRM PASSWORD ", font=("times new roman", 15, 'bold'), bg="white", fg='gray').place(
          x=50, y=430)

       self.cpass_word = Entry(frame1, font=("times new roman", 15), bg="lightgray")
       self.cpass_word.place(x=50, y=460, width=230)

       self.var_chk=IntVar()
       chk=Checkbutton(frame1,text="Agree",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman", 15)).place(x=50,y=500)

       self.btn_image=ImageTk.PhotoImage(file="regis.png")
       bn=Button(frame1,image=self.btn_image,bd=0,cursor="hand2",command= self.register_data).place(x=180,y=540,width=300, height=30)

       self.sign = ImageTk.PhotoImage(file="sign.png")
       bn = Button(self.root, image=self.sign, bd=0, cursor="hand2", command=self.main_window).place(x=210, y=470)

    def clint(self):
        client_Name = self.your_name.get()
        answer =self.txt_detailes .get('1.0',END)
        gender = self.gender.get()
        Data = 'Name: ' + client_Name + ' Problem: ' + answer + '  Gender: ' + gender
        named_tuple = time.localtime()  # get struct_time
        time_string = time.strftime(" %m/%d/%Y, %H:%M:%S ", named_tuple)



        # write our data in txt file also save date and time
        with open('record.txt', 'a') as f:
            f.write(
                f'{Data}' + f' Data entry time: {time_string}' + '\n')

    def main_window(self):
        self.root.destroy()
        import main

    def clear(self):
        self.your_name.delete(0,END)
        self.your_sector.delete(0,END)
        self.txt_date_entry .delete(0,END)
        self.Email_entry.delete(0,END)
        self.txt_detailes .get('1.0',END)
        self.pass_word_entry.delete(0,END)
        self.cpass_word.delete(0,END)
        self.gender.current(0)




    def register_data(self):
      self.clint()
      if  self.your_name.get()=="" or self.your_sector.get()=="" or self.txt_date_entry .get()=="" or  self.Email_entry.get()=="" or   self.gender.get()=="Select" or self.txt_detailes.get('1.0',END) =="" or  self.pass_word_entry.get() =="" or self.cpass_word.get() =="":
         messagebox.showerror("Error","All Fields Are Required", parent=self.root)

      elif self.pass_word_entry.get() != self.cpass_word.get():
         messagebox.showerror("Error", "Password not same", parent=self.root)

      elif self.var_chk.get()==0:
         messagebox.showerror("Error", "Please Agree Our all Condition and press registration button again", parent=self.root)

      else:


       try:
          con=pymysql.connect(host="localhost",user="root", password="",database="employ2")
          cur=con.cursor()
          cur.execute("select * from emp where email =%s",self.Email_entry.get())
          row=cur.fetchone()

          if row!=None:
              messagebox.showerror("Error", "User already Exist ",
                                   parent=self.root)

          else:

              cur.execute("insert into emp(name,sector,date,email,gender,details,password) values(%s,%s,%s,%s,%s,%s,%s)",
                          (self.your_name.get()
                           ,self.your_sector.get(),
                           self.txt_date_entry .get(),
                           self.Email_entry.get(),
                           self.gender.get(),
                           self.txt_detailes .get('1.0',END),
                           self.pass_word_entry.get()

                           ))
              con.commit()
              messagebox.showinfo("Done","Register Successful",parent=self.root)
              self.clear()

       except Exception as es:
          messagebox.showerror("Error", f"Error due to:{str(es)}",
                               parent=self.root)





root=Tk()
object=Register(root)
root.mainloop()
