import tkinter

import mysql.connector
import re
import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry

class SearchAppointment:
    def __init__(self, *args):
        self.appointmentID = args[0]
        print("Appointment frame")

        self.BASE_DIR = "C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase"
        text_font = ("Times", "24")
        title_font = ("Times", "44")

        self.patientID = args[0]
        self.search_appt_frame = tk.Toplevel()
        self.search_appt_frame.title("Edit Patient Details")
        width = self.search_appt_frame.winfo_screenwidth()
        height = self.search_appt_frame.winfo_screenheight()

        self.search_appt_frame.geometry("%dx%d" % (width, height))
        self.search_appt_frame.config(background="white")
        self.image = Image.open(self.BASE_DIR + "/res/docBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.searchAppt_window = tk.Label(self.search_appt_frame, image=self.background_image, justify='center')
        self.searchAppt_window.place(relwidth=1, relheight=1)

        self.searchAppoint_window = tk.Frame(self.searchAppt_window, bg="white")
        self.searchAppoint_window.pack(fill='both', anchor='w', padx=300, pady=50)
        self.search_appt_frame.title("Appointment")

        self.AppointmentTitle_frame = tk.Frame(self.searchAppoint_window,bg='white')  # admissionID
        self.AppointmentTitle_frame.pack(fill='both')

        self.AppointmentId_frame = tk.Frame(self.searchAppoint_window,bg='white')  # admissionID
        self.AppointmentId_frame.pack(fill='both')

        self.patientId_frame = tk.Frame(self.searchAppoint_window,bg='white')  # admissionDate
        self.patientId_frame.pack(fill='both')

        self.apptStaffId_frame = tk.Frame(self.searchAppoint_window,bg='white')  # patientid
        self.apptStaffId_frame.pack(fill='both')

        self.apptDate_frame = tk.Frame(self.searchAppoint_window,bg='white')  # patientid
        self.apptDate_frame.pack(fill='both')

        self.apptTime_Frame = tk.Frame(self.searchAppoint_window,bg='white')  # patientFirstName
        self.apptTime_Frame.pack(fill='both')

        self.apptCost_Frame = tk.Frame(self.searchAppoint_window,bg='white')  # patientFirstName
        self.apptCost_Frame.pack(fill='both')

        self.apptButton_Frame = tk.Frame(self.searchAppoint_window,bg='white')  # patientFirstName
        self.apptButton_Frame.pack(fill='both')

        self.ApptTitle = tk.Label(self.AppointmentTitle_frame,text="Appointment",bg="white")
        self.ApptTitle.config(font=title_font)
        self.ApptTitle.pack(fill='both', anchor='c')

        # Create and pack the widgets for patientID
        self.apptID_label = tk.Label(self.AppointmentId_frame, text="Appointment ID",bg='white')
        self.apptID_value = tk.Label(self.AppointmentId_frame, justify='left',bg='white')
        self.apptID_label.config(font=text_font)
        self.apptID_value.config(font=text_font)
        self.apptID_label.pack(side='left', padx=15, pady=15)
        self.apptID_value.pack(side='left', padx=15, pady=15)

        self.apptdate_label = tk.Label(self.apptDate_frame, text="Appointment Date",bg='white')
        self.apptdate_value = tk.Label(self.apptDate_frame,bg='white')
        self.apptdate_label.config(font=text_font)
        self.apptdate_value.config(font=text_font)
        self.apptdate_label.pack(side='left', padx=15, pady=15)
        self.apptdate_value.pack(side='left', padx=15, pady=15)

        self.apptTime_label = tk.Label(self.apptTime_Frame, text="Appointment Time",bg='white')
        self.apptTime_value = tk.Label(self.apptTime_Frame,justify="left",bg='white')
        self.apptTime_label.config(font=text_font)
        self.apptTime_value.config(font=text_font)
        self.apptTime_label.pack(side='left', padx=15, pady=15)
        self.apptTime_value.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.patientID_label = tk.Label(self.patientId_frame, text="Patient ID",bg='white')
        self.patientID_value = tk.Label(self.patientId_frame, justify='left',bg='white')
        self.patientID_label.config(font=text_font)
        self.patientID_value.config(font=text_font)
        self.patientID_label.pack(side='left', padx=15, pady=15)
        self.patientID_value.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.apptStaffID_label = tk.Label(self.apptStaffId_frame, text="appointed to StaffID",bg='white')
        self.apptStaffID_value = tk.Label(self.apptStaffId_frame, justify='left',bg='white')
        self.apptStaffID_label.config(font=text_font)
        self.apptStaffID_value.config(font=text_font)
        self.apptStaffID_label.pack(side='left', padx=15, pady=15)
        self.apptStaffID_value.pack(side='left', padx=15, pady=15)


        self.apptCost_label = tk.Label(self.apptCost_Frame, text="Appointment Cost",bg='white')
        self.apptCost_value = tk.Label(self.apptCost_Frame, justify='left',bg='white')
        self.apptCost_label.config(font=text_font)
        self.apptCost_value.config(font=text_font)
        self.apptCost_label.pack(side='left', padx=15, pady=15)
        self.apptCost_value.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.compute_button = tk.Button(self.apptButton_Frame, text='Delete', bg="#74d4cc",command=self.deleteAppointment)
        self.compute_button.config(font=text_font)
        self.compute_button.pack(side='right', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.back_button = tk.Button(self.apptButton_Frame, text='Back', command=self.back, bg="#74d4cc")
        self.back_button.config(font=text_font)
        self.back_button.pack(side='right', padx=15, pady=15)

        y = str(self.appointmentID)

        print(y)
        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor(buffered=True)
        mycursor.execute("use PMS")

        command = "SELECT * FROM appointment WHERE appointmentID = '" + y + "';"
        print(command)
        try:
            mycursor.execute(command)
            for i in mycursor:
                print(type(i))
                print("-------------------------------------------")
                print("item", i)
                print(i[0])
                self.apptID_value.configure(text=i[0])
                print(i[1])
                self.patientID_value.configure(text=i[1])
                print(i[2])
                self.apptStaffID_value.configure(text=i[2])
                print(i[3])
                self.apptdate_value.configure(text=i[3])
                print(i[4])
                self.apptTime_value.configure(text=i[4])
                print(i[5])
                self.apptCost_value.configure(text=i[5])

                print("*******************************************")

                db.commit()

        except Exception as e:
            tkinter.messagebox.showinfo("Sorry", "Didn't find the data for given ID")
            print("issue is with", e)
        else:
            print("got details")

        self.AppointmentId_frame.pack()
        self.patientId_frame.pack()
        self.apptStaffId_frame.pack()
        self.apptDate_frame.pack()
        self.apptTime_Frame.pack()
        self.apptCost_Frame.pack()
        self.searchAppoint_window.mainloop()

    def back(self):
        self.search_appt_frame.destroy()
    def deleteAppointment(self):
        print("Delete Appointment")

        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor()
        command = "DELETE FROM appointment WHERE appointmentID = '" + self.appointmentID + "';"

        print(command)
        try:
            mycursor.execute(command)
            db.commit()
        except Exception as e:
            tkinter.messagebox.showinfo("Sorry", "Cannot delete the data")
            print("issue is with", e)
        else:
            tkinter.messagebox.showinfo("Successfully", "Deleted")
            print("deleted data")
            db.close()
