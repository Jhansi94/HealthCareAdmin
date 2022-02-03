import tkinter

import mysql.connector
import re
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry

class EditMedication():

    def __init__(self,*args):
        print("Medication frame")
        self.medicationID = args[0]

        self.BASE_DIR = "C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase"
        text_font = ("Times", "24")
        title_font = ("Times", "44")

        self.patientID = args[0]
        self.edit_medication_frame = tk.Toplevel()
        self.edit_medication_frame.title("Edit Patient Details")
        width = self.edit_medication_frame.winfo_screenwidth()
        height = self.edit_medication_frame.winfo_screenheight()

        self.edit_medication_frame.geometry("%dx%d" % (width, height))
        self.edit_medication_frame.config(background="white")
        self.image = Image.open(self.BASE_DIR + "/res/docBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.one_frame = tk.Label(self.edit_medication_frame, image=self.background_image, justify='center')
        self.one_frame.place(relwidth=1, relheight=1)

        self.medicationDetail_window = tk.Label(self.one_frame, justify='center',bg='white')
        self.medicationDetail_window.pack(fill='both', anchor='w', padx=300, pady=50)

        self.edit_medication_frame.title("Medication")

        self.info_frame = tk.Frame(self.medicationDetail_window,bg="white")
        self.info_frame.pack(fill='both')

        self.medicationInfoTitle = tk.Frame(self.info_frame, bg="white")  # medicationInformation
        self.medicationInfoTitle.pack(fill='both',anchor='c')

        self.medicationID_frame = tk.Frame(self.info_frame,bg="white")  # medicationid
        self.medicationID_frame.pack(fill='both')

        self.staﬀID_prescribedBy_frame = tk.Frame(self.info_frame,bg="white")  # medication staﬀID_prescribedBy
        self.staﬀID_prescribedBy_frame.pack(fill='both')

        self.patientID_frame = tk.Frame(self.info_frame,bg="white")  # medicationSecondName
        self.patientID_frame.pack(fill='both')

        self.medicationName_frame = tk.Frame(self.info_frame,bg="white")  # medicationName
        self.medicationName_frame.pack(fill='both')

        self.date_frame = tk.Frame(self.info_frame,bg="white")  # date
        self.date_frame.pack(fill='both')

        self.time_frame = tk.Frame(self.info_frame,bg="white")  # time
        self.time_frame.pack(fill='both')

        self. medicationCost_frame = tk.Frame(self.info_frame,bg="white")  #  medicationCost
        self. medicationCost_frame.pack(fill='both')

        self.save_frame = tk.Frame(self.info_frame, bg="white")  #  medicationCost
        self.save_frame.pack(fill='both')

        self.medicationdate_frame = tk.Frame(self.info_frame,bg="white")
        self.medicationdate_frame.pack()

        self.medicationInfo_label = tk.Label(self.medicationInfoTitle, text="Medication", bg="white")
        self.medicationInfo_label.config(font=title_font)
        self.medicationInfo_label.pack(side='left',anchor='c',padx=15, pady=15)

        # Create and pack the widgets for medicationID
        self.medicationID_label = tk.Label(self.medicationID_frame, text="Medication ID",bg="white")
        self.medicationIDValue = tk.Label(self.medicationID_frame, justify='left',bg="white")
        self.medicationID_label.config(font=text_font)
        self.medicationIDValue.config(font=text_font)
        self.medicationID_label.pack(side='left', padx=15, pady=15)
        self.medicationIDValue.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for medicationName
        self.staﬀID_prescribedBy_label = tk.Label(self.staﬀID_prescribedBy_frame, text="First Name",bg="white")
        self.staﬀID_prescribedByEntry = tk.Entry(self.staﬀID_prescribedBy_frame, justify='left',bg="white")
        self.staﬀID_prescribedBy_label.config(font=text_font)
        self.staﬀID_prescribedByEntry.config(font=text_font)
        self.staﬀID_prescribedBy_label.pack(side='left', padx=15, pady=15)
        self.staﬀID_prescribedByEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for medicationName
        self.patientID_label = tk.Label(self.patientID_frame, text="Last Name",bg="white")
        self.patientIDEntry = tk.Entry(self.patientID_frame, justify='left',bg="white")
        self.patientID_label.config(font=text_font)
        self.patientIDEntry.config(font=text_font)
        self.patientID_label.pack(side='left', padx=15, pady=15)
        self.patientIDEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for medicationName
        self.medicationName_label = tk.Label(self.medicationName_frame, text="Date Of Birth",bg="white")
        self.medicationNameEntry = tk.Entry(self.medicationName_frame, justify='left',bg="white")
        self.medicationName_label.config(font=text_font)
        self.medicationNameEntry.config(font=text_font)
        self.medicationName_label.pack(side='left', padx=15, pady=15)
        self.medicationNameEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for date
        self.date_label = tk.Label(self.date_frame, text="date",bg="white")
        self.dateEntry = tk.Entry(self.date_frame, justify='left',bg="white")
        self.date_label.config(font=text_font)
        self.dateEntry.config(font=text_font)
        self.date_label.pack(side='left', padx=15, pady=15)
        self.dateEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for time
        self.time_label = tk.Label(self.time_frame, text="Time",bg="white")
        self.timeEntry = tk.Entry(self.time_frame, justify='left',bg="white")
        self.time_label.config(font=text_font)
        self.timeEntry.config(font=text_font)
        self.time_label.pack(side='left', padx=15, pady=15)
        self.timeEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for  medicationCost
        self.medicationCost_label = tk.Label(self. medicationCost_frame, text="Medication Cost",bg="white")
        self.medicationCostEntry = tk.Entry(self. medicationCost_frame, justify='left',bg="white")
        self.medicationCost_label.config(font=text_font)
        self.medicationCostEntry.config(font=text_font)
        self.medicationCost_label.pack(side='left', padx=15, pady=15)
        self.medicationCostEntry.pack(side='left', padx=15, pady=15)

        self.save_btn = tk.Button(self.save_frame,text="Save",bg="#74d4cc",command=self.saveChanges)
        self.save_btn.config(font=text_font)
        self.save_btn.pack(side='right', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.back_button = tk.Button(self.save_frame, text='Back', command=self.back, bg="#74d4cc")
        self.back_button.config(font=text_font)
        self.back_button.pack(side='right', padx=15, pady=15)


        self.medicationInfoTitle.pack()
        self.medicationID_frame.pack()
        self.staﬀID_prescribedBy_frame.pack()
        self.patientID_frame.pack()
        self.medicationName_frame.pack()
        self.date_frame.pack()
        self.time_frame.pack()
        self.medicationCost_frame.pack()


        y = str(self.medicationID)

        print(y)
        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor(buffered=True)
        mycursor.execute("use PMS")
        #mycursor.execute("SHOW TABLES")
        #results = mycursor.fetchall()
        #for table in results:
            #tableName = re.sub("[(),']", '', str(table))

        command = "SELECT * FROM medication WHERE medicationID = '" + y + "';"
        print(command)
        try:
            mycursor.execute(command)
            for i in mycursor:
                print(type(i))
                print("-------------------------------------------")
                print("item",i)
                print(i[0])
                self.medicationIDValue.configure(text=i[0])
                print(i[1])
                self.staﬀID_prescribedByEntry.insert(0,i[1])
                print(i[2])
                self.patientIDEntry.insert(0,i[2])
                print(i[3])
                self.medicationNameEntry.insert(0,i[3])
                print(i[4])
                self.dateEntry.insert(0,i[4])
                print(i[5])
                self.timeEntry.insert(0,i[5])
                print(i[6])
                self. medicationCostEntry.insert(0,i[6])
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
        self.edit_medication_frame.destroy()
    def saveChanges(self):
        print("added Appointment")
        staﬀID_prescribedBy = self.staﬀID_prescribedByEntry.get()
        patientID = self.patientIDEntry.get()
        medicationName = self.medicationNameEntry.get()
        date = self.dateEntry.get()
        time = self.timeEntry.get()
        medicationCost = self. medicationCostEntry.get()

        print(self.medicationID, staﬀID_prescribedBy, patientID, medicationName, date, time,  medicationCost)

        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor()
        if all([staﬀID_prescribedBy, patientID, medicationName, date, time,  medicationCost]) != None:
            command = "UPDATE medication SET staﬀID_prescribedBy='" + staﬀID_prescribedBy + "',patientID='" + \
                      patientID + "',medicationName='" + medicationName + "',medicationName='" + date + "',time='" \
                      + time + "', medicationCost='" \
                      +  medicationCost + "' WHERE medicationID='"+self.medicationID+"';"
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
