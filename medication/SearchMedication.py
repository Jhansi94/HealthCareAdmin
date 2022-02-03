import tkinter

import mysql.connector
import re
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry

class SearchMedication():

    def __init__(self,*args):
        print("Medication frame")
        self.medicationID = args[0]
        self.BASE_DIR = "C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase"
        text_font = ("Times", "24")
        title_font = ("Times", "44")

        self.patientID = args[0]
        self.search_medication_frame = tk.Toplevel()
        self.search_medication_frame.title("Edit Patient Details")
        width = self.search_medication_frame.winfo_screenwidth()
        height = self.search_medication_frame.winfo_screenheight()

        self.search_medication_frame.geometry("%dx%d" % (width, height))
        self.search_medication_frame.config(background="white")
        self.image = Image.open(self.BASE_DIR + "/res/docBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.medicationDetail_window = tk.Label(self.search_medication_frame, image=self.background_image, justify='center')
        self.medicationDetail_window.place(relwidth=1, relheight=1)

        self.search_medication_frame.title("Medication")

        self.info_frame = tk.Frame(self.medicationDetail_window,bg="white")
        self.info_frame.pack(fill='both',padx=100,pady=100)

        self.medicationInfoTitle = tk.Frame(self.info_frame, bg="white")  # medicationInformation
        self.medicationInfoTitle.pack(fill='both',anchor='c')

        self.medicarionID_frame = tk.Frame(self.info_frame,bg="white")  # medicarionid
        self.medicarionID_frame.pack(fill='both')

        self.staﬀID_prescribedBy_frame = tk.Frame(self.info_frame,bg="white")  # medicationstaﬀID_prescribedBy
        self.staﬀID_prescribedBy_frame.pack(fill='both')

        self.patientID_frame = tk.Frame(self.info_frame,bg="white")  # medication patientID
        self.patientID_frame.pack(fill='both')

        self.medicationName_frame = tk.Frame(self.info_frame,bg="white")  # medicationName
        self.medicationName_frame.pack(fill='both')

        self.date_frame = tk.Frame(self.info_frame,bg="white")  # date
        self.date_frame.pack(fill='both')

        self.time_frame = tk.Frame(self.info_frame,bg="white")  # time
        self.time_frame.pack(fill='both')

        self.medicationCost_frame = tk.Frame(self.info_frame,bg="white")  # medicationCost
        self.medicationCost_frame.pack(fill='both')
        
        self.deleteFrame = tk.Frame(self.info_frame,bg="white")
        self.deleteFrame.pack(fill='both')

        self.medicationInfo_label = tk.Label(self.medicationInfoTitle, text="Medication", bg="white")
        self.medicationInfo_label.config(font=title_font)
        self.medicationInfo_label.pack(anchor='c')

        # Create and pack the widgets for medicationID
        self.medicarionID_label = tk.Label(self.medicarionID_frame, text="Medication",bg="white")
        self.medicarionIDValue_label = tk.Label(self.medicarionID_frame, justify='left',bg="white")
        self.medicarionID_label.config(font=text_font)
        self.medicarionIDValue_label.config(font=text_font)
        self.medicarionID_label.pack(side='left', padx=15, pady=15)
        self.medicarionIDValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for medicationName
        self.staﬀID_prescribedBy_label = tk.Label(self.staﬀID_prescribedBy_frame, text="First Name",bg="white")
        self.staﬀID_prescribedByValue_label = tk.Label(self.staﬀID_prescribedBy_frame, justify='left',bg="white")
        self.staﬀID_prescribedBy_label.config(font=text_font)
        self.staﬀID_prescribedByValue_label.config(font=text_font)
        self.staﬀID_prescribedBy_label.pack(side='left', padx=15, pady=15)
        self.staﬀID_prescribedByValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for medicationName
        self.patientID_label = tk.Label(self.patientID_frame, text="Last Name",bg="white")
        self.patientIDValue_label = tk.Label(self.patientID_frame, justify='left',bg="white")
        self.patientID_label.config(font=text_font)
        self.patientIDValue_label.config(font=text_font)
        self.patientID_label.pack(side='left', padx=15, pady=15)
        self.patientIDValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for medicationName
        self.medicationName_label = tk.Label(self.medicationName_frame, text="Date Of Birth",bg="white")
        self.medicationNameValue_label = tk.Label(self.medicationName_frame, justify='left',bg="white")
        self.medicationName_label.config(font=text_font)
        self.medicationNameValue_label.config(font=text_font)
        self.medicationName_label.pack(side='left', padx=15, pady=15)
        self.medicationNameValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for date
        self.date_label = tk.Label(self.date_frame, text="date",bg="white")
        self.dateValue_label = tk.Label(self.date_frame, justify='left',bg="white")
        self.date_label.config(font=text_font)
        self.dateValue_label.config(font=text_font)
        self.date_label.pack(side='left', padx=15, pady=15)
        self.dateValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for time
        self.time_label = tk.Label(self.time_frame, text="time Number",bg="white")
        self.timeValue_label = tk.Label(self.time_frame, justify='left',bg="white")
        self.time_label.config(font=text_font)
        self.timeValue_label.config(font=text_font)
        self.time_label.pack(side='left', padx=15, pady=15)
        self.timeValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for medicationCost
        self.medicationCost_label = tk.Label(self.medicationCost_frame, text="medicationCost",bg="white")
        self.medicationCostValue_label = tk.Label(self.medicationCost_frame, justify='left',bg="white")
        self.medicationCost_label.config(font=text_font)
        self.medicationCostValue_label.config(font=text_font)
        self.medicationCost_label.pack(side='left', padx=15, pady=15)
        self.medicationCostValue_label.pack(side='left', padx=15, pady=15)

        self.delete_btn = tk.Button(self.deleteFrame, text="delete",justify='center', bg="#74d4cc",command=self.deleteRow)
        self.delete_btn.config(font=text_font)
        self.delete_btn.pack(side='right', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.back_button = tk.Button(self.deleteFrame, text='Back', command=self.back, bg="#74d4cc")
        self.back_button.config(font=text_font)
        self.back_button.pack(side='right', padx=15, pady=15)

        self.medicationInfoTitle.pack()
        self.medicarionID_frame.pack()
        self.staﬀID_prescribedBy_frame.pack()
        self.patientID_frame.pack()
        self.medicationName_frame.pack()
        self.date_frame.pack()
        self.time_frame.pack()
        self.medicationCost_frame.pack()
        self.deleteFrame.pack()


        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor(buffered=True)
        mycursor.execute("use PMS")

        command = "SELECT * FROM medication WHERE medicationID = '" + self.medicationID + "';"
        print(command)
        try:
            mycursor.execute(command)
            for i in mycursor:
                print(type(i))
                print("-------------------------------------------")
                print("item",i)
                print(i[0])
                self.medicarionIDValue_label.configure(text=i[0])
                print(i[1])
                self.staﬀID_prescribedByValue_label.configure(text=i[1])
                print(i[2])
                self.patientIDValue_label.configure(text=i[2])
                print(i[3])
                self.medicationNameValue_label.configure(text=i[3])
                print(i[4])
                self.dateValue_label.configure(text=i[4])
                print(i[5])
                self.timeValue_label.configure(text=i[5])
                print(i[6])
                self.medicationCostValue_label.configure(text=i[6])
                print("*******************************************")

                details = []
                print(', '.join(i))
                db.commit()

        except Exception as e:
            print("issue is with",e)
        else:
            print("got details")
    def back(self):
        self.search_medication_frame.destroy()
    def deleteRow(self):
        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor(buffered=True)
        mycursor.execute("use PMS")

        command = "DELETE FROM medication WHERE medicationID = '" + self.medicationID + "';"
        print(command)
        try:
            mycursor.execute(command)
            db.commit()

        except Exception as e:
            tkinter.messagebox.showinfo("Sorry", "Cannot delete the data")
            print("issue is with", e)
        else:
            tkinter.messagebox.showinfo("Successfully", "Deleted")
            print("got details")

    #print('All existing tables:', results)  # Returned as a list of tuples