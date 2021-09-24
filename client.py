
from tkinter import*
from tkinter import  ttk
import pymysql
from tkinter import messagebox

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title(" Your Client List ")
        self.root.geometry("1350x700+0+0")
        self.root.maxsize(1350, 700)
        self.root.minsize(1350, 700)
        root.wm_iconbitmap('cl.ico')

        title=Label(self.root,text="Your Client List",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="#6e6d80",fg="black")
        title.pack(side=TOP,fill=X)

        #### All Variables#####
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_No_var = StringVar()
        self.gender_var = StringVar()
        self.contact_No_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt= StringVar()



        ############ Manage Frame ##############
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#6e6d80")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_Frame,text="ADD CLIENT INFORMATION",bg="#6e6d80",fg="black",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll= Label(Manage_Frame, text="SL NO:", bg="#6e6d80", fg="black", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10,padx=20,sticky="w")

        txt_Roll = Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman", 15, "bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name:", bg="#6e6d80", fg="black", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Name = Entry(Manage_Frame,textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email:", bg="#6e6d80", fg="black", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_Email = Entry(Manage_Frame,textvariable=self.email_No_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender:", bg="#6e6d80", fg="black", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman", 13, "bold"),state='readonly')
        combo_gender["values"]=("Male","Female","Others")
        combo_gender.grid(row=4, column=1, pady=10, padx=20)


        lbl_contact = Label(Manage_Frame, text="Contact:", bg="#6e6d80", fg="black", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(Manage_Frame,textvariable=self.contact_No_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_DOB = Label(Manage_Frame, text="Date:", bg="#6e6d80", fg="black",
                            font=("times new roman", 20, "bold"))
        lbl_DOB.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_DOB = Entry(Manage_Frame,textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_DOB.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_Add = Label(Manage_Frame, text="Problem:", bg="#6e6d80", fg="black",
                        font=("times new roman", 20, "bold"))
        lbl_Add.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.txt_Address=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_Address.grid(row=7,column=1,pady=10, padx=20,sticky="w")

        ########## Button Frame ###########

        button_Frame = Frame(Manage_Frame, bd=3, relief=RIDGE, bg="#B00857")
        button_Frame.place(x=15, y=520, width=420)

        Addbtn    = Button(button_Frame, text="Add",command=self.add_student,font=("times new roman", 10, "bold"),width=10) .grid(row=0,column=0,padx=10,pady=20)
        updatebtn = Button(button_Frame, text="Update",command=self.update_date,font=("times new roman", 10, "bold"), width=10).grid(row=0, column=1, padx=10, pady=20)
        deletbtn  = Button(button_Frame, text="Delete ",command=self.delet_data,font=("times new roman", 10, "bold"), width=10).grid(row=0, column=2,padx=10, pady=20)
        clearbtn  = Button(button_Frame, text="Clear",command=self.clear,font=("times new roman", 10, "bold"), width=10).grid(row=0, column=3, padx=10, pady=20)

        ############ Detail Frame ##############
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#6e6d80")
        Detail_Frame.place(x=500, y=100, width=800, height=580)

        lbl_search = Label(Detail_Frame, text="SHOW INFORMATION", bg="#6e6d80", fg="black",
                        font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")



        btn_regis = Button(Detail_Frame, text="MAIN WINDOW",command=self.regis, font=("times new roman", 14, "bold"),
                           bg="#B00857", cursor="hand2",
                           fg="white").grid(row=0,
                                                                                                           column=6,
                                                                                                           padx=10, pady=20)

        btn_login = Button(Detail_Frame, text="LOGIN WINDOW",command=self.login, font=("times new roman", 14, "bold"),
                           bg="#B00857", cursor="hand2",
                           fg="white").grid(row=0,
                                            column=12,
                                            padx=10, pady=20)


        #########Table Frame###########

        table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="#6e6d80")
        table_Frame.place(x=10, y=70, width=760,height=500)

        scroll_x=Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="SL_No.")
        self.Student_table.heading("name", text="NAME")
        self.Student_table.heading("email", text="EMAIL")
        self.Student_table.heading("gender", text="GENDER")
        self.Student_table.heading("contact", text="CONTACT")
        self.Student_table.heading("dob", text="DATE")
        self.Student_table.heading("address", text="PROBLEM")

        self.Student_table['show']='headings'
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=200)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()

    def add_student(self):
        if self.Roll_No_var.get() == "" or self.name_var.get() == "" or self.email_No_var.get() == "" or self.gender_var.get() == "" or self.contact_No_var.get() =="" or self.dob_var.get()=="" :
                messagebox.showerror("Error", "All Fields Are Required", parent=self.root)

        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",( self.Roll_No_var.get(),
                                                                             self.name_var.get(),
                                                                             self.email_No_var.get(),
                                                                             self.gender_var.get(),
                                                                             self.contact_No_var.get(),
                                                                             self.dob_var.get(),
                                                                             self.txt_Address.get('1.0',END)
          ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been inserted", parent=self.root)

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_No_var.set("")
        self.gender_var.set("")
        self.contact_No_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0", END)

    def login(self):
        self.root.destroy()
        import main


    def regis(self):
        self.root.destroy()
        import registar

    def get_cursor(self,ev):
        curosor_row=self.Student_table.focus()
        content=self.Student_table.item(curosor_row)
        row=content['values']
        # print(row)
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_No_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_No_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END,row[6])

    def update_date(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s", (
                                                                          self.name_var.get(),
                                                                          self.email_No_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.contact_No_var.get(),
                                                                          self.dob_var.get(),
                                                                          self.txt_Address.get('1.0', END),
                                                                          self.Roll_No_var.get()
                                                                          ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

        messagebox.showinfo("Info", "update your data", parent=self.root)


    def delet_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("delete  from students where roll_no=%s",self.Roll_No_var.get())
        rows=cur.fetchall()
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()



root=Tk()
obj=Student(root)
root.mainloop()
