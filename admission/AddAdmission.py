import tkinter

import mysql.connector
import re
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry

class AddAdmission:
    def __init__(self):
        print("Admission frame")
        self.addAdmission_frame = tk.Toplevel()
        self.addAdmission_frame.title("Admission")
        self.BASE_DIR = "C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase"
        text_font = ("Times", "24")
        title_font = ("Times", "44")
        width = self.addAdmission_frame.winfo_screenwidth()
        height = self.addAdmission_frame.winfo_screenheight()

        self.addAdmission_frame.geometry("%dx%d" % (width, height))
        self.addAdmission_frame.config(background="white")
        self.image = Image.open(self.BASE_DIR + "/res/docBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.admission_window = tk.Label(self.addAdmission_frame, image=self.background_image, justify='center')
        self.admission_window.place(relwidth=1, relheight=1)

        self.addAdmission_window = tk.Label(self.admission_window, bg="white", justify='center')
        self.addAdmission_window.pack(fill='both', anchor='c', padx='15px', pady='15px')

        self.title_frame = tk.Frame(self.addAdmission_window, bg='white')  # admissionID
        self.title_frame.pack(fill='both', padx=15, pady=15)

        self.first_frame = tk.Frame(self.addAdmission_window,bg='white')  # admissionID
        self.first_frame.pack(fill='both', padx=15, pady=15)

        self.second_frame = tk.Frame(self.addAdmission_window,bg='white')  # admissionDate
        self.second_frame.pack(fill='both', padx=15, pady=15)

        self.first_frame = tk.Frame(self.addAdmission_window,bg='white')  # patientid
        self.first_frame.pack(fill='both', padx=15, pady=15)

        self.third_frame = tk.Frame(self.addAdmission_window,bg='white')  # patientid
        self.third_frame.pack(fill='both', padx=15, pady=15)

        self.fourth_frame = tk.Frame(self.addAdmission_window,bg='white')  # patientFirstName
        self.fourth_frame.pack(fill='both', padx=15, pady=15)

        self.fifth_frame = tk.Frame(self.addAdmission_window,bg='white')  # patientFirstName
        self.fifth_frame.pack(fill='both', padx=15, pady=15)

        self.sixth_frame = tk.Frame(self.addAdmission_window,bg='white')  # patientFirstName
        self.sixth_frame.pack(fill='both', padx=15, pady=15)

        self.admission_title = tk.Label(self.title_frame, text="Admission",bg='white')
        self.admission_title.config(font=title_font)
        self.admission_title.pack(side='left', padx=15, pady=15)



        # Create and pack the widgets for patientID
        self.admissionID_label = tk.Label(self.first_frame, text="Admission ID",bg='white')
        self.admissionID_entry = tk.Entry(self.first_frame, justify='left')
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
        self.Admittime_entry = tk.Entry(self.second_frame,justify="left")
        self.Admittime_label.config(font=text_font)
        self.Admittime_entry.config(font=text_font)
        self.Admittime_label.pack(side='left', padx=15, pady=15)
        self.Admittime_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.patientID_label = tk.Label(self.first_frame, text="Patient ID",bg='white')
        self.patientID_entry = tk.Entry(self.first_frame, justify='left')
        self.patientID_label.config(font=text_font)
        self.patientID_entry.config(font=text_font)
        self.patientID_label.pack(side='left', padx=15, pady=15)
        self.patientID_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.admitStaffID_label = tk.Label(self.fifth_frame, text="admitted By StaffID",bg='white')
        self.admitStaffID_entry = tk.Entry(self.fifth_frame, justify='left')
        self.admitStaffID_label.config(font=text_font)
        self.admitStaffID_entry.config(font=text_font)
        self.admitStaffID_label.pack(side='left', padx=15, pady=15)
        self.admitStaffID_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.wardNum_label = tk.Label(self.third_frame, text="Ward Number",bg='white')
        self.wardNum_entry = tk.Entry(self.third_frame, justify='left')
        self.wardNum_label.config(font=text_font)
        self.wardNum_entry.config(font=text_font)
        self.wardNum_label.pack(side='left', padx=15, pady=15)
        self.wardNum_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.roomNum_label = tk.Label(self.third_frame, text="Room Number",bg='white')
        self.roomNum_entry = tk.Entry(self.third_frame, justify='left')
        self.roomNum_label.config(font=text_font)
        self.roomNum_entry.config(font=text_font)
        self.roomNum_label.pack(side='left', padx=15, pady=15)
        self.roomNum_entry.pack(side='left', padx=15, pady=15)

        self.dischargeDate_label = tk.Label(self.fourth_frame, text="Discharge Date",bg='white')
        self.dischargeDate_entry = DateEntry(self.fourth_frame, width=12, background='black', foreground='white')
        self.dischargeDate_label.config(font =text_font)
        self.dischargeDate_entry.config(font=text_font)
        self.dischargeDate_label.pack(side='left', padx=15, pady=15)
        self.dischargeDate_entry.pack(side='left', padx=15, pady=15)

        self.dischargeTime_label = tk.Label(self.fourth_frame, text="Discharge Time",bg='white')
        self.dischargeTime_entry = tk.Entry(self.fourth_frame, justify="left")
        self.dischargeTime_label.config(font=text_font)
        self.dischargeTime_entry.config(font=text_font)
        self.dischargeTime_label.pack(side='left', padx=15, pady=15)
        self.dischargeTime_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.dischargeStaffID_label = tk.Label(self.fifth_frame, text="Discharged Staff ID",bg='white')
        self.dischargeStaffID_entry = tk.Entry(self.fifth_frame, justify='left')
        self.dischargeStaffID_label.config(font=text_font)
        self.dischargeStaffID_entry.config(font=text_font)
        self.dischargeStaffID_label.pack(side='left', padx=15, pady=15)
        self.dischargeStaffID_entry.pack(side='left', padx=15, pady=15)

        self.admissionCost_label = tk.Label(self.sixth_frame, text="Admission Cost",bg='white')
        self.admissionCost_entry = tk.Entry(self.sixth_frame, justify='left')
        self.admissionCost_label.config(font=text_font)
        self.admissionCost_entry.config(font=text_font)
        self.admissionCost_label.pack(side='left', padx=15, pady=15)
        self.admissionCost_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.compute_button = tk.Button(self.sixth_frame, text='Add Patient', command=self.addAdmission,bg='#74d4cc')
        self.compute_button.config(font=text_font)
        self.compute_button.pack(side='right', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.back_button = tk.Button(self.sixth_frame, text='Back', command=self.back, bg="#74d4cc",)
        self.back_button.config(font=text_font)
        self.back_button.pack(side='right', padx=15, pady=15)

        self.title_frame.pack()
        self.first_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        self.fourth_frame.pack()
        self.fifth_frame.pack()
        self.sixth_frame.pack()
        self.addAdmission_window.mainloop()

    def back(self):
        self.addAdmission_frame.destroy()

    def addAdmission(self):
        print("added Appointment")
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
            command = "INSERT INTO admission VALUES ('" + admission_id + "','" + admittedDate + "','" + admittedTime + "','" \
                      + patient_id + "','" \
                      + staffAdmittedID + "','" \
                      + wardNum + "','" \
                      + roomNum + "','" \
                      + dischargedDate + "','" \
                      + dischargedTime + "','" \
                      + dischargedStaffID + "','" \
                      + admissionCost + "')"
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