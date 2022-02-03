import tkinter

import mysql.connector
import re
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry


class EditPatient():

    def __init__(self,*args):
        print("patient frame")
        self.BASE_DIR = "C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase"
        text_font = ("Times", "24")
        title_font = ("Times", "44")

        self.patientID = args[0]
        self.edit_patient_frame = tk.Toplevel()
        self.edit_patient_frame.title("Edit Patient Details")
        width = self.edit_patient_frame.winfo_screenwidth()
        height = self.edit_patient_frame.winfo_screenheight()

        self.edit_patient_frame.geometry("%dx%d" % (width, height))
        self.edit_patient_frame.config(background="white")
        self.image = Image.open(self.BASE_DIR + "/res/docBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.one_frame = tk.Label(self.edit_patient_frame, image=self.background_image, justify='center')
        self.one_frame.place(relwidth=1, relheight=1)

        self.edit_patient_window = tk.Label(self.one_frame, justify='center')
        self.edit_patient_window.pack(fill='both',anchor='w',padx=300,pady=50)

        self.patientInfoTitle = tk.Frame(self.edit_patient_window, bg="white")  # patientInformation
        self.patientInfoTitle.pack(fill='both',anchor='w')

        self.patientID_frame = tk.Frame(self.edit_patient_window,bg="white")  # patientid
        self.patientID_frame.pack(fill='both',anchor='w')

        self.firstName_frame = tk.Frame(self.edit_patient_window,bg="white")  # patientFirstName
        self.firstName_frame.pack(fill='both',anchor='w')

        self.lastName_frame = tk.Frame(self.edit_patient_window,bg="white")  # patientSecondName
        self.lastName_frame.pack(fill='both',anchor='w')

        self.dateOfBirth_frame = tk.Frame(self.edit_patient_window,bg="white")  # dateOfBirth
        self.dateOfBirth_frame.pack(fill='both',anchor='w')

        self.gender_frame = tk.Frame(self.edit_patient_window,bg="white")  # gender
        self.gender_frame.pack(fill='both',anchor='w')

        self.phone_frame = tk.Frame(self.edit_patient_window,bg="white")  # phone
        self.phone_frame.pack(fill='both',anchor='w')

        self.address_frame = tk.Frame(self.edit_patient_window,bg="white")  # address
        self.address_frame.pack(fill='both',anchor='w')

        self.save_frame = tk.Frame(self.edit_patient_window, bg="white")  # address
        self.save_frame.pack(fill='both',anchor='w')


        self.patientInfo_label = tk.Label(self.patientInfoTitle, text="Edit Patient Information", bg="white")
        self.patientInfo_label.config(font=title_font)
        self.patientInfo_label.pack(anchor='c',padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.patientID_label = tk.Label(self.patientID_frame, text="Patient ID",bg="white")
        self.patientIDEntry = tk.Label(self.patientID_frame, justify='left',bg="white")
        self.patientID_label.config(font=text_font)
        self.patientIDEntry.config(font=text_font)
        self.patientID_label.pack(side='left', padx=15, pady=15)
        self.patientIDEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientName
        self.firstName_label = tk.Label(self.firstName_frame, text="First Name",bg="white")
        self.firstNameEntry = tk.Entry(self.firstName_frame, justify='left',bg="white")
        self.firstName_label.config(font=text_font)
        self.firstNameEntry.config(font=text_font)
        self.firstName_label.pack(side='left', padx=15, pady=15)
        self.firstNameEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientName
        self.lastName_label = tk.Label(self.lastName_frame, text="Last Name",bg="white")
        self.lastNameEntry = tk.Entry(self.lastName_frame, justify='left',bg="white")
        self.lastName_label.config(font=text_font)
        self.lastNameEntry.config(font=text_font)
        self.lastName_label.pack(side='left', padx=15, pady=15)
        self.lastNameEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for dateOfBirth
        self.dateOfBirth_label = tk.Label(self.dateOfBirth_frame, text="Date Of Birth",bg="white")
        self.dateOfBirthEntry = tk.Entry(self.dateOfBirth_frame, justify='left',bg="white")
        self.dateOfBirth_label.config(font=text_font)
        self.dateOfBirthEntry.config(font=text_font)
        self.dateOfBirth_label.pack(side='left', padx=15, pady=15)
        self.dateOfBirthEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for gender
        self.gender_label = tk.Label(self.gender_frame, text="Gender",bg="white")
        self.genderEntry = tk.Entry(self.gender_frame, justify='left',bg="white")
        self.gender_label.config(font=text_font)
        self.genderEntry.config(font=text_font)
        self.gender_label.pack(side='left', padx=15, pady=15)
        self.genderEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for phone
        self.phone_label = tk.Label(self.phone_frame, text="Phone Number",bg="white")
        self.phoneEntry = tk.Entry(self.phone_frame, justify='left',bg="white")
        self.phone_label.config(font=text_font)
        self.phoneEntry.config(font=text_font)
        self.phone_label.pack(side='left', padx=15, pady=15)
        self.phoneEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for address
        self.address_label = tk.Label(self.address_frame, text="Address",bg="white")
        self.addressEntry = tk.Entry(self.address_frame, justify='left',bg="white")
        self.address_label.config(font=text_font)
        self.addressEntry.config(font=text_font)
        self.address_label.pack(side='left', padx=15, pady=15)
        self.addressEntry.pack(side='left', padx=15, pady=15)

        self.save_btn = tk.Button(self.save_frame,text="Save",bg="#74d4cc",command=self.saveChanges)
        self.save_btn.config(font=text_font)
        self.save_btn.pack(side='right', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.back_button = tk.Button(self.save_frame, text='Back', command=self.back, bg="#74d4cc")
        self.back_button.config(font=text_font)
        self.back_button.pack(side='right', padx=15, pady=15)


        self.patientInfoTitle.pack()
        self.patientID_frame.pack()
        self.firstName_frame.pack()
        self.lastName_frame.pack()
        self.dateOfBirth_frame.pack()
        self.gender_frame.pack()
        self.phone_frame.pack()
        self.address_frame.pack()


        y = str(self.patientID)

        print(y)
        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor(buffered=True)
        mycursor.execute("use PMS")

        command = "SELECT * FROM patient WHERE patientID = '" + y + "';"
        print(command)
        try:
            mycursor.execute(command)
            for i in mycursor:
                print(type(i))
                print("-------------------------------------------")
                print("item",i)
                print(i[0])
                self.patientIDEntry.configure(text=i[0])
                print(i[1])
                self.firstNameEntry.insert(0,i[1])
                print(i[2])
                self.lastNameEntry.insert(0,i[2])
                print(i[3])
                self.dateOfBirthEntry.insert(0,i[3])
                print(i[4])
                self.genderEntry.insert(0,i[4])
                print(i[5])
                self.phoneEntry.insert(0,i[5])
                print(i[6])
                self.addressEntry.insert(0,i[6])
                print("*******************************************")

                details = []
                print(', '.join(i))
                db.commit()

        except Exception as e:
            tkinter.messagebox.showinfo("Sorry", "Didn't find the data for given ID")
            print("issue is with",e)
        else:
            print("got details")
    def back(self):
        self.edit_patient_frame.destroy()
    def saveChanges(self):
        print("added Appointment")
        patient_id = self.patientIDEntry.cget("text")
        firstName = self.firstNameEntry.get()
        lastName = self.lastNameEntry.get()
        dob = self.dateOfBirthEntry.get()
        gender = self.genderEntry.get()
        phone = self.phoneEntry.get()
        address = self.addressEntry.get()

        print(patient_id, firstName, lastName, dob, gender, phone, address)

        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor()
        if all([patient_id, firstName, lastName, dob, gender, phone, address]) != None:
            command = "UPDATE patient SET firstName='" + firstName + "',lastName='" + \
                      lastName + "',dateOfBirth='" + dob + "',gender='" + gender + "',phone='" \
                      + phone + "',address='" \
                      + address + "' WHERE patientID='"+patient_id+"';"
            print(command)
            try:
                mycursor.execute(command)
                db.commit()
            except Exception as e:
                print("issue is with", e)
                tkinter.messagebox.showinfo("Sorry", "Couldn't make update")

            else:
                print("inserted data")
                tkinter.messagebox.showinfo("Successfully", "Updated")
                db.close()
        else:
            print("null values are there")
