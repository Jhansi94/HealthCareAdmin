import tkinter

import mysql.connector
import re
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry


class EditAdmission:
    def __init__(self,*args):
        self.givenAdmissionId = args[0]
        print("Admission frame")
        self.BASE_DIR = "C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase"
        text_font = ("Times", "24")
        title_font = ("Times", "44")

        self.patientID = args[0]
        self.edit_admin_frame = tk.Toplevel()
        self.edit_admin_frame.title("Edit Patient Details")
        width = self.edit_admin_frame.winfo_screenwidth()
        height = self.edit_admin_frame.winfo_screenheight()

        self.edit_admin_frame.geometry("%dx%d" % (width, height))
        self.edit_admin_frame.config(background="white")
        self.image = Image.open(self.BASE_DIR + "/res/docBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.one_frame = tk.Label(self.edit_admin_frame, image=self.background_image, justify='center')
        self.one_frame.place(relwidth=1, relheight=1)

        self.edit_admin_window = tk.Label(self.one_frame, justify='center',bg='white')
        self.edit_admin_window.pack(fill='both', anchor='c', padx=15, pady=15)

        self.title_frame = tk.Frame(self.edit_admin_window,bg='white')  # admissionID
        self.title_frame.pack(fill='both')

        self.first_frame = tk.Frame(self.edit_admin_window,bg='white')  # admissionID
        self.first_frame.pack(fill='both', padx=15, pady=15)

        self.second_frame = tk.Frame(self.edit_admin_window,bg='white')  # admissionDate
        self.second_frame.pack(fill='both', padx=15, pady=15)

        self.first_frame = tk.Frame(self.edit_admin_window,bg='white')  # patientid
        self.first_frame.pack(fill='both', padx=15, pady=15)

        self.third_frame = tk.Frame(self.edit_admin_window,bg='white')  # patientid
        self.third_frame.pack(fill='both', padx=15, pady=15)

        self.fourth_frame = tk.Frame(self.edit_admin_window,bg='white')  # patientFirstName
        self.fourth_frame.pack(fill='both', padx=15, pady=15)

        self.fifth_frame = tk.Frame(self.edit_admin_window,bg='white')  # patientFirstName
        self.fifth_frame.pack(fill='both', padx=15, pady=15)

        self.sixth_frame = tk.Frame(self.edit_admin_window,bg='white')  # patientFirstName
        self.sixth_frame.pack(fill='both', padx=15, pady=15)

        self.admissionTitle = tk.Label(self.title_frame, text="Admission ID",bg='white')
        self.admissionTitle.config(font=title_font)
        self.admissionTitle.pack(anchor='c')

        # Create and pack the widgets for patientID
        self.admissionID_label = tk.Label(self.first_frame, text="Admission ID",bg='white')
        self.admissionID_entry = tk.Entry(self.first_frame, justify='left',bg='white')
        self.admissionID_label.config(font=text_font)
        self.admissionID_entry.config(font=text_font)
        self.admissionID_label.pack(side='left', padx=15, pady=15)
        self.admissionID_entry.pack(side='left', padx=15, pady=15)

        self.Admitdate_label = tk.Label(self.second_frame, text="Admitted Date",bg='white')
        self.Admitdate_entry = DateEntry(self.second_frame, width=12, background='black', foreground='white')
        self.Admitdate_label.config(font=text_font)
        self.Admitdate_entry.config(font=text_font)
        self.Admitdate_label.pack(side='left', padx=15, pady=15)
        self.Admitdate_entry.pack(side='left', padx=15, pady=15)

        self.Admittime_label = tk.Label(self.second_frame, text="Admitted Time",bg='white')
        self.Admittime_entry = tk.Entry(self.second_frame,justify="left",bg='white')
        self.Admittime_label.config(font=text_font)
        self.Admittime_entry.config(font=text_font)
        self.Admittime_label.pack(side='left', padx=15, pady=15)
        self.Admittime_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.patientID_label = tk.Label(self.first_frame, text="Patient ID",bg='white')
        self.patientID_entry = tk.Entry(self.first_frame, justify='left',bg='white')
        self.patientID_label.config(font=text_font)
        self.patientID_entry.config(font=text_font)
        self.patientID_label.pack(side='left', padx=15, pady=15)
        self.patientID_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.admitStaffID_label = tk.Label(self.fifth_frame, text="admitted By StaffID",bg='white')
        self.admitStaffID_entry = tk.Entry(self.fifth_frame, justify='left',bg='white')
        self.admitStaffID_label.config(font=text_font)
        self.admitStaffID_entry.config(font=text_font)
        self.admitStaffID_label.pack(side='left', padx=15, pady=15)
        self.admitStaffID_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.wardNum_label = tk.Label(self.third_frame, text="Ward Number",bg='white')
        self.wardNum_entry = tk.Entry(self.third_frame, justify='left',bg='white')
        self.wardNum_label.config(font=text_font)
        self.wardNum_entry.config(font=text_font)
        self.wardNum_label.pack(side='left', padx=15, pady=15)
        self.wardNum_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.roomNum_label = tk.Label(self.third_frame, text="Room Number",bg='white')
        self.roomNum_entry = tk.Entry(self.third_frame, justify='left',bg='white')
        self.roomNum_label.config(font=text_font)
        self.roomNum_entry.config(font=text_font)
        self.roomNum_label.pack(side='left', padx=15, pady=15)
        self.roomNum_entry.pack(side='left', padx=15, pady=15)

        self.dischargeDate_label = tk.Label(self.fourth_frame, text="Discharge Date",bg='white')
        self.dischargeDate_entry = DateEntry(self.fourth_frame, width=12, background='black', foreground='white')
        self.dischargeDate_label.config(font=text_font)
        self.dischargeDate_entry.config(font=text_font)
        self.dischargeDate_label.pack(side='left', padx=15, pady=15)
        self.dischargeDate_entry.pack(side='left', padx=15, pady=15)

        self.dischargeTime_label = tk.Label(self.fourth_frame, text="Discharge Time",bg='white')
        self.dischargeTime_entry = tk.Entry(self.fourth_frame, justify="left",bg='white')
        self.dischargeTime_label.config(font=text_font)
        self.dischargeTime_entry.config(font=text_font)
        self.dischargeTime_label.pack(side='left', padx=15, pady=15)
        self.dischargeTime_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.dischargeStaffID_label = tk.Label(self.fifth_frame, text="Discharged Staff ID",bg='white')
        self.dischargeStaffID_entry = tk.Entry(self.fifth_frame, justify='left',bg='white')
        self.dischargeStaffID_label.config(font=text_font)
        self.dischargeStaffID_entry.config(font=text_font)
        self.dischargeStaffID_label.pack(side='left', padx=15, pady=15)
        self.dischargeStaffID_entry.pack(side='left', padx=15, pady=15)

        self.admissionCost_label = tk.Label(self.sixth_frame, text="Admission Cost",bg='white')
        self.admissionCost_entry = tk.Entry(self.sixth_frame, justify='left',bg='white')
        self.admissionCost_label.config(font=text_font)
        self.admissionCost_entry.config(font=text_font)
        self.admissionCost_label.pack(side='left', padx=15, pady=15)
        self.admissionCost_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.compute_button = tk.Button(self.sixth_frame, text='Add Patient',bg="#74d4cc",command=self.addAdmission)
        self.compute_button.config(font=text_font)
        self.compute_button.pack(side='right', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.back_button = tk.Button(self.sixth_frame, text='Back', command=self.back, bg="#74d4cc")
        self.back_button.config(font=text_font)
        self.back_button.pack(side='right', padx=15, pady=15)


        y = str(self.givenAdmissionId)

        print(y)
        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor(buffered=True)
        mycursor.execute("use PMS")

        command = "SELECT * FROM admission WHERE admissionId = '" + y + "';"
        print(command)
        try:
            mycursor.execute(command)
            for i in mycursor:
                print(type(i))
                print("-------------------------------------------")
                print("item", i)
                print(i[0])
                self.admissionID_entry.insert(0, i[0])
                print(i[1])
                self.Admitdate_entry.insert(0,'')
                self.Admitdate_entry.insert(0, i[1])
                print(i[2])
                self.Admittime_entry.insert(0, i[2])
                print(i[3])
                self.patientID_entry.insert(0, i[3])
                print(i[4])
                self.admitStaffID_entry.insert(0, i[4])
                print(i[5])
                self.wardNum_entry.insert(0, i[5])
                print(i[6])
                self.roomNum_entry.insert(0, i[6])
                print(i[7])
                self.dischargeDate_entry.insert(0,'')
                self.dischargeDate_entry.insert(0, i[7])
                print(i[8])
                self.dischargeTime_entry.insert(0, i[8])
                print(i[9])
                self.dischargeStaffID_entry.insert(0, i[9])
                print(i[10])
                self.admissionCost_entry.insert(0, i[10])

                print("*******************************************")

                details = []
                print(', '.join(i))
                db.commit()

        except Exception as e:
            tkinter.messagebox.showinfo("Sorry", "Didn't find the data for given ID")
            print("issue is with", e)
        else:
            print("got details")
        self.first_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        self.fourth_frame.pack()
        self.fifth_frame.pack()
        self.sixth_frame.pack()
        self.edit_admin_window.mainloop()

    def back(self):
        self.edit_admin_frame.destroy()

    def addAdmission(self):
        print("change Appointment")
        patient_id = self.patientID_entry.get()
        staffAdmittedID = self.admitStaffID_entry.get()
        admission_id = self.admissionID_entry.get()
        admittedDate = self.Admitdate_entry.get()
        admittedTime = self.Admittime_entry.get()
        wardNum = self.wardNum_entry.get()
        roomNum = self.roomNum_entry.get()
        dischargedDate = self.dischargeDate_entry.get()
        dischargedTime = self.dischargeTime_entry.get()
        dischargedStaffID = self.dischargeStaffID_entry.get()
        admissionCost = self.admissionCost_entry.get()

        print(patient_id, staffAdmittedID, admission_id, admittedDate, admittedTime,wardNum,roomNum,
              dischargedDate,dischargedTime,dischargedStaffID,admissionCost)

        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor()
        if all([patient_id, staffAdmittedID, admission_id, admittedDate, admittedTime,wardNum,roomNum,
              dischargedDate,dischargedTime,dischargedStaffID,admissionCost]) != None:
            command = "UPDATE admission SET dateAdmitted='" + admittedDate \
                      + "',timeAdmitted='" + admittedTime \
                      + "',patientID='" + patient_id \
                      + "',staﬀID_admittedBy='" + staffAdmittedID \
                      + "',wardNumber='" + wardNum \
                      + "',bedNumber='" + roomNum \
                      + "',dateDischarged='" + dischargedDate \
                      + "',timeDischarged='" + dischargedTime \
                      + "',staﬀID_dischargedBy='" + dischargedStaffID \
                      + "',admissionCost='" + admissionCost + "' WHERE admissionId='"+admission_id+"'"
            print(command)
            try:
                mycursor.execute(command)
                db.commit()
            except Exception as e:
                tkinter.messagebox.showinfo("Sorry", "Couldn't make update")
                print("issue is with", e)
            else:
                print("inserted data")
                tkinter.messagebox.showinfo("Successfully", "Updated")
                db.close()
        else:
            print("null values are there")