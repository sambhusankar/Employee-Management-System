from tkinter import *
import tkinter.messagebox
from Store.data import Data
from EditEmp import EmpEdit
class Departments:
    def __init__(self):
        self.Data = Data()
        self.root = Tk()
        self.root.geometry("700x600")
        self.root.title("Employee Management System")
        self.root.configure(bg = "lightblue")
        self.DeptPage = Frame(self.root, bg = "lightblue")
        self.DeptPage.pack(fill = BOTH, expand = True)
        self.DepartmentsScreen()
        EmpEdit(self.root)
        self.root.mainloop()

    def GoDeptPage(self):
        global activePage
        self.HomePage.pack_forget()
        self.DeptPage.pack(fill = BOTH, expand = True)
        self.activePage = self.DeptPage

    def Back(self):
        self.activePage.pack_forget()
        self.HomePage.pack(fill = BOTH, expand = True)

    def DepartmentsScreen(self):
        i = 1
        j = 50
        for dept in self.Data.Dept():
            Button(self.DeptPage, text = dept, bg = "blue", fg = "white", height = 2, width = 12, font = ("calibri", 10), command = lambda dept = dept : self.ViewEmpByDept(dept)).place(x = i * 100, y = j)
            i += 1
            if i >= 6:
                j *= 2
                i = 1
        Button(self.DeptPage, text = "Back", bg = "blue", fg = "white", font = ("calibri", 15), command = self.Back).place(x = 10, y = 10)

    
if __name__ == "__main__":
    Departments()