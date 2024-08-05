from tkinter import *
import tkinter.messagebox
from Store.data import Data
class Payroll:
    def __init__(self, root, back):
        self.Data = Data
        self.PayRollpage = Frame(root, bg = "lightblue")
        self.PayRollpage.pack(fill = BOTH, expand = True)
        self.ID = IntVar()
        self.Salary = IntVar()
        self.Bonus = IntVar()
        self.Decuction = IntVar()
        self.Pay_Date = StringVar()
        self.Back = back
        self.PayRollScreen()

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

    # def Back(self):
    #     self.activePage.pack_forget()
    #     self.HomePage.pack(fill = BOTH, expand = True)

    def PayRollScreen(self):
        Label(self.PayRollpage, text = "Add or Edit Employee Salary Details", bg = "lightblue", fg = "blue", font = ("calibri", 25)).place(x = 60, y = 30)

        Label(self.PayRollpage, text = "ID", fg = "blue", bg = "lightblue", font = ("calibri", 15)).place(x = 70, y = 100)
        Label(self.PayRollpage, text = "Salary", fg = "blue", bg = "lightblue", font = ("calibri", 15)).place(x = 70, y = 150)
        Label(self.PayRollpage, text = "Bonus", fg = "blue", bg = "lightblue", font = ("calibri", 15)).place(x = 70, y = 200)
        Label(self.PayRollpage, text = "Decuction", fg = "blue", bg = "lightblue", font = ("calibri", 15)).place(x = 70, y = 250)
        Label(self.PayRollpage, text = "Pay_Date", fg = "blue", bg = "lightblue", font = ("calibri", 15)).place(x = 70, y = 300)

        Entry(self.PayRollpage, textvariable = self.ID, fg = "blue", bg = "lightblue", font = ("calibri", 15)).place(x = 190, y = 100)
        Entry(self.PayRollpage, textvariable = self.Salary, fg = "blue", bg = "lightblue", font = ("calibri", 15)).place(x = 190, y = 150)
        Entry(self.PayRollpage, textvariable = self.Bonus, fg = "blue", bg = "lightblue", font = ("calibri", 15)).place(x = 190, y = 200)
        Entry(self.PayRollpage, textvariable = self.Decuction, fg = "blue", bg = "lightblue", font = ("calibri", 15)).place(x = 190, y = 250)
        Entry(self.PayRollpage, textvariable = self.Pay_Date, fg = "blue", bg = "lightblue", font = ("calibri", 15)).place(x = 190, y = 300)
        
        Button(self.PayRollpage, text = "Save", bg = "blue", fg = "white", font = ("calibri", 15), command = self.SavePayRoll).place(x = 250, y = 400)
        Button(self.PayRollpage, text = "View Salary Details", bg = "blue", fg = "white", font = ("calibri", 15), command = self.ViewPayRoll).place(x = 350, y = 400)


        Button(self.PayRollpage, text = "Back", bg = "blue", fg = "white", font = ("calibri", 15), command = self.Back).place(x = 10, y = 10)


if __name__ == "__main__":
    Payroll()