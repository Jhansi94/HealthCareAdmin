import mysql.connector
import re
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry


class EditHealthService:
    def __init__(self, *args):
        self.serviceID = args[0]
        print("patient frame")
        self.editHealthService_window = tk.Tk()
        self.editHealthService_window.title("HealthService")

        self.serviceID_frame = tk.Frame(self.editHealthService_window)  # patientFirstName
        self.serviceID_frame.pack(fill='both', padx=15, pady=15)

        self.serviceType_frame = tk.Frame(self.editHealthService_window)  # patientFirstName
        self.serviceType_frame.pack(fill='both', padx=15, pady=15)

        self.patientID_frame = tk.Frame(self.editHealthService_window)  # patientid
        self.patientID_frame.pack(fill='both', padx=15, pady=15)

        self.serviceIssue_frame = tk.Frame(self.editHealthService_window)  # patientFirstName
        self.serviceIssue_frame.pack(fill='both', padx=15, pady=15)

        self.servicePerformed_frame = tk.Frame(self.editHealthService_window)  # patientFirstName
        self.servicePerformed_frame.pack(fill='both', padx=15, pady=15)

        self.serviceCost_frame = tk.Frame(self.editHealthService_window)  # patientFirstName
        self.serviceCost_frame.pack(fill='both', padx=15, pady=15)

        self.editService_frame = tk.Frame(self.editHealthService_window)  # patientFirstName
        self.editService_frame.pack(fill='both', padx=15, pady=15)

        # Create and pack the widgets for patientName
        self.serviceID_label = tk.Label(self.serviceID_frame, text="Service ID")
        self.serviceID_value = tk.Label(self.serviceID_frame, justify='left')
        self.serviceID_label.pack(side='left', padx=15, pady=15)
        self.serviceID_value.pack(side='left', padx=15, pady=15)

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
        self.serviceIssueID_entry = tk.Entry(self.serviceIssue_frame, justify='left')
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
        self.compute_button = tk.Button(self.editService_frame, text='Add HealthService', command=self.editService)
        self.compute_button.pack(side='left', padx=15, pady=15)

        y = str(self.serviceID)

        print(y)
        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor(buffered=True)
        mycursor.execute("use PMS")

        command = "SELECT * FROM healthservice WHERE serviceID = '" + y + "';"
        print(command)
        try:
            mycursor.execute(command)
            for i in mycursor:
                print(type(i))
                print("-------------------------------------------")
                print("item", i)
                print(i[0])
                self.serviceID_value.configure(text=i[0])
                print(i[1])
                self.serviceType_entry.insert(0, i[1])
                print(i[2])
                self.patientID_entry.insert(0, i[2])
                print(i[3])
                self.serviceIssueID_entry.insert(0, i[3])
                print(i[4])
                self.servicePerformedID_entry.insert(0, i[4])
                print(i[5])
                self.serviceCost_entry.insert(0, i[5])

                print("*******************************************")

                db.commit()

        except Exception as e:
            print("issue is with", e)
        else:
            print("got details")

        self.serviceID_frame.pack()
        self.serviceType_frame.pack()
        self.patientID_frame.pack()
        self.serviceIssue_frame.pack()
        self.servicePerformed_frame.pack()
        self.serviceCost_frame.pack()
        self.editService_frame.pack()

        self.editHealthService_window.mainloop()
    def editService(self):
        print("added Appointment")
        patient_id = self.patientID_entry.get()
        serviceType = self.serviceType_entry.get()
        issuedBy = self.serviceIssueID_entry.get()
        performedBy = self.servicePerformedID_entry.get()
        serviceCost = self.serviceCost_entry.get()

        y = str(self.serviceID)

        print(serviceType, patient_id, issuedBy,performedBy,serviceCost)

        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor()
        if all([serviceType, patient_id, issuedBy,performedBy,serviceCost]) != None:
            command = "UPDATE healthservice SET servicetype=" + serviceType + "',patientID='" + patient_id \
                      + "',serviceissuedby'" + issuedBy \
                      + "',serviceperformedby='" + performedBy \
                      + "',serviceBill='" + serviceCost \
                      + "' WHERE appointmentID='"+self.serviceID+"';"
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