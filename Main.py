from tkinter import *
import tkinter.messagebox
import mysql.connector
from Store.data import Data
from PIL import Image, ImageTk
from Components.EditEmp import EmpEdit
from Components.Departments import Departments
from Components.Payroll import Payroll
class EmployeeManagement:
    def __init__(self):
        self.Data = Data()
        self.root = Tk()
        self.image = Image.open("D:\\Shiash Internship\\CodingPractices\\EmployeeManagementSystem\\Assets\\logo.png")
        self.photo = ImageTk.PhotoImage(self.image)
        self.db = mysql.connector.connect(user  = "root", password = "", host = "localhost", db = "employeemanagement")
        self.cursor =  self.db.cursor()
        self.root.geometry("700x600")
        self.root.title("Employee Management System")
        self.root.configure(bg = "lightblue")
        self.ID = IntVar()
        self.Name = StringVar()
        self.Dept = StringVar()
        self.Dob = StringVar()
        self.Role = StringVar()
        self.Email  = StringVar()
        self.Phone = IntVar()
        self.Salary = IntVar()
        self.Bonus = IntVar()
        self.Decuction = IntVar()
        self.Pay_Date = StringVar()
        self.HomePage = Frame(self.root, bg = "lightblue")
        self.HomePage.pack(fill = BOTH, expand = True)
        self.EditPage = Frame(self.root, bg = "lightblue")
        self.DeptPage = Frame(self.root, bg = "lightblue")
        self.PayRollpage = Frame(self.root, bg = "lightblue")
        self.activePage = None
        self.WelcomeScreen()
        self.root.mainloop()

    def AddEmp(self):
        name = self.Name.get()
        dob = self.Dob.get()
        mail = self.Email.get()
        phone = self.Phone.get()
        role = self.Role.get()
        dept = self.Dept.get()
        if "@" in mail and name != "" and dob != "" and mail != "" and phone != "" and role != "" and dept != "":
            self.cursor.execute("insert into employees(Name, DOB, Email, Phone, Role, Dept) values(%s, %s, %s, %s, %s, %s)", [name, dob, mail, phone, role, dept])
            self.db.commit()
            self.Name.set('')
            self.Dob.set('')
            self.Email.set('')
            self.Phone.set('')
            self.Role.set('')
            self.Dept.set('')
            tkinter.messagebox.showinfo("emp added", "Employee Added Successfully")
        else:
            tkinter.messagebox.showerror("emp addition err", "Please Enter Valid Details")
    
    def UpdateEmp(self):
        id = self.ID.get()
        name = self.Name.get()
        dept = self.Dept.get()
        dob = self.Dob.get()
        mail = self.Email.get()
        ph = self.Phone.get()
        role = self.Role.get()
        if id in self.Data.ID():
            self.cursor.execute("update employees set Name = %s, Dept = %s, DOB = %s, Email  = %s, Phone = %s, Role = %s where ID = %s", [name, dept, dob, mail, ph, role, id])
            self.db.commit()
            tkinter.messagebox.showinfo("update added", "Employee Updated Successfully")
        else:
            tkinter.messagebox.showerror("emp update err", "There is no Employee with this ID")

    def Back(self):
        self.activePage.pack_forget()
        self.HomePage.pack(fill = BOTH, expand = True)

    def GoEmpEditPage(self):
        global activePage
        self.HomePage.pack_forget()
        self.EditPage.pack(fill = BOTH, expand = True)
        self.activePage = self.EditPage
        self.EmpEditScreen()

    def GoDeptPage(self):
        global activePage
        self.HomePage.pack_forget()
        self.DeptPage.pack(fill = BOTH, expand = True)
        self.activePage = self.DeptPage
        self.DepartmentsScreen()

    def GoPayRollPage(self):
        global activePage
        self.HomePage.pack_forget()
        self.PayRollpage.pack(fill = BOTH, expand = True)
        self.activePage = self.PayRollpage
        self.PayRollScreen()

    def GoViewEmpPage(self):
        viewEmp = Toplevel(self.root)
        viewEmp.geometry("1000x500")
        viewEmp.title("view all employee details")
        viewEmp.configure(bg = "lightblue")
        names = ["ID", "Name", "DOB", "Email", "Phone", "Role", "Dept"]
        Label(viewEmp, text = "All Employee Details", fg = "blue", bg = "lightblue").grid(row = 0)
        for i in range(len(names)):
            Label(viewEmp, text = names[i], fg = "blue", bg = "lightblue", font = ("calibri", 15)).grid(row = 1, column = i)
        for i in range(len(self.Data.emp_data())):
            for j in range(len(self.Data.emp_data()[0])):
                E = Entry(viewEmp, text = "")
                E.grid(row = i+2, column = j, padx = 5, pady = 2)
                E.insert(END, self.Data.emp_data()[i][j])
        
        viewEmp.mainloop()

    def EmpDelete(self):
        id = self.ID.get()
        if id in self.Data.ID():
            self.cursor.execute("delete from employees where Id = %s", [id])
            self.db.commit()
            tkinter.messagebox.showinfo("emp deleted", "Employee Deleted Successfully")
        else:
            tkinter.messagebox.showerror("emp delete err", "There is no Employee with this ID")

    def EmpView(self):
        id = self.ID.get()
        name = self.Name.get()
        self.cursor.execute("select * from employees where Id = %s OR Name = %s", [id, name])
        data = self.cursor.fetchall()
        if id != '' or name != '':
            if len(data)  > 0:
                self.ID.set(data[0][0])
                self.Name.set(data[0][1])
                self.Dob.set(data[0][2])
                self.Email.set(data[0][3])
                self.Phone.set(data[0][4])
                self.Role.set(data[0][5])
                self.Dept.set(data[0][6])
            else:
                tkinter.messagebox.showerror("no data", "There is no user with this ID")
        else:
            tkinter.messagebox.showerror("no data", "Please enter Id or Name to see the details")

    def SavePayRoll(self):
        id = self.ID.get()
        salary = self.Salary.get()
        bonus = self.Bonus.get()
        deduction = self.Decuction.get()
        pay_date = self.Pay_Date.get()
        
        if id in self.Data.ID():
            self.cursor.execute("insert into payroll(ID, Salary, Bonus, Deduction, Pay_Date) values(%s, %s,  %s, %s, %s)", [id, salary, bonus, deduction, pay_date])
            self.db.commit()
        else:
            tkinter.messagebox.showerror("no id", "there is no employee with this id")

    def ViewEmpByDept(self, d):
        emps = Toplevel(self.root)
        emps.geometry("1000x500")
        emps.title("Employees by Department")
        emps.configure(bg = "lightblue")
        self.cursor.execute("select * from employees where Dept = %s", [d])
        data = self.cursor.fetchall()
        Label(emps, text = f"View Employees of {d} Department", bg = "lightblue", fg = "blue").grid(row = 0)
        for i in range(len(data)):
            for j in range(len(data[0])):
                E = Entry(emps, text ='')
                E.grid(row = i+1,column = j, padx = 5)
                E.insert(END, data[i][j])
        
        emps.mainloop()

    def ViewPayRoll(self):
        salaries = Toplevel(self.root)
        salaries.geometry("1000x500")
        salaries.title("Salary Details")
        salaries.configure(bg = "lightblue")
        Label(salaries, text = "View Paid Employees Salary Details", bg = "lightblue", fg = "blue").grid(row = 0)
        names = ["ID", "Name", "Salary", "Bonus", "Deduction", "Pay_Date"]
        for i in range(len(names)):
            Label(salaries, text = names[i], fg = "blue", bg = "lightblue", font = ("calibri", 15)).grid(row = 1, column = i)
        for i in range(len(self.Data.salary_data())):
            for j in range(len(self.Data.salary_data()[0])):
                E = Entry(salaries, text ='')
                E.grid(row = i+2,column = j, padx = 5, pady = 2)
                E.insert(END, self.Data.salary_data()[i][j]) 
        
        salaries.mainloop()

    def WelcomeScreen(self):
        Label(self.HomePage, text = "-----------------------------------------------------------", bg = "lightblue", fg = "blue", font = ("calibri", 25)).place(x = 60, y = 30)
        Label(self.HomePage, text = "Welcome to Employee Management System", bg = "lightblue", fg = "blue", font = ("calibri", 25)).place(x = 60, y = 10)

        Label(self.HomePage, image = self.photo, bg = "lightblue").place(x = 90, y = 100)
        
        Button(self.HomePage, text = "Add or Edit Employee", bg = "blue", fg = "white", font = ("calibri", 15), height = 1, width = 20, command = self.GoEmpEditPage).place(x = 270, y = 200)
        Button(self.HomePage, text = "Departments", bg = "blue", fg = "white", font = ("calibri", 15), height = 1, width = 20, command = self.GoDeptPage).place(x = 270, y = 250)
        Button(self.HomePage, text = "PayRoll", bg = "blue", fg = "white", font = ("calibri", 15), height = 1, width = 20, command = self.GoPayRollPage).place(x = 270, y = 300)
        Button(self.HomePage, text = "View Employees", bg = "blue", fg = "white", font = ("calibri", 15), height = 1, width = 20, command = self.GoViewEmpPage).place(x = 270, y = 350)

    def EmpEditScreen(self):
        emp_edit = EmpEdit(self.EditPage, self.Back)
        emp_edit.db = self.db
        emp_edit.cursor = self.cursor
        emp_edit.Data = self.Data
        emp_edit.EmpEditScreen()

    def DepartmentsScreen(self):
        dept = Departments(self.DeptPage, self.Back)
        dept.db = self.db
        dept.cursor = self.cursor
        dept.Data = self.Data
        dept.DepartmentsScreen()

    def PayRollScreen(self):
        payroll = Payroll(self.PayRollpage, self.Back)
        payroll.PayRollScreen()
    
if __name__ == "__main__":
    E = EmployeeManagement()