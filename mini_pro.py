from customtkinter import *
import sqlite3
from App import Application, menubar

conn = sqlite3.connect('database.db')
c = conn.cursor()
ids = []
number = []
patients = []

window = CTk()
b = Application(window)
b.startpage()
window.config(menu=menubar())
window.title("Hospital Management")
window.iconbitmap(r'medkit.ico')
window.geometry("450x400")
window.resizable(False, False)

window.mainloop()

