from customtkinter import *
import tkinter
from tkinter.ttk import Separator
from tkinter import messagebox
from tkinter import *
from db import Database


class Application:

    def __init__(self, window):

        self.window = window
        self.db = Database('database.db')
        self.c = self.db.c
        self.conn = self.db.conn
        self.all_data = self.c.fetchall()
        # creating the frames in the window
        self.main = CTkFrame(window, width=450, height=400)

        self.show_details_frame = CTkFrame(self.window)
        self.update_frame = CTkFrame(self.window)
        self.delete_frame = CTkFrame(self.window)
        self.v = IntVar()

    def startpage(self):

        # labels for the window
        self.heading = CTkLabel(self.main, text="Hospital Management System", font=('Centaur', 20))
        self.heading.place(x=60, y=20)

        # name
        self.name = CTkLabel(self.main, text="Patients Name", font=('arial', 12))
        self.name.place(x=0, y=110)

        # age

        self.age = CTkLabel(self.main, text="Age", font=('arial', 12))
        self.age.place(x=0, y=155)

        # gender
        CTkLabel(self.main, text="Gender", font=('arial', 12)).place(x=0, y=210)
        a = CTkRadioButton(self.main, text="Male", font=('arial', 10), variable=self.v, value=1, ).place(x=130, y=210)
        b = CTkRadioButton(self.main, text="Female", font=('arial', 10), variable=self.v, value=2, ).place(x=220, y=210)

        # location

        self.time = CTkLabel(self.main, text="Location", font=('arial', 12))
        self.time.place(x=0, y=255)

        # phone

        self.phone = CTkLabel(self.main, text="Contact Number", font=('arial', 12))
        self.phone.place(x=0, y=300)

        # text box for lables

        self.name_entry = CTkEntry(self.main, width=250)
        self.name_entry.place(x=140, y=115)

        self.age_entry = CTkEntry(self.main, width=250)
        self.age_entry.place(x=140, y=160)

        self.location_entry = CTkEntry(self.main, width=250)
        self.location_entry.place(x=140, y=258)

        self.phone_entry = CTkEntry(self.main, width=250)
        self.phone_entry.place(x=140, y=310)

        # button to perform a command

        self.submit = CTkButton(self.main, text="Add Appointment", font=('arial', 12), width=15, height=2,
                                command=self.add_appointment)
        self.submit.place(x=150, y=340)

        # show log

        sql2 = "SELECT id FROM appointments "
        self.result = self.c.execute(sql2)
        for self.row in self.result:
            self.id = self.row[0]
            ids.append(self.id)

        # ordering the ids

        self.new = sorted(ids)
        self.final_id = self.new[len(ids) - 1]

        #  display the logs in our frame

        self.logs = CTkLabel(self.main, text="Total\n Appointments:", font=('arial', 10))
        self.logs.place(x=280, y=350)
        self.logs = CTkLabel(self.main, text=" " + str(self.final_id), width=8, height=1).place(x=360,
                                                                                                y=360)

        self.main.pack()

    # funtion to call submit button

    def add_appointment(self):

        self.val1 = self.name_entry.get()
        self.val2 = self.age_entry.get()
        if self.v.get() == 1:
            self.val3 = "Male"
        elif self.v.get() == 2:
            self.val3 = "Female"
        else:
            self.val3 = "Not Specified"
        self.val4 = self.location_entry.get()
        self.val5 = self.phone_entry.get()

        if self.val1 == '' or self.val2 == '' or self.val3 == '' or self.val4 == '' or self.val5 == '':
            tkinter.messagebox.showinfo("Warning", "Please Fill Up All Boxes")
        else:

            # sql = "INSERT INTO 'appointments' ( name, age, gender, location, phone) VALUES(?, ?, ?, ?, ? )"
            # c.execute(sql, (self.val1, self.val2, self.val3, self.val4, self.val5))
            sql = "INSERT INTO appointments (name, age, gender, location, phone) VALUES (?, ?, ?, ?, ?)"
            params = (self.val1, self.val2, self.val3, self.val4, self.val5)
            self.c.execute(sql, params)
            self.conn.commit()
            tkinter.messagebox.showinfo("Success", "\n Appointment for " + str(self.val1) + " has been created")
        self.main.destroy()
        self.__init__(self.window)
        self.startpage()

    def homee(self):
        self.main.destroy()
        self.show_details_frame.destroy()
        self.update_frame.destroy()
        self.delete_frame.destroy()
        self.__init__(self.window)
        self.startpage()
        self.main.pack()

    def show_details(self):
        self.main.destroy()
        self.show_details_frame.destroy()
        self.update_frame.destroy()
        self.delete_frame.destroy()
        self.__init__(self.window)
        count1 = 0
        count2 = 0
        column_name = ['App no', 'name', 'age', 'gender', 'location', 'contact no']
        for i in range(len(column_name)):
            CTkLabel(self.show_details_frame, text=column_name[i], font=('arial', 12), width=70).grid(row=0, column=i * 2)
            Separator(self.show_details_frame, orient=VERTICAL).grid(row=0, column=i * 2 + 1, sticky='ns')
        column_name = ['App no', 'name', 'age', 'gender', 'location', 'contact no']
        for i in range(len(column_name)):
            CTkLabel(self.show_details_frame, text=column_name[i], font=('arial', 12)).grid(row=0, column=i * 2)
            Separator(self.show_details_frame, orient=VERTICAL).grid(row=0, column=i * 2 + 1, sticky='ns')
        for i in range(len(self.all_data)):
            for j in range(6):
                CTkLabel(self.show_details_frame, text=self.all_data[i][j], font=('arial', 10)).grid(row=count1 + 2,
                                                                                                     column=count2 * 2)
                Separator(self.show_details_frame, orient=VERTICAL).grid(row=count1 + 2, column=count2 * 2 + 1,
                                                                         sticky='ns')
                count2 += 1
            count2 = 0
            count1 += 1
        self.show_details_frame.pack()

    def updatee(self):
        self.main.destroy()
        self.show_details_frame.destroy()
        self.update_frame.destroy()
        self.delete_frame.destroy()
        self.__init__(self.window)

        self.id = CTkLabel(self.update_frame, text="Search Appoinment Number To Update", font=('arial', 12))
        self.id.place(x=0, y=12)
        self.id_net = CTkEntry(self.update_frame, width=30)
        self.id_net.place(x=230, y=18)
        self.search = CTkButton(self.update_frame, text="Search", font=('arial', 12), width=10, height=1,
                                command=self.update1)
        self.search.place(x=160, y=50)
        self.update_frame.pack(fill='both', expand=True)

    def update1(self):
        self.input = self.id_net.get()
        # execute sql
        sql = "SELECT * FROM appointments WHERE id LIKE ?"
        self.res = self.c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.phone = self.row[5]
        # creating the update form
        self.uname = CTkLabel(self.update_frame, text="Patient's Name", font=('arial', 14))
        self.uname.place(x=0, y=140)

        self.patiant_age = CTkLabel(self.update_frame, text="Age", font=('arial', 14))
        self.patiant_age.place(x=0, y=180)

        self.patiant_gender = CTkLabel(self.update_frame, text="Gender", font=('arial', 14))
        self.patiant_gender.place(x=0, y=220)

        self.patiant_location = CTkLabel(self.update_frame, text="Location", font=('arial', 14))
        self.patiant_location.place(x=0, y=260)

        self.patiant_phone = CTkLabel(self.update_frame, text="Phone Number", font=('arial', 14))
        self.patiant_phone.place(x=0, y=300)
        # entrys
        self.ent1 = CTkEntry(self.update_frame, width=30)
        self.ent1.place(x=180, y=140)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = CTkEntry(self.update_frame, width=30)
        self.ent2.place(x=180, y=180)
        self.ent2.insert(END, str(self.age))

        self.ent3 = CTkEntry(self.update_frame, width=30)
        self.ent3.place(x=180, y=220)
        self.ent3.insert(END, str(self.gender))

        self.ent4 = CTkEntry(self.update_frame, width=30)
        self.ent4.place(x=180, y=260)
        self.ent4.insert(END, str(self.location))

        self.ent5 = CTkEntry(self.update_frame, width=30)
        self.ent5.place(x=180, y=300)
        self.ent5.insert(END, str(self.phone))
        # buttons for update and delete
        self.update = CTkButton(self.update_frame, text="Update", font=('arial', 12), width=10, height=1,
                                command=self.update2)
        self.update.place(x=25, y=340)
        self.update_frame.pack()

    def update2(self):

        # declaring the variables to update
        self.var1 = self.ent1.get()
        self.var2 = self.ent2.get()
        self.var3 = self.ent3.get()
        self.var4 = self.ent4.get()
        self.var5 = self.ent5.get()

        query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=? WHERE id LIKE ?"
        self.c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var5, self.id_net.get(),))
        self.conn.commit()
        tkinter.messagebox.showinfo("Updated", "Successfully Updated.")
        self.update_frame.destroy()
        self.__init__(self.window)
        self.updatee()
        self.update_frame.pack()

    def deletee(self):

        self.main.destroy()
        self.show_details_frame.destroy()
        self.update_frame.destroy()
        self.delete_frame.destroy()
        self.__init__(self.window)

        self.id = CTkLabel(self.delete_frame, text="Search Appoinment Number To Delete", font=('arial', 12))
        self.id.place(x=0, y=12)
        self.id_net = CTkEntry(self.delete_frame, width=30)
        self.id_net.place(x=230, y=18)
        self.search = CTkButton(self.delete_frame, text="Search", font=('arial', 12), width=10, height=1,
                                command=self.delete1)
        self.search.place(x=160, y=50)
        self.delete_frame.pack(fill='both', expand=True)

    def delete1(self):
        self.input = self.id_net.get()
        # execute sql
        sql = "SELECT * FROM appointments WHERE id LIKE ?"
        self.res = self.c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.phone = self.row[5]
        # creating the update form
        self.uname = CTkLabel(self.delete_frame, text="Patient's Name", font=('arial', 14))
        self.uname.place(x=0, y=140)

        self.patiant_age = CTkLabel(self.delete_frame, text="Age", font=('arial', 14))
        self.patiant_age.place(x=0, y=180)

        self.patiant_gender = CTkLabel(self.delete_frame, text="Gender", font=('arial', 14))
        self.patiant_gender.place(x=0, y=220)

        self.patiant_location = CTkLabel(self.delete_frame, text="Location", font=('arial', 14))
        self.patiant_location.place(x=0, y=260)

        self.patiant_phone = CTkLabel(self.delete_frame, text="Phone Number", font=('arial', 14))
        self.patiant_phone.place(x=0, y=300)
        # entrys
        self.ent1 = CTkEntry(self.delete_frame, width=80)
        self.ent1.place(x=180, y=140)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = CTkEntry(self.delete_frame, width=80)
        self.ent2.place(x=180, y=180)
        self.ent2.insert(END, str(self.age))

        self.ent3 = CTkEntry(self.delete_frame, width=80)
        self.ent3.place(x=180, y=220)
        self.ent3.insert(END, str(self.gender))

        self.ent4 = CTkEntry(self.delete_frame, width=80)
        self.ent4.place(x=180, y=260)
        self.ent4.insert(END, str(self.location))

        self.ent5 = CTkEntry(self.delete_frame, width=80)
        self.ent5.place(x=180, y=300)
        self.ent5.insert(END, str(self.phone))
        # buttons for update and delete
        self.update = CTkButton(self.delete_frame, text="Delete", font=('arial', 12), width=10, height=1,
                                command=self.delete2)
        self.update.place(x=25, y=340)
        self.delete_frame.pack()

    def delete2(self):
        sql2 = "DELETE FROM appointments WHERE id LIKE ?"
        self.c.execute(sql2, (self.id_net.get(),))
        self.conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.delete_frame.destroy()
        self.__init__(self.window)
        self.deletee()
        self.delete_frame.pack()


def menubar():
    main_menu = Menu()
    window.config(menu=main_menu)
    file_menu = Menu(main_menu, tearoff=False)
    main_menu.add_cascade(label="Menu", menu=file_menu)
    file_menu.add_command(label="Home", command=b.homee)
    file_menu.add_command(label="Show details", command=b.show_details)
    file_menu.add_command(label="Update", command=b.updatee)
    file_menu.add_command(label="Delete", command=b.deletee)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)

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