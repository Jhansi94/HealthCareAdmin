import tkinter

import mysql.connector
import re
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry

class Editdepartment():

    def __init__(self,*args):
        print("department frame")
        self.departmentID = args[0]
        self.BASE_DIR = "C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase"
        text_font = ("Times", "24")
        title_font = ("Times", "44")

        self.patientID = args[0]
        self.edit_department_frame = tk.Toplevel()
        self.edit_department_frame.title("Edit Patient Details")
        width = self.edit_department_frame.winfo_screenwidth()
        height = self.edit_department_frame.winfo_screenheight()

        self.edit_department_frame.geometry("%dx%d" % (width, height))
        self.edit_department_frame.config(background="white")
        self.image = Image.open(self.BASE_DIR + "/res/docBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.one_frame = tk.Label(self.edit_department_frame, image=self.background_image, justify='center')
        self.one_frame.place(relwidth=1, relheight=1)

        self.departmentDetail_window = tk.Label(self.one_frame, justify='center',bg='white')
        self.departmentDetail_window.pack(fill='both', anchor='w', padx=300, pady=50)

        self.edit_department_frame.title("department")


        self.info_frame = tk.Frame(self.departmentDetail_window,bg="white")
        self.info_frame.pack(side="left")

        self.departmentInfoTitle = tk.Frame(self.info_frame, bg="white")  # departmentInformation
        self.departmentInfoTitle.pack()

        self.departmentID_frame = tk.Frame(self.info_frame,bg="white")  # departmentid
        self.departmentID_frame.pack(anchor='w')

        self.Name_frame = tk.Frame(self.info_frame,bg="white")  # department Name
        self.Name_frame.pack(anchor='w')

        self.numberstaff_frame = tk.Frame(self.info_frame,bg="white")  # departmentnumberstaff
        self.numberstaff_frame.pack(anchor='w')

        self.location_frame = tk.Frame(self.info_frame,bg="white")  # location
        self.location_frame.pack(anchor='w')


        self.save_frame = tk.Frame(self.info_frame, bg="white")  #  departmentCost
        self.save_frame.pack()


        self.departmentTitle_label = tk.Label(self.departmentID_frame, text="Department ", bg="white")
        self.departmentTitle_label.config(font=title_font)
        self.departmentTitle_label.pack(anchor='c',padx=15, pady=15)

        # Create and pack the widgets for departmentID
        self.departmentID_label = tk.Label(self.departmentID_frame, text="department ID",bg="white")
        self.departmentIDEntry = tk.Label(self.departmentID_frame, justify='left',bg="white")
        self.departmentID_label.config(font=text_font)
        self.departmentIDEntry.config(font=text_font)
        self.departmentID_label.pack(side='left',anchor='w', padx=15, pady=15)
        self.departmentIDEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for location
        self.Name_label = tk.Label(self.Name_frame, text="First Name",bg="white")
        self.NameEntry = tk.Entry(self.Name_frame, justify='left',bg="white")
        self.Name_label.config(font=text_font)
        self.NameEntry.config(font=text_font)
        self.Name_label.pack(side='left', padx=15, pady=15)
        self.NameEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for location
        self.numberstaff_label = tk.Label(self.numberstaff_frame, text="Number of Staff",bg="white")
        self.numberstaffEntry = tk.Entry(self.numberstaff_frame, justify='left',bg="white")
        self.numberstaff_label.config(font=text_font)
        self.numberstaffEntry.config(font=text_font)
        self.numberstaff_label.pack(side='left', padx=15, pady=15)
        self.numberstaffEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for location
        self.location_label = tk.Label(self.location_frame, text="Location",bg="white")
        self.locationEntry = tk.Entry(self.location_frame, justify='left',bg="white")
        self.location_label.config(font=text_font)
        self.locationEntry.config(font=text_font)
        self.location_label.pack(side='left', padx=15, pady=15)
        self.locationEntry.pack(side='left', padx=15, pady=15)


        self.save_btn = tk.Button(self.save_frame,text="Save",bg="#74d4cc",command=self.saveChanges)
        self.save_btn.config(font=text_font)
        self.save_btn.pack(side='right', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.back_button = tk.Button(self.save_frame, text='Back', command=self.back, bg="#74d4cc")
        self.back_button.config(font=text_font)
        self.back_button.pack(side='right', padx=15, pady=15)


        self.departmentInfoTitle.pack()
        self.departmentID_frame.pack()
        self.Name_frame.pack()
        self.numberstaff_frame.pack()
        self.location_frame.pack()


        y = str(self.departmentID)

        print(y)
        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor(buffered=True)
        mycursor.execute("use PMS")

        command = "SELECT * FROM department WHERE departmentID = '" + y + "';"
        print(command)
        try:
            mycursor.execute(command)
            for i in mycursor:
                print(type(i))
                print("-------------------------------------------")
                print("item",i)
                print(i[0])
                self.departmentIDEntry.configure(text=i[0])
                print(i[1])
                self.NameEntry.insert(0,i[1])
                print(i[2])
                self.numberstaffEntry.insert(0,i[2])
                print(i[3])
                self.locationEntry.insert(0,i[3])
                print("*******************************************")

                db.commit()

        except Exception as e:
            tkinter.messagebox.showinfo("Sorry", "Didn't find the data for given ID")
            print("issue is with",e)
        else:
            print("got details")
    def back(self):
        self.edit_department_frame.destroy()
    def saveChanges(self):
        print("added Department")
        department_id = self.departmentIDEntry.get()
        Name = self.NameEntry.get()
        numberstaff = self.numberstaffEntry.get()
        location = self.locationEntry.get()

        print(department_id, Name, numberstaff, location)

        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor()
        if all([department_id, Name, numberstaff, location]) != None:
            command = "UPDATE department SET name='" + Name + "',numberStaﬀ='" + \
                      numberstaff + "',location='" + location + "' WHERE departmentID='" + department_id + "';"
            print(command)
            try:
                mycursor.execute(command)
                db.commit()
            except Exception as e:
                tkinter.messagebox.showinfo("Sorry", "Couldn't make update")
                print("issue is with", e)
            else:
                tkinter.messagebox.showinfo("Successfully", "Updated")
                print("inserted data")
                db.close()
        else:
            print("null values are there")
