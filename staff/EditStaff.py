import mysql.connector
import re
import tkinter as tk
from tkinter import ttk

class EditStaff():

    def __init__(self,*args):
        print("Staff frame")
        self.staffID = args[0]
        self.staffDetail_window = tk.Tk()
        self.staffDetail_window.title("Staff")

        self.info_frame = tk.Frame(self.staffDetail_window,bg="white")
        self.info_frame.pack()

        self.staffInfoTitle = tk.Frame(self.info_frame, bg="white")  # staffInformation
        self.staffInfoTitle.pack()

        self.staffID_frame = tk.Frame(self.info_frame,bg="white")  # staffid
        self.staffID_frame.pack()

        self.firstName_frame = tk.Frame(self.info_frame,bg="white")  # staffFirstName
        self.firstName_frame.pack()

        self.lastName_frame = tk.Frame(self.info_frame,bg="white")  # staffSecondName
        self.lastName_frame.pack()

        self.dateOfBirth_frame = tk.Frame(self.info_frame,bg="white")  # dateOfBirth
        self.dateOfBirth_frame.pack()

        self.gender_frame = tk.Frame(self.info_frame,bg="white")  # gender
        self.gender_frame.pack()

        self.phone_frame = tk.Frame(self.info_frame,bg="white")  # phone
        self.phone_frame.pack()

        self.address_frame = tk.Frame(self.info_frame,bg="white")  # address
        self.address_frame.pack()

        self.save_frame = tk.Frame(self.info_frame, bg="white")  # address
        self.save_frame.pack()

        self.StaffGender_frame = tk.Frame(self.info_frame,bg="white")
        self.StaffGender_frame.pack()

        self.StaffInfo_label = tk.Label(self.staffInfoTitle, text="Staff Information", bg="white")
        self.StaffInfo_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for staffID
        self.staffID_label = tk.Label(self.staffID_frame, text="Staff ID",bg="white")
        self.staffIDEntry = tk.Entry(self.staffID_frame, justify='left',bg="white")
        self.staffID_label.pack(side='left', padx=15, pady=15)
        self.staffIDEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for staffName
        self.firstName_label = tk.Label(self.firstName_frame, text="First Name",bg="white")
        self.firstNameEntry = tk.Entry(self.firstName_frame, justify='left',bg="white")
        self.firstName_label.pack(side='left', padx=15, pady=15)
        self.firstNameEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for staffName
        self.lastName_label = tk.Label(self.lastName_frame, text="Last Name",bg="white")
        self.lastNameEntry = tk.Entry(self.lastName_frame, justify='left',bg="white")
        self.lastName_label.pack(side='left', padx=15, pady=15)
        self.lastNameEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for dateOfBirth
        self.dateOfBirth_label = tk.Label(self.dateOfBirth_frame, text="Date Of Birth",bg="white")
        self.dateOfBirthEntry = tk.Entry(self.dateOfBirth_frame, justify='left',bg="white")
        self.dateOfBirth_label.pack(side='left', padx=15, pady=15)
        self.dateOfBirthEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for gender
        self.gender_label = tk.Label(self.gender_frame, text="Gender",bg="white")
        self.genderEntry = tk.Entry(self.gender_frame, justify='left',bg="white")
        self.gender_label.pack(side='left', padx=15, pady=15)
        self.genderEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for phone
        self.phone_label = tk.Label(self.phone_frame, text="Phone Number",bg="white")
        self.phoneEntry = tk.Entry(self.phone_frame, justify='left',bg="white")
        self.phone_label.pack(side='left', padx=15, pady=15)
        self.phoneEntry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for address
        self.address_label = tk.Label(self.address_frame, text="Address",bg="white")
        self.addressEntry = tk.Entry(self.address_frame, justify='left',bg="white")
        self.address_label.pack(side='left', padx=15, pady=15)
        self.addressEntry.pack(side='left', padx=15, pady=15)

        self.save_btn = tk.Button(self.save_frame,text="Save Changes",bg="white",command=self.saveChanges)
        self.save_btn.pack(side='right', padx=15, pady=15)


        y = str(self.staffID)

        print(y)
        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor(buffered=True)
        mycursor.execute("use PMS")

        command = "SELECT * FROM staff WHERE staffID = '" + self.staffID + "';"
        command = "SELECT * FROM appointment WHERE appointmentID = '" + y + "';"

        print(command)
        try:
            mycursor.execute(command)
            for i in mycursor:
                print(type(i))
                print("-------------------------------------------")
                print("item",i)
                print(i[0])
                self.staffIDEntry.insert(0,i[0])
                print(i[1])
                self.firstNameEntry.insert(0,i[1])
                print(i[2])
                self.lastNameEntry.insert(0,i[2])
                print(i[3])
                self.dateOfBirthEntry.insert(0,i[3])
                print(i[4])
                self.genderEntry.insert(0,i[4])
                print(i[5])
                self.phoneEntry.insert(0,i[5])
                print(i[6])
                self.addressEntry.insert(0,i[6])
                print("*******************************************")

                details = []
                print(', '.join(i))
                db.commit()

        except Exception as e:
            print("issue is with",e)
        else:
            print("got details")

        self.staffInfoTitle.pack()
        self.staffID_frame.pack()
        self.firstName_frame.pack()
        self.lastName_frame.pack()
        self.dateOfBirth_frame.pack()
        self.gender_frame.pack()
        self.phone_frame.pack()
        self.address_frame.pack()
        self.info_frame.mainloop()
    def saveChanges(self):
        print("added Appointment")
        staff_id = self.staffIDEntry.get()
        firstName = self.firstNameEntry.get()
        lastName = self.lastNameEntry.get()
        dob = self.dateOfBirthEntry.get()
        gender = self.genderEntry.get()
        phone = self.phoneEntry.get()
        address = self.addressEntry.get()

        print(staff_id, firstName, lastName, dob, gender, phone, address)

        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor()
        if all([staff_id, firstName, lastName, dob, gender, phone, address]) != None:
            command = "UPDATE staff SET firstName='" + firstName + "',lastName='" + \
                      lastName + "',dateOfBirth='" + dob + "',gender='" + gender + "',phone='" \
                      + phone + "',address='" \
                      + address + "' WHERE staffID='"+staff_id+"';"
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
