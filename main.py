from tkinter import *
from tkinter import messagebox,ttk
import pymysql
import time
import os
import tempfile
class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Payroll Calculator |I051 I059 I065 I069")
        self.root.geometry("1350x700+0+0")
        title=Label(self.root,text="Payroll Calculator",font=("liquid crystal",30),bg="darkblue",fg="white").place(x=0,y=0,relwidth=1)
        btn_EMP = Button(self.root, text="All Employee's",command=self.employee_frame, font=("liquid crystal", 12), bg="grey",fg="white").place(x=1100, y=10)

        #FRAMES
        Frame1=Frame(self.root,bd=2,relief=RIDGE)
        Frame1.place(x=0,y=51,width=570,height=645)

        Frame2 = Frame(self.root, bd=2, relief=RIDGE)
        Frame2.place(x=571, y=51, width=450, height=410)

        Frame3 = Frame(self.root, bd=2, relief=RIDGE)
        Frame3.place(x=571, y=451, width=450, height=400)

        Frame4 = Frame(self.root, bd=2, relief=RIDGE)
        Frame4.place(x=1022, y=51, width=450, height=645)

        self.var_emp_code = StringVar()
        self.var_Designation = StringVar()
        self.var_Name = StringVar()
        self.var_Age = StringVar()
        self.var_Gender = StringVar()
        self.var_Email = StringVar()
        self.var_DOB = StringVar()
        self.var_DOJ = StringVar()
        self.var_ProofID = StringVar()
        self.var_ContactNO = StringVar()
        self.var_Experience = StringVar()
        title2 = Label(Frame1, text="Information", font=("liquid crystal", 20), bg="darkred",fg="white").place(x=0, y=0, relwidth=1)

        lb1_code= Label(Frame1, text="Employee Code:", font=("liquid crystal", 19), bg="white",fg="black").place(x=10, y=50)
        self.txt_code = Entry(Frame1, font=("liquid crystal", 19),textvariable=self.var_emp_code , bg="lightyellow",fg="black")
        self.txt_code.place(x=210, y=48, height=40)

        lb1_designation = Label(Frame1, text="Designation:", font=("liquid crystal", 19), bg="white", fg="black").place(x=10,y=100)
        txt_designation = Entry(Frame1, font=("liquid crystal", 19),textvariable=self.var_Designation, bg="lightyellow", fg="black").place(x=160,y=102,height=36)

        lb1_DOB = Label(Frame1, text="D.O.B", font=("liquid crystal", 19), bg="white", fg="black").place(x=10, y=145)
        txt_DOB = Entry(Frame1, font=("liquid crystal", 19),textvariable=self.var_DOB, bg="lightyellow",fg="black").place(x=160, y=145,height=36)

        lb1_Name = Label(Frame1, text="Name:", font=("liquid crystal", 19), bg="white", fg="black").place(x=10, y=185)
        txt_Name = Entry(Frame1, font=("liquid crystal", 19),textvariable=self.var_Name, bg="lightyellow", fg="black").place(x=160,y=185,height=36)

        lb1_Age = Label(Frame1, text="Age:", font=("liquid crystal", 19), bg="white", fg="black").place(x=10, y=225)
        txt_Age = Entry(Frame1, font=("liquid crystal", 19),textvariable=self.var_Age, bg="lightyellow", fg="black").place(x=160,y=225,height=36)

        lb1_Gender = Label(Frame1, text="Gender:", font=("liquid crystal", 19), bg="white", fg="black").place(x=10, y=265)
        txt_Gender = Entry(Frame1, font=("liquid crystal", 19),textvariable=self.var_Gender, bg="lightyellow", fg="black").place(x=160,y=265,height=36)

        lb1_Email = Label(Frame1, text="Email:", font=("liquid crystal", 19), bg="white", fg="black").place(x=10, y=305)
        txt_Email = Entry(Frame1, font=("liquid crystal", 19),textvariable=self.var_Email, bg="lightyellow", fg="black").place(x=160,y=305,height=36)

        lb1_DOJ = Label(Frame1, text="D.O.J", font=("liquid crystal", 19), bg="white", fg="black").place(x=10, y=345)
        txt_DOJ = Entry(Frame1, font=("liquid crystal", 19),textvariable=self.var_DOJ, bg="lightyellow", fg="black").place(x=160,y=345,height=36)

        lb1_Experience = Label(Frame1, text="Experience:", font=("liquid crystal", 19), bg="white", fg="black").place(x=10, y=385)
        txt_Experience = Entry(Frame1, font=("liquid crystal", 19),textvariable=self.var_Experience, bg="lightyellow", fg="black").place(x=160,y=385,height=36)

        lb1_ProofID = Label(Frame1, text="Proof ID:", font=("liquid crystal", 19), bg="white", fg="black").place(x=10, y=425)
        txt_ProofID = Entry(Frame1, font=("liquid crystal", 19),textvariable=self.var_ProofID, bg="lightyellow", fg="black").place(x=160,y=425,height=36)

        lb1_ContactNumber = Label(Frame1, text="Contact NO.", font=("liquid crystal", 19), bg="white", fg="black").place(x=10, y=465)
        txt_ContactNumber = Entry(Frame1, font=("liquid crystal", 19),textvariable=self.var_ContactNO, bg="lightyellow", fg="black").place(x=160,y=465,height=36)

        lb1_Address = Label(Frame1, text="Address:", font=("liquid crystal", 19), bg="white", fg="black").place(x=10, y=510)
        self.txt_Address = Text(Frame1, font=("liquid crystal", 19), bg="lightyellow", fg="black")
        self.txt_Address.place(x=160,y=505,width=405,height=90)


        #==================================================================================================================================================================
        self.var_Month = StringVar()
        self.var_Year = StringVar()
        self.var_TotalDays = StringVar()
        self.var_Absents = StringVar()
        self.var_BasicSalary = StringVar()
        self.var_Medical = StringVar()
        self.var_Convence = StringVar()
        self.var_ProvidentFund = StringVar()
        self.var_NetSalary  = StringVar()

        title3 = Label(Frame2, text="Salary Details", font=("liquid crystal", 20), bg="darkred", fg="white").place(x=0,y=0,relwidth=1)

        lb1_Month = Label(Frame2, text="Month:", font=("liquid crystal", 13), bg="white", fg="black").place(x=10, y=50)
        txt_Month = Entry(Frame2, font=("liquid crystal", 15),textvariable=self.var_Month, bg="lightyellow", fg="black").place(x=140, y=49,height=30)

        lb1_Year = Label(Frame2, text="Year:", font=("liquid crystal", 13), bg="white", fg="black").place(x=10, y=90)
        txt_Year = Entry(Frame2, font=("liquid crystal", 15),textvariable=self.var_Year, bg="lightyellow", fg="black").place(x=140, y=89,height=30)

        lb1_TotalDays = Label(Frame2, text="Total Days:", font=("liquid crystal", 13), bg="white", fg="black").place(x=10, y=130)
        txt_TotalDays = Entry(Frame2, font=("liquid crystal", 15),textvariable=self.var_TotalDays, bg="lightyellow", fg="black").place(x=140, y=129,height=30)

        lb1_Absents = Label(Frame2, text="Absents:", font=("liquid crystal", 13), bg="white", fg="black").place(x=10, y=170)
        txt_Absents = Entry(Frame2, font=("liquid crystal", 15),textvariable=self.var_Absents, bg="lightyellow", fg="black").place(x=140, y=169,height=30)

        lb1_BasicSalary = Label(Frame2, text="Basic Salary:", font=("liquid crystal", 13), bg="white", fg="black").place(x=10, y=210)
        txt_BasicSalary = Entry(Frame2, font=("liquid crystal", 15),textvariable=self.var_BasicSalary, bg="lightyellow", fg="black").place(x=140, y=209,height=30)

        lb1_Medical = Label(Frame2, text="Medical:", font=("liquid crystal", 13), bg="white", fg="black").place(x=10, y=250)
        txt_Medical = Entry(Frame2, font=("liquid crystal", 15),textvariable=self.var_Medical, bg="lightyellow", fg="black").place(x=140, y=249,height=30)

        lb1_Convence = Label(Frame2, text="Convence:", font=("liquid crystal", 13), bg="white", fg="black").place(x=10, y=290)
        txt_Convence = Entry(Frame2, font=("liquid crystal", 15),textvariable=self.var_Convence, bg="lightyellow", fg="black").place(x=140, y=289,height=30)

        lb1_ProvidentFund = Label(Frame2, text="Provident Fund:", font=("liquid crystal", 13), bg="white", fg="black").place(x=10, y=330)
        txt_ProvidentFund = Entry(Frame2, font=("liquid crystal", 15),textvariable=self.var_ProvidentFund, bg="lightyellow", fg="black").place(x=140, y=329,height=30)

        lb1_NetSalary = Label(Frame2, text="Net Salary:", font=("liquid crystal", 13), bg="white", fg="black").place(x=10, y=365)
        txt_NetSalary = Entry(Frame2, font=("liquid crystal", 15),textvariable=self.var_NetSalary, bg="white", fg="black").place(x=140, y=364,height=30)
