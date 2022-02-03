import mysql.connector
import re
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry


class AddHealthService:
    def __init__(self):
        print("patient frame")
        self.addHealthService_window = tk.Tk()
        self.addHealthService_window.title("HealthService")

        self.serviceID_frame = tk.Frame(self.addHealthService_window)  # patientFirstName
        self.serviceID_frame.pack(fill='both', padx=15, pady=15)

        self.serviceType_frame = tk.Frame(self.addHealthService_window)  # patientFirstName
        self.serviceType_frame.pack(fill='both', padx=15, pady=15)

        self.patientID_frame = tk.Frame(self.addHealthService_window)  # patientid
        self.patientID_frame.pack(fill='both', padx=15, pady=15)

        self.serviceIssue_frame = tk.Frame(self.addHealthService_window)  # patientFirstName
        self.serviceIssue_frame.pack(fill='both', padx=15, pady=15)

        self.servicePerformed_frame = tk.Frame(self.addHealthService_window)  # patientFirstName
        self.servicePerformed_frame.pack(fill='both', padx=15, pady=15)

        self.serviceCost_frame = tk.Frame(self.addHealthService_window)  # patientFirstName
        self.serviceCost_frame.pack(fill='both', padx=15, pady=15)

        self.addService_frame = tk.Frame(self.addHealthService_window)  # patientFirstName
        self.addService_frame.pack(fill='both', padx=15, pady=15)

        # Create and pack the widgets for patientName
        self.serviceID_label = tk.Label(self.serviceID_frame, text="Service ID")
        self.serviceID_entry = tk.Entry(self.serviceID_frame, justify='left')
        self.serviceID_label.pack(side='left', padx=15, pady=15)
        self.serviceID_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientName
        self.serviceType_label = tk.Label(self.serviceType_frame, text="Service Type")
        self.serviceType_entry = tk.Entry(self.serviceType_frame, justify='left')
        self.serviceType_label.pack(side='left', padx=15, pady=15)
        self.serviceType_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.patientID_label = tk.Label(self.patientID_frame, text="Patient ID")
        self.patientID_entry = tk.Entry(self.patientID_frame, justify='left')
        self.patientID_label.pack(side='left', padx=15, pady=15)
        self.patientID_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.serviceIssueID_label = tk.Label(self.serviceIssue_frame, text="Service Issued By")
        self.serviceIssueID_entry = tk.Entry(self.patientID_frame, justify='left')
        self.serviceIssueID_label.pack(side='left', padx=15, pady=15)
        self.serviceIssueID_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.servicePerformedID_label = tk.Label(self.servicePerformed_frame, text="Service Performed By")
        self.servicePerformedID_entry = tk.Entry(self.servicePerformed_frame, justify='left')
        self.servicePerformedID_label.pack(side='left', padx=15, pady=15)
        self.servicePerformedID_entry.pack(side='left', padx=15, pady=15)


        # Create and pack the widgets for patientName
        self.serviceCost_label = tk.Label(self.serviceCost_frame, text="Service Cost")
        self.serviceCost_entry = tk.Entry(self.serviceCost_frame, justify='left')
        self.serviceCost_label.pack(side='left', padx=15, pady=15)
        self.serviceCost_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.compute_button = tk.Button(self.addService_frame, text='Add HealthService', command=self.addHealthService)
        self.compute_button.pack(side='left', padx=15, pady=15)

        self.serviceID_frame.pack()
        self.serviceType_frame.pack()
        self.patientID_frame.pack()
        self.serviceIssue_frame.pack()
        self.servicePerformed_frame.pack()
        self.serviceCost_frame.pack()
        self.addService_frame.pack()

        self.addHealthService_window.mainloop()

    def addHealthService(self):
        print("added Appointment")
        patient_id = self.patientID_entry.get()
        serviceId = self.serviceID_entry.get()
        serviceType = self.serviceType_entry.get()
        serviceIssued = self.serviceIssueID_entry.get()
        servicePerformed = self.servicePerformedID_entry.get()
        serviceCost = self.serviceCost_entry.get()


        print(serviceId, serviceType,patient_id,serviceIssued, servicePerformed, serviceCost)

        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor()
        if all([serviceId, serviceType,patient_id,serviceIssued, servicePerformed, serviceCost]) != None:
            command = "INSERT INTO healthservice VALUES ('" + serviceId + "','" + serviceType + "','" + patient_id + "','" \
                      + serviceIssued + "','" \
                      + servicePerformed + "','" \
                      + serviceCost + "')"
            print(command)
            try:
                mycursor.execute(command)
                db.commit()
            except Exception as e:
                print("issue is with", e)
            else:
                print("inserted data")
                db.close()
        else:
            print("null values are there")