import mysql.connector
import re
import tkinter as tk
from tkinter import ttk

class SearchStaff():

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


        self.deleteFrame = tk.Frame(self.info_frame,bg="white")
        self.deleteFrame.pack()

        self.staffInfo_label = tk.Label(self.staffInfoTitle, text="Staff Information", bg="white")
        self.staffInfo_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for staffID
        self.staffID_label = tk.Label(self.staffID_frame, text="Staff ID",bg="white")
        self.staffIDValue_label = tk.Label(self.staffID_frame, justify='left',bg="white")
        self.staffID_label.pack(side='left', padx=15, pady=15)
        self.staffIDValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for staffName
        self.firstName_label = tk.Label(self.firstName_frame, text="First Name",bg="white")
        self.firstNameValue_label = tk.Label(self.firstName_frame, justify='left',bg="white")
        self.firstName_label.pack(side='left', padx=15, pady=15)
        self.firstNameValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for staffName
        self.lastName_label = tk.Label(self.lastName_frame, text="Last Name",bg="white")
        self.lastNameValue_label = tk.Label(self.lastName_frame, justify='left',bg="white")
        self.lastName_label.pack(side='left', padx=15, pady=15)
        self.lastNameValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for dateOfBirth
        self.dateOfBirth_label = tk.Label(self.dateOfBirth_frame, text="Date Of Birth",bg="white")
        self.dateOfBirthValue_label = tk.Label(self.dateOfBirth_frame, justify='left',bg="white")
        self.dateOfBirth_label.pack(side='left', padx=15, pady=15)
        self.dateOfBirthValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for gender
        self.gender_label = tk.Label(self.gender_frame, text="Gender",bg="white")
        self.genderValue_label = tk.Label(self.gender_frame, justify='left',bg="white")
        self.gender_label.pack(side='left', padx=15, pady=15)
        self.genderValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for phone
        self.phone_label = tk.Label(self.phone_frame, text="Phone Number",bg="white")
        self.phoneValue_label = tk.Label(self.phone_frame, justify='left',bg="white")
        self.phone_label.pack(side='left', padx=15, pady=15)
        self.phoneValue_label.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for address
        self.address_label = tk.Label(self.address_frame, text="Address",bg="white")
        self.addressValue_label = tk.Label(self.address_frame, justify='left',bg="white")
        self.address_label.pack(side='left', padx=15, pady=15)
        self.addressValue_label.pack(side='left', padx=15, pady=15)

        self.delete_btn = tk.Button(self.deleteFrame, text="delete",justify='center', bg="white",command=self.deleteRow)
        self.delete_btn.pack(side='right', padx=15, pady=15)




        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor(buffered=True)
        mycursor.execute("use PMS")

        command = "SELECT * FROM staff WHERE staffID = '" + self.staffID + "';"
        print(command)
        try:
            mycursor.execute(command)
            for i in mycursor:
                print(type(i))
                print("-------------------------------------------")
                print("item",i)
                print(i[0])
                self.staffIDValue_label.configure(text=i[0])
                print(i[1])
                self.firstNameValue_label.configure(text=i[1])
                print(i[2])
                self.lastNameValue_label.configure(text=i[2])
                print(i[3])
                self.dateOfBirthValue_label.configure(text=i[3])
                print(i[4])
                self.genderValue_label.configure(text=i[4])
                print(i[5])
                self.phoneValue_label.configure(text=i[5])
                print(i[6])
                self.addressValue_label.configure(text=i[6])
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
        self.deleteFrame.pack()
        self.info_frame.mainloop()
    def deleteRow(self):
        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor(buffered=True)
        mycursor.execute("use PMS")

        command = "DELETE FROM staff WHERE staffID = '" + self.staffID + "';"
        print(command)
        try:
            mycursor.execute(command)
            db.commit()

        except Exception as e:
            print("issue is with", e)
        else:
            print("got details")

    #print('All existing tables:', results)  # Returned as a list of tuples