#==========================================================Function Buttons=========================================================================================================================
        sal_Frame4 = Frame(Frame4, bg="white", bd=2, relief=RIDGE)
        sal_Frame4.place(x=2, y=2, width=240, height=590)

        self.btn_Save = Button(sal_Frame4, text="Save",command=self.add, font=("liquid crystal", 19), bg="lime", fg="white")
        self.btn_Save.place(x=3,y=380,height=45,width=230)
        btn_Clear = Button(Frame4, text="Clear",command=self.clear, font=("liquid crystal", 19), bg="grey", fg="white").place(x=7,y=484,height=45,width=230)
        btn_Calculate = Button(Frame2, text="Calculate",command=self.calculate, font=("liquid crystal", 12), bg="blue", fg="white").place(x=367,y=360)
        btn_Search = Button(sal_Frame4, text="Search", command=self.search, font=("liquid crystal", 19), bg="limegreen",fg="white").place(x=3, y=330,height=45,width=230)
        self.btn_Delete = Button(sal_Frame4, text="Delete",state=DISABLED,command=self.delete, font=("liquid crystal", 19), bg="Red", fg="white")
        self.btn_Delete.place(x=3, y=430,height=45,width=230)
        #====================================================================CALCULATOR===============================================================================
        self.var_txt=StringVar()
        self.var_operator=''
        def but_ton(x):
            self.var_operator=self.var_operator+str(x)
            self.var_txt.set(self.var_operator)

        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator = ''

        def clearr():
            expression = ""
            self.var_txt.set(expression)
            self.var_operator = ''

        cal_Frame= Frame(Frame3,bg="white",bd=2, relief=RIDGE)
        cal_Frame.place(x=2,y=2,width=445,height=305)

        txt_Result = Entry(cal_Frame,bg="lightyellow",textvariable=self.var_txt,font=("liquid crystal", 20),justify=RIGHT).place(x=0,y=0,relwidth=1,height=39)

        but_1=Button(cal_Frame,text="1",command=lambda:but_ton(1),font=("liquid crystal",15), bg="blue", fg="white").place(x=0,y=39,w=60,h=60)
        but_2 = Button(cal_Frame, text="2",command=lambda:but_ton(2), font=("liquid crystal", 15), bg="blue", fg="white").place(x=61, y=39, w=60, h=60)
        but_3 = Button(cal_Frame, text="3",command=lambda:but_ton(3), font=("liquid crystal", 15), bg="blue", fg="white").place(x=122, y=39, w=60, h=60)
        but_4 = Button(cal_Frame, text="4",command=lambda:but_ton(4), font=("liquid crystal", 15), bg="blue", fg="white").place(x=183, y=39, w=60, h=60)
        but_5 = Button(cal_Frame, text="5",command=lambda:but_ton(5), font=("liquid crystal", 15), bg="blue", fg="white").place(x=243,y=39, w=60, h=60)
        but_6 = Button(cal_Frame, text="6",command=lambda:but_ton(6), font=("liquid crystal", 15), bg="blue", fg="white").place(x=303, y=39, w=60, h=60)
        but_7 = Button(cal_Frame, text="7",command=lambda:but_ton(7), font=("liquid crystal", 15), bg="blue", fg="white").place(x=363, y=39, w=60, h=60)

        but_a = Button(cal_Frame, text="+",command=lambda:but_ton('+'), font=("liquid crystal", 15), bg="blue", fg="white").place(x=0, y=100, w=60, h=60)
        but_s = Button(cal_Frame, text="-",command=lambda:but_ton('-'), font=("liquid crystal", 15), bg="blue", fg="white").place(x=61, y=100, w=60, h=60)
        but_8 = Button(cal_Frame, text="8",command=lambda:but_ton(8), font=("liquid crystal", 15), bg="blue", fg="white").place(x=122, y=100, w=60, h=60)
        but_9 = Button(cal_Frame, text="9",command=lambda:but_ton(9), font=("liquid crystal", 15), bg="blue", fg="white").place(x=183, y=100, w=60, h=60)
        but_0 = Button(cal_Frame, text="0",command=lambda:but_ton(0), font=("liquid crystal", 15), bg="blue", fg="white").place(x=243, y=100, w=60, h=60)
        but_m = Button(cal_Frame, text="*",command=lambda:but_ton('*'), font=("liquid crystal", 15), bg="blue", fg="white").place(x=303, y=100, w=60, h=60)
        but_d = Button(cal_Frame, text="/",command=lambda:but_ton('/'), font=("liquid crystal", 15), bg="blue", fg="white").place(x=363, y=100, w=60, h=60)

        but_e = Button(cal_Frame, text="=", command=result, font=("liquid crystal", 15), bg="blue", fg="white").place(x=0,y=160,w=240, h=60)
        but_C = Button(cal_Frame, text="C", command=clearr, font=("liquid crystal", 15), bg="red", fg="white").place(x=215, y=160,w=240,h=60)
        but_dot = Button(cal_Frame, text=".", command=lambda: but_ton('.'), font=("liquid crystal", 15), bg="blue",fg="white").place(x=422, y=39, w=20, h=121)
