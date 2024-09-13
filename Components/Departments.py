from tkinter import *
import tkinter.messagebox
import sys
import os
# Add the parent directory of folder_one and folder_two to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Store.data import Data

class Departments:
    def __init__(self, root, back, viewByDept):
        self.Data = Data()
        self.DeptPage = Frame(root, bg = "lightblue")
        self.DeptPage.pack(fill = BOTH, expand = True)
        self.Back = back
        
        self.viewByDept = viewByDept
        self.DepartmentsScreen()
    def GoDeptPage(self):
        global activePage
        self.HomePage.pack_forget()
        self.DeptPage.pack(fill = BOTH, expand = True)
        self.activePage = self.DeptPage

 
    def DepartmentsScreen(self):
        i = 1
        j = 50
        for dept in self.Data.Dept():
            Button(self.DeptPage, text = dept, bg = "blue", fg = "white", height = 2, width = 12, font = ("calibri", 10), command = lambda dept = dept : self.viewByDept(dept)).place(x = i * 100, y = j)
            i += 1
            if i >= 6:
                j *= 2
                i = 1
        Button(self.DeptPage, text = "Back", bg = "blue", fg = "white", font = ("calibri", 15), command = self.Back).place(x = 10, y = 10)

    
if __name__ == "__main__":
    Departments()