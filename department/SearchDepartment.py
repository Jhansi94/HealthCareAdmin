import tkinter

import mysql.connector
import re
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry

class SearchDepartment():

    def __init__(self,*args):
        print("Department frame")
        self.DepartmentID = args[0]

        self.BASE_DIR = "C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase"
        text_font = ("Times", "24")
        title_font = ("Times", "44")

        self.patientID = args[0]
        self.search_dept_frame = tk.Toplevel()
        self.search_dept_frame.title("Edit Patient Details")
        width = self.search_dept_frame.winfo_screenwidth()
        height = self.search_dept_frame.winfo_screenheight()

        self.search_dept_frame.geometry("%dx%d" % (width, height))
        self.search_dept_frame.config(background="white")
        self.image = Image.open(self.BASE_DIR + "/res/docBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.departmentDetail_window = tk.Label(self.search_dept_frame, image=self.background_image, justify='center')
        self.departmentDetail_window.place(relwidth=1, relheight=1)

        self.search_dept_frame.title("department")

        self.info_frame = tk.Frame(self.departmentDetail_window,bg="white")
        self.info_frame.pack(pady=100)

        self.departmentInfoTitle = tk.Frame(self.info_frame, bg="white")  # departmentInformation
        self.departmentInfoTitle.pack(fill='both')

        self.DepartmentID_frame = tk.Frame(self.info_frame,bg="white")  # Departmentid
        self.DepartmentID_frame.pack(fill='both')

        self.Name_frame = tk.Frame(self.info_frame,bg="white")  # departmentName
        self.Name_frame.pack(fill='both')

        self.numberStaff_frame = tk.Frame(self.info_frame,bg="white")  # departmentnumberStaff
        self.numberStaff_frame.pack(fill='both')

        self.location_frame = tk.Frame(self.info_frame,bg="white")  # location
        self.location_frame.pack(fill='both')

        self.deleteFrame = tk.Frame(self.info_frame,bg="white")
        self.deleteFrame.pack(fill='both')

        self.departmentInfo_label = tk.Label(self.departmentInfoTitle, text="Department", bg="white")
        self.departmentInfo_label.config(font=title_font)
        self.departmentInfo_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for DepartmentID
        self.DepartmentID_label = tk.Label(self.DepartmentID_frame, text="department ID",bg="white")
        self.DepartmentIDValue_label = tk.Label(self.DepartmentID_frame, justify='left',bg="white")
        self.DepartmentID_label.config(font=text_font)
        self.DepartmentIDValue_label.config(font=text_font)
        self.DepartmentID_label.pack(side='left', padx=15, pady=15)
        self.DepartmentIDValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for departmentName
        self.Name_label = tk.Label(self.Name_frame, text=" Name",bg="white")
        self.NameValue_label = tk.Label(self.Name_frame, justify='left',bg="white")
        self.Name_label.config(font=text_font)
        self.NameValue_label.config(font=text_font)
        self.Name_label.pack(side='left', padx=15, pady=15)
        self.NameValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for departmentName
        self.numberStaff_label = tk.Label(self.numberStaff_frame, text="Number of Staff",bg="white")
        self.numberStaffValue_label = tk.Label(self.numberStaff_frame, justify='left',bg="white")
        self.numberStaff_label.config(font=text_font)
        self.numberStaffValue_label.config(font=text_font)
        self.numberStaff_label.pack(side='left', padx=15, pady=15)
        self.numberStaffValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for location
        self.location_label = tk.Label(self.location_frame, text="Location",bg="white")
        self.locationValue_label = tk.Label(self.location_frame, justify='left',bg="white")
        self.location_label.config(font=text_font)
        self.locationValue_label.config(font=text_font)
        self.location_label.pack(side='left', padx=15, pady=15)
        self.locationValue_label.pack(side='left', padx=15, pady=15)

        self.delete_btn = tk.Button(self.deleteFrame, text="delete",justify='center', bg="#74d4cc",command=self.deleteRow)
        self.delete_btn.config(font=text_font)
        self.delete_btn.pack(side='right', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.back_button = tk.Button(self.deleteFrame, text='Back', command=self.back, bg="#74d4cc")
        self.back_button.config(font=text_font)
        self.back_button.pack(side='right', padx=15, pady=15)

        # Create and pack the widgets for the button widgets

        self.departmentInfoTitle.pack()
        self.DepartmentID_frame.pack()
        self.Name_frame.pack()
        self.numberStaff_frame.pack()
        self.location_frame.pack()
        self.deleteFrame.pack()


        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor(buffered=True)
        mycursor.execute("use PMS")

        command = "SELECT * FROM department WHERE DepartmentID = '" + self.DepartmentID + "';"
        print(command)
        try:
            mycursor.execute(command)
            for i in mycursor:
                print(type(i))
                print("-------------------------------------------")
                print("item",i)
                print(i[0])
                self.DepartmentIDValue_label.configure(text=i[0])
                print(i[1])
                self.NameValue_label.configure(text=i[1])
                print(i[2])
                self.numberStaffValue_label.configure(text=i[2])
                print(i[3])
                self.locationValue_label.configure(text=i[3])
                print("*******************************************")

                db.commit()

        except Exception as e:
            tkinter.messagebox.showinfo("Sorry", "Didn't find the data for given ID")
            print("issue is with",e)
        else:
            print("got details")

    def back(self):
        self.search_dept_frame.destroy()
    def deleteRow(self):
        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor(buffered=True)
        mycursor.execute("use PMS")

        command = "DELETE FROM department WHERE departmentID = '" + self.DepartmentID + "';"
        print(command)
        try:
            mycursor.execute(command)
            db.commit()

        except Exception as e:
            print("issue is with", e)
        else:
            print("got details")