#=================================================================================================================================================================================
        title_sal = Label(sal_Frame4, text="Salary Reciept", font=("liquid crystal", 20), bg="darkred", fg="white").place(x=0,y=0,relwidth=1)

        sal_Frame2=Frame(sal_Frame4,bg="white",bd=2, relief=RIDGE)
        sal_Frame2.place(x=0,y=36,relwidth=1,h=290)
        #==================================================================================================================================================================================
        self.sample = f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor 4
---------------------------------------------------
    Employee ID\t\t: 
    Salary of\t\t:  Mon-YYYY
    Generated On\t\t:  DD-MM-YYYY
----------------------------------------------------
Total Days\t\t:  DD
Total Present\t\t:  DD
Total Absents\t\t:  DD
Convence\t\t:  Rs----
Medical\t\t:  Rs----
PF\t\t:  Rs----
Gross Payment\t\t:  Rs----
Net Salary\t\t:  Rs----
----------------------------------------------------
THIS IS A COMPUTER 
GENERATED SLIP,
NOT REQUIRED ANY SIGNATURE
    '''
#======================================================================================================================================================================================
        scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_recipt=Text(sal_Frame2,font=("times new roman",10), bg='lightyellow',yscrollcommand=scroll_y.set)
        self.txt_salary_recipt.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_recipt.yview)
        self.txt_salary_recipt.insert(END,self.sample)
        self.btn_Print = Button(sal_Frame4, text="Print",state=DISABLED,command=self.print, font=("liquid crystal", 19), bg="black", fg="white")
        self.btn_Print.place(x=3,y=530,height=45,width=230)
#========================================================FUNCTIONS==============================================================================================
    def search(self):
        try:
            con = pymysql.connect(host='localhost', port=3308, user='root', password='', database='employee')
            cur = con.cursor()
            cur.execute("SELECT * FROM `employee-salary` where emp_code=%s", (self.var_emp_code.get()))
            rows = cur.fetchone()
            if rows ==None:
               messagebox.showerror("Error", "InValid Employee ID,Please Try Again With Another Employee ID",parent=self.root)
            else:
                print(rows)
                self.var_emp_code.set(rows[0])
                self.var_Designation.set(rows[1])
                self.var_Name.set(rows[2])
                self.var_Age.set(rows[3])
                self.var_Gender.set(rows[4])
                self.var_Email.set(rows[5])
                self.var_DOB.set(rows[6])
                self.var_DOJ.set(rows[7])
                self.var_ProofID.set(rows[8])
                self.var_ContactNO.set(rows[9])
                self.var_Experience.set(rows[10])
                self.txt_Address.delete('1.0',END)
                self.txt_Address.insert(END, rows[11])

                self.var_Month.set(rows[12])
                self.var_Year.set(rows[13])
                self.var_TotalDays.set(rows[14])
                self.var_Absents.set(rows[15])
                self.var_BasicSalary.set(rows[16])
                self.var_Medical.set(rows[17])
                self.var_Convence.set(rows[18])
                self.var_ProvidentFund.set(rows[19])
                self.var_NetSalary.set(rows[20])
                file_ = open("s" + str(rows[21]), 'r')
                self.txt_salary_recipt.delete('1.0',END)
                for i in file_:
                    self.txt_salary_recipt.insert(END,i)
                file_.close()
                self.btn_Save.config(state=DISABLED)
                self.btn_Delete.config(state=NORMAL)
                self.txt_code.config(state='readonly')
                self.btn_Print.config(state=NORMAL)
        except Exception as ex:
            messagebox.showerror("Error", f'Error Due to This: {str(ex)}')



    def clear(self):
        self.btn_Save.config(state=NORMAL)
        self.btn_Print.config(state=DISABLED)
        self.btn_Delete.config(state=DISABLED)
        self.txt_code.config(state=NORMAL)
        self.var_emp_code.set('')
        self.var_Designation.set('')
        self.var_Name.set('')
        self.var_Age.set('')
        self.var_Gender.set('')
        self.var_Email.set('')
        self.var_DOB.set('')
        self.var_DOJ.set('')
        self.var_ProofID.set('')
        self.var_ContactNO.set('')
        self.var_Experience.set('')
        self.txt_Address.delete('1.0',END)

        self.var_Month.set('')
        self.var_Year.set('')
        self.var_TotalDays.set('')
        self.var_Absents.set('')
        self.var_BasicSalary.set('')
        self.var_Medical.set('')
        self.var_Convence.set('')
        self.var_ProvidentFund.set('')
        self.var_NetSalary.set('')
        self.txt_salary_recipt.delete('1.0',END)
        self.txt_salary_recipt.insert(END,self.sample)

    def delete(self):
        if self.var_emp_code.get()=='':
            messagebox.showerror("Error","Employee ID Must Be Required")
        else:
            try:
                con = pymysql.connect(host='localhost', port=3308, user='root', password='', database='employee')
                cur = con.cursor()
                cur.execute("SELECT * FROM `employee-salary` where emp_code=%s", (self.var_emp_code.get()))
                rows = cur.fetchone()

                if rows == None:
                    messagebox.showerror("Error", "InValid Employee ID,Please Try Again With Another Employee ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do You Really Want To Delete")
                    if op==True:
                        cur.execute("delete FROM `employee-salary` where emp_code=%s", (self.var_emp_code.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete","Employee Record Deleted Successfuly",parent=self.root)
                        self.clear()
            except Exception as ex:
                messagebox.showerror("Error", f'Error Due to This: {str(ex)}')

    def add(self):
        if self.var_emp_code.get()=='' or self.var_NetSalary.get()=='' or self.var_Name.get()=='' :
            messagebox.showerror("Error","Employee Details Required")
        else:
            try:
                con = pymysql.connect(host='localhost', port=3308, user='root', password='', database='employee')
                cur = con.cursor()
                cur.execute("SELECT * FROM `employee-salary` where emp_code=%s", (self.var_emp_code.get()))
                rows = cur.fetchone()
                # print(rows)
                if rows != None:
                    messagebox.showerror("Error", "This Employee ID IS Already Available, Try Again With Another ID",
                                         parent=self.root)

                else:
                    cur.execute(
                        "INSERT into`employee-salary` VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                         self.var_emp_code.get(),
                         self.var_Designation.get(),
                         self.var_Name.get(),
                         self.var_Age.get(),
                         self.var_Gender.get(),
                         self.var_Email.get(),
                         self.var_DOB.get(),
                         self.var_DOJ.get(),
                         self.var_ProofID.get(),
                         self.var_ContactNO.get(),
                         self.var_Experience.get(),
                         self.txt_Address.get('1.0',END),

                         self.var_Month.get(),
                         self.var_Year.get(),
                         self.var_TotalDays.get(),
                         self.var_Absents.get(),
                         self.var_BasicSalary.get(),
                         self.var_Medical.get(),
                         self.var_Convence.get(),
                         self.var_ProvidentFund.get(),
                         self.var_NetSalary.get(),
                         self.var_emp_code.get()+ ".txt"
                         )
                         )
                    messagebox.showinfo("Success", "Record Added Successfully")
                con.commit()
                con.close()
                file_=open("s"+str(self.var_emp_code.get())+".txt",'w')
                file_.write(self.txt_salary_recipt.get('1.0',END))
                file_.close()
            except Exception as ex:
                messagebox.showerror("Error", f'Error Due to This: {str(ex)}')
                self.btn_Print.config(state=NORMAL)

    def calculate(self):
        if self.var_Month.get() == '' or self.var_Year.get() == '' or self.var_BasicSalary.get() == '' or self.var_TotalDays.get() == '' or self.var_Absents.get() == '' or self.var_emp_code.get() == '' or self.var_Name.get() == '' or self.var_Experience.get() == '':
            messagebox.showerror('Error', 'All fields are required')
        else:
            per_day = int(self.var_BasicSalary.get()) / int(self.var_TotalDays.get())
            work_day = int(self.var_TotalDays.get()) - int(self.var_Absents.get())
            sal_ = per_day * work_day
            deduct = int(self.var_Medical.get()) + int(self.var_ProvidentFund.get())
            addition = int(self.var_Convence.get())
            net_sal = sal_ - deduct + addition
            self.var_NetSalary.set(str(round(net_sal, 2)))
#========================Updating======================================================================
            new_sample = f'''\tCompany Name, XYZ\n\tAddress: Xyz, Floor 4
