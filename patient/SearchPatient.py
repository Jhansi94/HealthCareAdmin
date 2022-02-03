import tkinter

import mysql.connector
import re
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry

class SearchPatient():

    def __init__(self,*args):
        print("patient frame")
        self.BASE_DIR = "C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase"
        text_font = ("Times", "24")
        title_font = ("Times", "44")

        self.patientID = args[0]
        self.search_patient_frame = tk.Toplevel()
        self.search_patient_frame.title("Edit Patient Details")
        width = self.search_patient_frame.winfo_screenwidth()
        height = self.search_patient_frame.winfo_screenheight()

        self.search_patient_frame.geometry("%dx%d" % (width, height))
        self.search_patient_frame.config(background="white")
        self.image = Image.open(self.BASE_DIR + "/res/docBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.patientDetail_window = tk.Label(self.search_patient_frame, image=self.background_image, justify='center')
        self.patientDetail_window.place(relwidth=1, relheight=1)


        self.info_frame = tk.Frame(self.patientDetail_window,bg="white")
        self.info_frame.pack(fill='both', anchor='w', padx=300, pady=50)

        self.patientInfoTitle = tk.Frame(self.info_frame, bg="white")  # patientInformation
        self.patientInfoTitle.pack(fill='both',anchor='w')

        self.patientID_frame = tk.Frame(self.info_frame,bg="white")  # patientid
        self.patientID_frame.pack(fill='both',anchor='w')

        self.firstName_frame = tk.Frame(self.info_frame,bg="white")  # patientFirstName
        self.firstName_frame.pack(fill='both',anchor='w')

        self.lastName_frame = tk.Frame(self.info_frame,bg="white")  # patientSecondName
        self.lastName_frame.pack(fill='both',anchor='w')

        self.dateOfBirth_frame = tk.Frame(self.info_frame,bg="white")  # dateOfBirth
        self.dateOfBirth_frame.pack(fill='both',anchor='w')

        self.gender_frame = tk.Frame(self.info_frame,bg="white")  # gender
        self.gender_frame.pack(fill='both',anchor='w')

        self.phone_frame = tk.Frame(self.info_frame,bg="white")  # phone
        self.phone_frame.pack(fill='both',anchor='w')

        self.address_frame = tk.Frame(self.info_frame,bg="white")  # address
        self.address_frame.pack(fill='both',anchor='w')


        self.deleteFrame = tk.Frame(self.info_frame,bg="white")
        self.deleteFrame.pack(fill='both',anchor='w')

        self.patientInfo_label = tk.Label(self.patientInfoTitle, text="Patient Information", bg="white")
        self.patientInfo_label.config(font=title_font)
        self.patientInfo_label.pack(anchor='c', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.patientID_label = tk.Label(self.patientID_frame, text="Patient ID",bg="white")
        self.patientIDValue_label = tk.Label(self.patientID_frame, justify='left',bg="white")
        self.patientID_label.config(font=text_font)
        self.patientIDValue_label.config(font=text_font)
        self.patientID_label.pack(side='left', padx=15, pady=15)
        self.patientIDValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientName
        self.firstName_label = tk.Label(self.firstName_frame, text="First Name",bg="white")
        self.firstNameValue_label = tk.Label(self.firstName_frame, justify='left',bg="white")
        self.firstName_label.config(font=text_font)
        self.firstNameValue_label.config(font=text_font)
        self.firstName_label.pack(side='left', padx=15, pady=15)
        self.firstNameValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientName
        self.lastName_label = tk.Label(self.lastName_frame, text="Last Name",bg="white")
        self.lastNameValue_label = tk.Label(self.lastName_frame, justify='left',bg="white")
        self.lastName_label.config(font=text_font)
        self.lastNameValue_label.config(font=text_font)
        self.lastName_label.pack(side='left', padx=15, pady=15)
        self.lastNameValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for dateOfBirth
        self.dateOfBirth_label = tk.Label(self.dateOfBirth_frame, text="Date Of Birth",bg="white")
        self.dateOfBirthValue_label = tk.Label(self.dateOfBirth_frame, justify='left',bg="white")
        self.dateOfBirth_label.config(font=text_font)
        self.dateOfBirthValue_label.config(font=text_font)
        self.dateOfBirth_label.pack(side='left', padx=15, pady=15)
        self.dateOfBirthValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for gender
        self.gender_label = tk.Label(self.gender_frame, text="Gender",bg="white")
        self.genderValue_label = tk.Label(self.gender_frame, justify='left',bg="white")
        self.gender_label.config(font=text_font)
        self.genderValue_label.config(font=text_font)
        self.gender_label.pack(side='left', padx=15, pady=15)
        self.genderValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for phone
        self.phone_label = tk.Label(self.phone_frame, text="Phone Number",bg="white")
        self.phoneValue_label = tk.Label(self.phone_frame, justify='left',bg="white")
        self.phone_label.config(font=text_font)
        self.phoneValue_label.config(font=text_font)
        self.phone_label.pack(side='left', padx=15, pady=15)
        self.phoneValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for address
        self.address_label = tk.Label(self.address_frame, text="Address",bg="white")
        self.addressValue_label = tk.Label(self.address_frame, justify='left',bg="white")
        self.address_label.config(font=text_font)
        self.addressValue_label.config(font=text_font)
        self.address_label.pack(side='left', padx=15, pady=15)
        self.addressValue_label.pack(side='left', padx=15, pady=15)

        self.delete_btn = tk.Button(self.deleteFrame, text="delete",justify='center', bg="#74d4cc",command=self.deleteRow)
        self.delete_btn.config(font=text_font)
        self.delete_btn.pack(side='right', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.back_button = tk.Button(self.deleteFrame, text='Back', command=self.back, bg="#74d4cc")
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
        self.deleteFrame.pack()


        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor(buffered=True)
        mycursor.execute("use PMS")

        command = "SELECT * FROM patient WHERE patientID = '" + self.patientID + "';"
        print(command)
        try:
            mycursor.execute(command)
            for i in mycursor:
                print(type(i))
                print("-------------------------------------------")
                print("item",i)
                print(i[0])
                self.patientIDValue_label.configure(text=i[0])
                print(i[1])
                self.firstNameValue_label.configure(text=i[1])
                print(i[2])
                self.lastNameValue_label.configure(text=i[2])
                print(i[3])
                self.dateOfBirthValue_label.configure(text=i[3])
                print(i[4])
                self.genderValue_label.configure(text=i[4])
                print(i[5])
                self.phoneValue_label.configure(text=i[5])
                print(i[6])
                self.addressValue_label.configure(text=i[6])
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
        self.search_patient_frame.destroy()
    def deleteRow(self):
        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor(buffered=True)
        mycursor.execute("use PMS")

        command = "DELETE FROM patient WHERE patientID = '" + self.patientID + "';"
        print(command)
        try:
            mycursor.execute(command)
            db.commit()

        except Exception as e:
            tkinter.messagebox.showinfo("Sorry", "Cannot delete the data")
            print("issue is with", e)
        else:
            tkinter.messagebox.showinfo("Successfully", "Deleted")

            print("deleted details")

    #print('All existing tables:', results)  # Returned as a list of tuples