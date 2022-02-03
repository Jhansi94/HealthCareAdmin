import tkinter

import mysql.connector
import re
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry

class AddDepartment:
    def __init__(self):
        print("department frame")
        self.BASE_DIR = "C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase"
        text_font = ("Times", "24")
        title_font = ("Times", "44")

        self.add_department_frame = tk.Toplevel()
        self.add_department_frame.title("Add Department")
        width = self.add_department_frame.winfo_screenwidth()
        height = self.add_department_frame.winfo_screenheight()

        self.add_department_frame.geometry("%dx%d" % (width, height))
        self.add_department_frame.config(background="white")
        self.image = Image.open(self.BASE_DIR + "/res/docBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.patientDetail_window = tk.Label(self.add_department_frame, image=self.background_image, justify='center')
        self.patientDetail_window.place(relwidth=1, relheight=1)


        self.addDepartment_window = tk.Frame(self.patientDetail_window, bg="white")
        self.addDepartment_window.pack(fill='both', anchor='w', padx=300, pady=50)

        self.departmentTitle_frame = tk.Frame(self.patientDetail_window,bg="white")
        self.departmentTitle_frame.pack(fill='both',anchor='w',padx=15,pady=15)

        self.departmentID_frame = tk.Frame(self.addDepartment_window,bg="white")  # departmentID
        self.departmentID_frame.pack(fill='both', padx=15, pady=15)

        self.Name_frame = tk.Frame(self.addDepartment_window,bg="white")  # DepartmentName
        self.Name_frame.pack(fill='both', padx=15, pady=15)

        self.numberStaff_frame = tk.Frame(self.addDepartment_window,bg="white")  # Number of Staff
        self.numberStaff_frame.pack(fill='both', padx=15, pady=15)

        self.location_frame = tk.Frame(self.addDepartment_window,bg="white")  # location
        self.location_frame.pack(fill='both', padx=15, pady=15)

        self.button_frame = tk.Frame(self.addDepartment_window,bg="white")
        self.button_frame.pack(fill='both', padx=15, pady=15)

        # Create and pack the widgets for departmentID
        self.department_title = tk.Label(self.departmentID_frame, text="Department ID", bg="white")
        self.department_title.config(font=title_font)
        self.department_title.pack(anchor='c', padx=15, pady=15)

        # Create and pack the widgets for departmentID
        self.departmentID_label = tk.Label(self.departmentID_frame, text="Department ID",bg="white")
        self.departmentID_entry = tk.Entry(self.departmentID_frame, justify='left')
        self.departmentID_label.config(font=text_font)
        self.departmentID_entry.config(font=text_font)
        self.departmentID_label.pack(side='left', padx=15, pady=15)
        self.departmentID_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for StaffName
        self.Name_label = tk.Label(self.Name_frame, text=" Name",bg="white")
        self.Name_entry = tk.Entry(self.Name_frame, justify='left')
        self.Name_label.config(font=text_font)
        self.Name_entry.config(font=text_font)
        self.Name_label.pack(side='left', padx=15, pady=15)
        self.Name_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for StaffName
        self.numberStaff_label = tk.Label(self.numberStaff_frame, text="Number of Staff",bg="white")
        self.numberStaff_entry = tk.Entry(self.numberStaff_frame, justify='left')
        self.numberStaff_label.config(font=text_font)
        self.numberStaff_entry.config(font=text_font)
        self.numberStaff_label.pack(side='left', padx=15, pady=15)
        self.numberStaff_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for location
        self.location_label = tk.Label(self.location_frame, text="Location",bg="white")
        self.location_entry = DateEntry(self.location_frame, width=12, background='black',foreground='white', borderwidth=2)
        self.location_label.config(font=text_font)
        self.location_entry.config(font=text_font)
        self.location_label.pack(side='left', padx=15, pady=15)
        self.location_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.compute_button = tk.Button(self.button_frame, text='Add department', command=self.addDepartment,bg="#74d4cc")
        self.compute_button.config(font=text_font)
        self.compute_button.pack(side='right', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.back_button = tk.Button(self.button_frame, text='Back', command=self.back,bg="#74d4cc")
        self.back_button.config(font=text_font)
        self.back_button.pack(side='right', padx=15, pady=15)

        self.departmentID_frame.pack()
        self.Name_frame.pack()
        self.numberStaff_frame.pack()
        self.button_frame.pack()
        self.addDepartment_window.mainloop()
    def back(self):
        self.add_department_frame.destroy()

    def addDepartment(self):
        print("added Appointment")
        departmentID = self.departmentID_entry.get()
        Name = self.Name_entry.get()
        numberStaff = self.numberStaff_entry.get()
        location = self.location_entry.get()


        print(departmentID, Name, numberStaff, location)

        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor()
        if all([departmentID, Name, numberStaff, location]) != None:
            command = "INSERT INTO department VALUES ('" + departmentID + "','" + Name + "','" + numberStaff + "','" \
                      + location + "')"
            print(command)
            try:
                mycursor.execute(command)
                db.commit()
            except Exception as e:
                tkinter.messagebox.showinfo("Sorry", "Please enter the Values")
                print("issue is with", e)
            else:
                tkinter.messagebox.showinfo("Sucessfully", "Added Data")
                print("inserted data")
                db.close()
        else:
            print("null values are there")