--------------------------------------------------
Employee ID\t\t:  {self.var_emp_code.get()}
Salary of\t\t:  {self.var_Month.get()}-{self.var_Year.get()}
Generated On\t\t:  {str(time.strftime("%d-%m-%Y"))}
---------------------------------------------------
Total Days\t\t:  {self.var_TotalDays.get()}
Total Present\t\t:  {str(int(self.var_TotalDays.get())-int(self.var_Absents.get()))}
Total Absents\t\t:  {self.var_Absents.get()}
Convence\t\t:  {self.var_Convence.get()}
Medical\t\t:  {self.var_Medical.get()}
PF\t\t:  {self.var_ProvidentFund.get()}
Gross Payment\t\t:  {self.var_BasicSalary.get()}
Net Salary\t\t:  {self.var_NetSalary.get()}
----------------------------------------------------
THIS IS A COMPUTER 
GENERATED SLIP,
NOT REQUIRED ANY SIGNATURE
            '''
            self.txt_salary_recipt.delete('1.0',END)
            self.txt_salary_recipt.insert(END,new_sample)
    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',port=3308,user='root',password='',database='employee')
            cur=con.cursor()
            cur.execute("SELECT * FROM `employee-salary`")
            ro=cur.fetchall()
            print(ro)

        except Exception as ex:
            messagebox.showerror("Error",f'Error Due to This: {str(ex)}')
    def show(self):
        try:
            con=pymysql.connect(host='localhost',port=3308,user='root',password='',database='employee')
            cur=con.cursor()
            cur.execute("SELECT * FROM `employee-salary`")
            ro=cur.fetchall()
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in ro:
                self.employee_tree.insert('',END,values=row)
            con.close()

        except Exception as ex:
            messagebox.showerror("Error",f'Error Due to This: {str(ex)}')


    def employee_frame(self):
        self.root2 = Toplevel(self.root)
        self.root2.title("Payroll Calculator | Created By Utkarsh Rawat | Roll no.16 Class 12 E")
        self.root2.geometry("1000x500+120+100")
        title = Label(self.root2, text="All Employee Details", font=("liquid crystal", 20), bg="black",fg="white").pack(side=TOP,fill=X)
        self.root2.focus_force()

        scroll_y=Scrollbar(self.root2,orient=VERTICAL)
        scroll_x= Scrollbar(self.root2,orient=HORIZONTAL)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.pack(side=BOTTOM,fill=X)

        self.employee_tree=ttk.Treeview(self.root2,columns=('emp_code', 'Designation', 'Name', 'Age', 'Gender', 'Email', 'DOB', 'DOJ', 'Proof ID', 'Contact No.', 'Experience', 'Address', 'Month', 'Year', 'Total Days', 'Absents', 'Basic Salary', 'Medical', 'Convence', 'Provident Fund', 'Net Salary', 'sal_receipt'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
        self.employee_tree.heading('emp_code',text='Employee Code')
        self.employee_tree.heading('Designation', text='Designation')
        self.employee_tree.heading('Name', text='Name')
        self.employee_tree.heading('Age', text='Age')
        self.employee_tree.heading('Gender', text='Gender')
        self.employee_tree.heading('Email', text='Email')
        self.employee_tree.heading('DOB', text='DOB')
        self.employee_tree.heading('DOJ', text='DOJ')
        self.employee_tree.heading('Proof ID', text='Proof ID')
        self.employee_tree.heading('Contact No.', text='Contact No.')
        self.employee_tree.heading('Experience', text='Experience')
        self.employee_tree.heading('Address', text='Address')
        self.employee_tree.heading('Month', text='Month')
        self.employee_tree.heading('Year', text='Year')
        self.employee_tree.heading('Total Days', text='Total Days')
        self.employee_tree.heading('Absents', text='Absents')
        self.employee_tree.heading('Basic Salary', text='Basic Salary')
        self.employee_tree.heading('Medical', text='Medical')
        self.employee_tree.heading('Convence', text='Convence')
        self.employee_tree.heading('Provident Fund', text='Provident Fund')
        self.employee_tree.heading('Net Salary', text='Net Salary')
        self.employee_tree.heading('sal_receipt', text='Salary Receipt')
        self.employee_tree['show']='headings'

        self.employee_tree.column('emp_code',width=100)
        self.employee_tree.column('Designation', width=100)
        self.employee_tree.column('Name', width=100)
        self.employee_tree.column('Age', width=100)
        self.employee_tree.column('Gender', width=100)
        self.employee_tree.column('Email', width=100)
        self.employee_tree.column('DOB', width=100)
        self.employee_tree.column('DOJ', width=100)
        self.employee_tree.column('Proof ID', width=100)
        self.employee_tree.column('Contact No.', width=100)
        self.employee_tree.column('Experience', width=100)
        self.employee_tree.column('Address', width=500)
        self.employee_tree.column('Month', width=100)
        self.employee_tree.column('Year', width=100)
        self.employee_tree.column('Total Days', width=100)
        self.employee_tree.column('Absents', width=100)
        self.employee_tree.column('Basic Salary', width=100)
        self.employee_tree.column('Medical', width=100)
        self.employee_tree.column('Convence', width=100)
        self.employee_tree.column('Provident Fund', width=100)
        self.employee_tree.column('Net Salary', width=100)
        self.employee_tree.column('sal_receipt', width=100)
        scroll_x.config(command=self.employee_tree.xview)
        scroll_y.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()
    def print(self):
        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_recipt.get('1.0',END))
        os.startfile(file_,'print')




root=Tk()
obj=EmployeeSystem(root)
root.mainloop()


