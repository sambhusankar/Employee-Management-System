import mysql.connector
import tkinter.messagebox

class Data:
    def __init__(self):
        self.db = mysql.connector.connect(user = "root", password = "", host = "localhost", db = "employeemanagement")
        self.cursor = self.db.cursor()

    def emp_data(self):
        self.cursor.execute("select * from employees")
        d = self.cursor.fetchall()
        row = len(d)
        column = len(d[0])
        data = [[] for i in range(row)]
        for i in range(row):
            for j in range(column):
                data[i].append(d[i][j])
        
        return data
    
    def add_emp_data(self, name, dob, mail, phone, role, dept):
        if "@" in mail and name != "" and dob != "" and mail != "" and phone != "" and role != "" and dept != "":
            self.cursor.execute("insert into employees(Name, DOB, Email, Phone, Role, Dept) values(%s, %s, %s, %d, %s, %s)", [name, dob, mail, phone, role, dept])
            self.db.commit()
            tkinter.messagebox.showinfo("emp added", "Employee Added Successfully")
        else:
            tkinter.messagebox.showerror("emp addition err", "Please Enter Valid Details")
    
    def update_emp_data(self, id, name, dob, mail, phone, role, dept):
        if id in self.Data.ID():
            self.cursor.execute("update employees set Name = %s, Dept = %s, DOB = %s, Email  = %s, Phone = %s, Role = %s where ID = %s", [name, dept, dob, mail, phone, role, id])
            self.db.commit()
            tkinter.messagebox.showinfo("update added", "Employee Updated Successfully")
        else:
            tkinter.messagebox.showerror("emp update err", "There is no Employee with this ID")

    def salary_data(self):
        self.cursor.execute("select employees.ID, employees.Name, payroll.Salary, payroll.Bonus, payroll.Deduction, payroll.Pay_Date from employees inner join payroll ON employees.ID = payroll.ID")
        d = self.cursor.fetchall()
        row = len(d)
        column = len(d[0])
        data = [[] for i in range(row)]
        for i in range(row):
            for j in range(column):
                data[i].append(d[i][j])
        
        return data

    def ID(self):
        self.cursor.execute("select ID from employees")
        d = self.cursor.fetchall()
        data = []
        for i in range(len(d)):
            data.append(d[i][0])
        return data
    
    def Name(self):
        self.cursor.execute("select Name from employees")
        d = self.cursor.fetchall()
        data = []
        for i in range(len(d)):
            data.append(d[i][0])
        return data

    def Dept(self):
        self.cursor.execute("select Dept from employees")
        d = self.cursor.fetchall()
        data = set()
        for i in range(len(d)):
            data.add(d[i][0])
        return list(data)

    def DOB(self):
        self.cursor.execute("select DOB from employees")
        d = self.cursor.fetchall()
        return d

    def Email(self):
        self.cursor.execute("select Email from employees")
        d = self.cursor.fetchall()
        return d

    def Phone(self):
        self.cursor.execute("select Phone from employees")
        d = self.cursor.fetchall()
        return d

    def Role(self):
        self.cursor.execute("select Role from employees")
        d = self.cursor.fetchall()
        return d

    def Salary(self):
        self.cursor.execute("select Salary from payroll")
        d = self.cursor.fetchall()
        data = []
        for i in range(len(d)):
            data.append(d[i][0])
        return data

    def Bonus(self):
        self.cursor.execute("select Bonus from payroll")
        d = self.cursor.fetchall()
        return d

    def Deduction(self):
        self.cursor.execute("select Deduction from payroll")
        d = self.cursor.fetchall()
        return d

    def Pay_Date(self):
        self.cursor.execute("select Pay_Date from payroll")
        d = self.cursor.fetchall()
        return d    

if __name__ == "__main__":
    Data()
    