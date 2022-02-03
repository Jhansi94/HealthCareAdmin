import tkinter

import mysql.connector
import re
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry


class SearchAdmission:
    def __init__(self,*args):
        self.givenAdmissionId = args[0]
        print("Admission frame")
        self.BASE_DIR = "C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase"
        text_font = ("Times", "24")
        title_font = ("Times", "44")

        self.patientID = args[0]
        self.search_admin_frame = tk.Toplevel()
        self.search_admin_frame.title("Edit Patient Details")
        width = self.search_admin_frame.winfo_screenwidth()
        height = self.search_admin_frame.winfo_screenheight()

        self.search_admin_frame.geometry("%dx%d" % (width, height))
        self.search_admin_frame.config(background="white")
        self.image = Image.open(self.BASE_DIR + "/res/docBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.one_frame = tk.Label(self.search_admin_frame, image=self.background_image, justify='center')
        self.one_frame.place(relwidth=1, relheight=1)

        self.searchAdmission_window = tk.Label(self.one_frame, justify='center', bg='white')
        self.searchAdmission_window.pack(fill='both', anchor='c', padx=15, pady=15)

        self.title_frame = tk.Frame(self.searchAdmission_window, bg='white')  # admissionID
        self.title_frame.pack(fill='both')

        self.first_frame = tk.Frame(self.searchAdmission_window, bg='white')  # admissionID
        self.first_frame.pack(fill='both', padx=15, pady=15)

        self.second_frame = tk.Frame(self.searchAdmission_window, bg='white')  # admissionDate
        self.second_frame.pack(fill='both', padx=15, pady=15)

        self.first_frame = tk.Frame(self.searchAdmission_window, bg='white')  # patientid
        self.first_frame.pack(fill='both', padx=15, pady=15)

        self.third_frame = tk.Frame(self.searchAdmission_window, bg='white')  # patientid
        self.third_frame.pack(fill='both', padx=15, pady=15)

        self.fourth_frame = tk.Frame(self.searchAdmission_window, bg='white')  # patientFirstName
        self.fourth_frame.pack(fill='both', padx=15, pady=15)

        self.fifth_frame = tk.Frame(self.searchAdmission_window, bg='white')  # patientFirstName
        self.fifth_frame.pack(fill='both', padx=15, pady=15)

        self.sixth_frame = tk.Frame(self.searchAdmission_window, bg='white')  # patientFirstName
        self.sixth_frame.pack(fill='both', padx=15, pady=15)

        self.admissionTitle = tk.Label(self.title_frame, text="Admission ID", bg='white')
        self.admissionTitle.config(font=title_font)
        self.admissionTitle.pack(anchor='c')

        # Create and pack the widgets for patientID
        self.admissionID_label = tk.Label(self.first_frame, text="Admission ID", bg='white')
        self.admissionID_value = tk.Label(self.first_frame, justify='left', bg='white')
        self.admissionID_label.config(font=text_font)
        self.admissionID_value.config(font=text_font)
        self.admissionID_label.pack(side='left', padx=15, pady=15)
        self.admissionID_value.pack(side='left', padx=15, pady=15)

        self.Admitdate_label = tk.Label(self.second_frame, text="Admitted Date", bg='white')
        self.Admitdate_value = tk.Label(self.second_frame, width=12, foreground='black',bg='white')
        self.Admitdate_label.config(font=text_font)
        self.Admitdate_value.config(font=text_font)
        self.Admitdate_label.pack(side='left', padx=15, pady=15)
        self.Admitdate_value.pack(side='left', padx=15, pady=15)

        self.Admittime_label = tk.Label(self.second_frame, text="Admitted Time", bg='white')
        self.Admittime_value = tk.Label(self.second_frame, justify="left", bg='white',fg='black')
        self.Admittime_label.config(font=text_font)
        self.Admittime_value.config(font=text_font)
        self.Admittime_label.pack(side='left', padx=15, pady=15)
        self.Admittime_value.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.patientID_label = tk.Label(self.first_frame, text="Patient ID", bg='white')
        self.patientID_value = tk.Label(self.first_frame, justify='left', bg='white')
        self.patientID_label.config(font=text_font)
        self.patientID_value.config(font=text_font)
        self.patientID_label.pack(side='left', padx=15, pady=15)
        self.patientID_value.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.admitStaffID_label = tk.Label(self.fifth_frame, text="admitted By StaffID", bg='white')
        self.admitStaffID_value = tk.Label(self.fifth_frame, justify='left', bg='white')
        self.admitStaffID_label.config(font=text_font)
        self.admitStaffID_value.config(font=text_font)
        self.admitStaffID_label.pack(side='left', padx=15, pady=15)
        self.admitStaffID_value.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.wardNum_label = tk.Label(self.third_frame, text="Ward Number", bg='white')
        self.wardNum_value = tk.Label(self.third_frame, justify='left', bg='white')
        self.wardNum_label.config(font=text_font)
        self.wardNum_value.config(font=text_font)
        self.wardNum_label.pack(side='left', padx=15, pady=15)
        self.wardNum_value.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.roomNum_label = tk.Label(self.third_frame, text="Room Number", bg='white')
        self.roomNum_value = tk.Label(self.third_frame, justify='left', bg='white')
        self.roomNum_label.config(font=text_font)
        self.roomNum_value.config(font=text_font)
        self.roomNum_label.pack(side='left', padx=15, pady=15)
        self.roomNum_value.pack(side='left', padx=15, pady=15)

        self.dischargeDate_label = tk.Label(self.fourth_frame, text="Discharge Date", bg='white')
        self.dischargeDate_value = tk.Label(self.fourth_frame, width=12, fg='black', bg='white')
        self.dischargeDate_label.config(font=text_font)
        self.dischargeDate_value.config(font=text_font)
        self.dischargeDate_label.pack(side='left', padx=15, pady=15)
        self.dischargeDate_value.pack(side='left', padx=15, pady=15)

        self.dischargeTime_label = tk.Label(self.fourth_frame, text="Discharge Time", bg='white')
        self.dischargeTime_value = tk.Label(self.fourth_frame, justify="left", bg='white')
        self.dischargeTime_label.config(font=text_font)
        self.dischargeTime_value.config(font=text_font)
        self.dischargeTime_label.pack(side='left', padx=15, pady=15)
        self.dischargeTime_value.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.dischargeStaffID_label = tk.Label(self.fifth_frame, text="Discharged Staff ID", bg='white')
        self.dischargeStaffID_value = tk.Label(self.fifth_frame, justify='left', bg='white')
        self.dischargeStaffID_label.config(font=text_font)
        self.dischargeStaffID_value.config(font=text_font)
        self.dischargeStaffID_label.pack(side='left', padx=15, pady=15)
        self.dischargeStaffID_value.pack(side='left', padx=15, pady=15)

        self.admissionCost_label = tk.Label(self.sixth_frame, text="Admission Cost", bg='white')
        self.admissionCost_value = tk.Label(self.sixth_frame, justify='left', bg='white')
        self.admissionCost_label.config(font=text_font)
        self.admissionCost_value.config(font=text_font)
        self.admissionCost_label.pack(side='left', padx=15, pady=15)
        self.admissionCost_value.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.compute_button = tk.Button(self.sixth_frame, text='Delete', bg="#74d4cc", command=self.deleteAdmission)
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
                self.admissionID_value.configure(text=i[0])
                print(i[1])
                self.Admitdate_value.configure(text=i[1])
                print(i[2])
                self.Admittime_value.configure(text=i[2])
                print(i[3])
                self.patientID_value.configure(text=i[3])
                print(i[4])
                self.admitStaffID_value.configure(text=i[4])
                print(i[5])
                self.wardNum_value.configure(text=i[5])
                print(i[6])
                self.roomNum_value.configure(text=i[6])
                print(i[7])
                self.dischargeDate_value.configure(text=i[7])
                print(i[8])
                self.dischargeTime_value.configure(text=i[8])
                print(i[9])
                self.dischargeStaffID_value.configure(text=i[9])
                print(i[10])
                self.admissionCost_value.configure(text=i[10])

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
        self.searchAdmission_window.mainloop()

    def back(self):
        self.search_admin_frame.destroy()

    def deleteAdmission(self):
        print("Delete Admission")

        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor()
        command = "DELETE FROM admission WHERE admissionId = '" + self.givenAdmissionId + "';"

        print(command)
        try:
            mycursor.execute(command)
            db.commit()
        except Exception as e:
            tkinter.messagebox.showinfo("Sorry", "Cannot delete the data")
            print("issue is with", e)
        else:
            print("deleted data")
            tkinter.messagebox.showinfo("Successfully", "Deleted")
            db.close()
