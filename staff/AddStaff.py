import mysql.connector
import re
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry


class AddStaff:
    def __init__(self):
        print("Staff frame")
        self.addStaff_window = tk.Tk()
        self.addStaff_window.title("Staff")


        self.StaffID_frame = tk.Frame(self.addStaff_window)  # Staffid
        self.StaffID_frame.pack(fill='both', padx=15, pady=15)

        self.firstName_frame = tk.Frame(self.addStaff_window)  # StaffFirstName
        self.firstName_frame.pack(fill='both', padx=15, pady=15)

        self.lastName_frame = tk.Frame(self.addStaff_window)  # StaffSecondName
        self.lastName_frame.pack(fill='both', padx=15, pady=15)

        self.dateOfBirth_frame = tk.Frame(self.addStaff_window)  # dateOfBirth
        self.dateOfBirth_frame.pack(fill='both', padx=15, pady=15)

        self.gender_frame = tk.Frame(self.addStaff_window)  # gender
        self.gender_frame.pack(fill='both', padx=15, pady=15)

        self.phone_frame = tk.Frame(self.addStaff_window)  # phone
        self.phone_frame.pack(fill='both', padx=15, pady=15)

        self.address_frame = tk.Frame(self.addStaff_window)  # address
        self.address_frame.pack(fill='both', padx=15, pady=15)

        self.button_frame = tk.Frame(self.addStaff_window)
        self.button_frame.pack(fill='both', padx=15, pady=15)

        self.StaffGender_frame = tk.Frame(self.addStaff_window)
        self.StaffGender_frame.pack(fill='both', padx=15, pady=15)



        # Create and pack the widgets for StaffID
        self.StaffID_label = tk.Label(self.StaffID_frame, text="Staff ID")
        self.StaffID_entry = tk.Entry(self.StaffID_frame, justify='left')
        self.StaffID_label.pack(side='left', padx=15, pady=15)
        self.StaffID_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for StaffName
        self.firstName_label = tk.Label(self.firstName_frame, text="First Name")
        self.firstName_entry = tk.Entry(self.firstName_frame, justify='left')
        self.firstName_label.pack(side='left', padx=15, pady=15)
        self.firstName_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for StaffName
        self.lastName_label = tk.Label(self.lastName_frame, text="Last Name")
        self.lastName_entry = tk.Entry(self.lastName_frame, justify='left')
        self.lastName_label.pack(side='left', padx=15, pady=15)
        self.lastName_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for dateOfBirth
        self.dateOfBirth_label = tk.Label(self.dateOfBirth_frame, text="Date Of Birth")
        self.dateOfBirth_entry = DateEntry(self.dateOfBirth_frame, width=12, background='black',foreground='white', borderwidth=2)
        #self.dateOfBirth_entry = tk.Entry(self.dateOfBirth_frame, justify='left')
        self.dateOfBirth_label.pack(side='left', padx=15, pady=15)
        self.dateOfBirth_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for gender
        self.gender_label = tk.Label(self.gender_frame, text="Gender")
        self.gender_entry = tk.Entry(self.gender_frame, justify='left')
        self.gender_label.pack(side='left', padx=15, pady=15)
        self.gender_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for phone
        self.phone_label = tk.Label(self.phone_frame, text="Phone Number")
        self.phone_entry = tk.Entry(self.phone_frame, justify='left')
        self.phone_label.pack(side='left', padx=15, pady=15)
        self.phone_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for address
        self.address_label = tk.Label(self.address_frame, text="Address")
        self.address_entry = tk.Entry(self.address_frame, justify='left')
        self.address_label.pack(side='left', padx=15, pady=15)
        self.address_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.compute_button = tk.Button(self.button_frame, text='Add Staff', command=self.addStaff)
        self.compute_button.pack(side='left', padx=15, pady=15)

        self.StaffID_frame.pack()
        self.firstName_frame.pack()
        self.lastName_frame.pack()
        self.dateOfBirth_frame.pack()
        self.gender_frame.pack()
        self.phone_frame.pack()
        self.address_frame.pack()
        self.button_frame.pack()
        self.addStaff_window.mainloop()

    def addStaff(self):
        print("added Appointment")
        Staff_id = self.StaffID_entry.get()
        firstName = self.firstName_entry.get()
        lastName = self.lastName_entry.get()
        dob = self.dateOfBirth_entry.get()
        gender = self.gender_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()

        print(Staff_id, firstName, lastName, dob, gender,phone,address)

        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor()
        if all([Staff_id, firstName, lastName, dob, gender,phone,address]) != None:
            command = "INSERT INTO staff VALUES ('" + Staff_id + "','" + firstName + "','" + lastName + "','" \
                      + dob + "','" \
                      + gender + "','" \
                      + phone + "','" \
                      + address + "')"
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