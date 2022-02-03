import tkinter

import mysql.connector
import tkinter as tk
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry




class AddPatient:
    def __init__(self):
        print("patient frame")
        self.BASE_DIR = "C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase"
        text_font = ("Times", "24")
        title_font = ("Times", "44")
        self.patient_frame = tk.Toplevel()
        self.patient_frame.title("Add Patient")
        width = self.patient_frame.winfo_screenwidth()
        height = self.patient_frame.winfo_screenheight()

        self.patient_frame.geometry("%dx%d" % (width, height))
        self.patient_frame.config(background="white")
        self.image = Image.open(self.BASE_DIR + "/res/docBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.addPatient_frame = tk.Label(self.patient_frame, image=self.background_image, justify='center')
        self.addPatient_frame.place(relwidth=1, relheight=1)

        self.addPatient_window = tk.Label(self.addPatient_frame, bg="white", justify='center')
        self.addPatient_window.pack(fill='both',anchor='c',padx='300px',pady='50px')

        self.patientTitle_label = tk.Label(self.addPatient_window, text="Add Patient", bg="white")
        self.patientTitle_label.config(font=title_font)
        self.patientTitle_label.pack(side=tk.TOP, anchor='c', padx=15, pady=15)

        self.patientID_frame = tk.Frame(self.addPatient_window,bg="white")  # patientid
        self.patientID_frame.pack(fill='both',anchor='c')

        self.firstName_frame = tk.Frame(self.addPatient_window,bg="white")  # patientFirstName
        self.firstName_frame.pack(fill='both',anchor='c')

        self.lastName_frame = tk.Frame(self.addPatient_window,bg="white")  # patientSecondName
        self.lastName_frame.pack(fill='both',anchor='c')

        self.dateOfBirth_frame = tk.Frame(self.addPatient_window,bg="white")  # dateOfBirth
        self.dateOfBirth_frame.pack(fill='both',anchor='c')

        self.gender_frame = tk.Frame(self.addPatient_window,bg="white")  # gender
        self.gender_frame.pack(fill='both',anchor='c')

        self.phone_frame = tk.Frame(self.addPatient_window,bg="white")  # phone
        self.phone_frame.pack(fill='both',anchor='c')

        self.address_frame = tk.Frame(self.addPatient_window,bg="white")  # address
        self.address_frame.pack(fill='both',anchor='c')

        self.button_frame = tk.Frame(self.addPatient_window,bg="white")
        self.button_frame.pack(fill='both',anchor='c')


        # Create and pack the widgets for patientID
        self.patientID_label = tk.Label(self.patientID_frame, text="Patient ID",bg="white")
        self.patientID_entry = tk.Entry(self.patientID_frame, justify='left',bg="white")
        self.patientID_label.config(font=text_font)
        self.patientID_entry.config(font=text_font)
        self.patientID_label.pack(fill='both',side='left', padx=15, pady=15)
        self.patientID_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientName
        self.firstName_label = tk.Label(self.firstName_frame, text="First Name",bg="white")
        self.firstName_entry = tk.Entry(self.firstName_frame, justify='left',bg="white")
        self.firstName_label.config(font=text_font)
        self.firstName_entry.config(font=text_font)
        self.firstName_label.pack(side='left', padx=15, pady=15)
        self.firstName_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientName
        self.lastName_label = tk.Label(self.lastName_frame, text="Last Name",bg="white")
        self.lastName_entry = tk.Entry(self.lastName_frame, justify='left',bg="white")
        self.lastName_label.config(font=text_font)
        self.lastName_entry.config(font=text_font)
        self.lastName_label.pack(side='left', padx=15, pady=15)
        self.lastName_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for dateOfBirth
        self.dateOfBirth_label = tk.Label(self.dateOfBirth_frame, text="Date Of Birth",bg="white")
        self.dateOfBirth_entry = DateEntry(self.dateOfBirth_frame, width=12, background='black',foreground='white', borderwidth=2)
        #self.dateOfBirth_entry = tk.Entry(self.dateOfBirth_frame, justify='left')
        self.dateOfBirth_label.config(font=text_font)
        self.dateOfBirth_entry.config(font=text_font)
        self.dateOfBirth_label.pack(side='left', padx=15, pady=15)
        self.dateOfBirth_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for gender
        self.gender_label = tk.Label(self.gender_frame, text="Gender",bg="white")
        self.gender_entry = tk.Entry(self.gender_frame, justify='left',bg="white")
        self.gender_label.config(font=text_font)
        self.gender_entry.config(font=text_font)
        self.gender_label.pack(side='left', padx=15, pady=15)
        self.gender_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for phone
        self.phone_label = tk.Label(self.phone_frame, text="Phone Number",bg="white")
        self.phone_entry = tk.Entry(self.phone_frame, justify='left',bg="white")
        self.phone_label.config(font=text_font)
        self.phone_entry.config(font=text_font)
        self.phone_label.pack(side='left', padx=15, pady=15)
        self.phone_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for address
        self.address_label = tk.Label(self.address_frame, text="Address",bg="white")
        self.address_entry = tk.Entry(self.address_frame, justify='left',bg="white")
        self.address_label.config(font=text_font)
        self.address_entry.config(font=text_font)
        self.address_label.pack(side='left', padx=15, pady=15)
        self.address_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.compute_button = tk.Button(self.button_frame, text='Add Patient', command=self.addPatient,bg="#74d4cc")
        self.compute_button.config(font=text_font)
        self.compute_button.pack(side='right', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.back_button = tk.Button(self.button_frame, text='Back', command=self.back, bg="#74d4cc")
        self.back_button.config(font=text_font)
        self.back_button.pack(side='right', padx=15, pady=15)

        self.patientID_frame.pack()
        self.firstName_frame.pack()
        self.lastName_frame.pack()
        self.dateOfBirth_frame.pack()
        self.gender_frame.pack()
        self.phone_frame.pack()
        self.address_frame.pack()
        self.button_frame.pack()
        self.addPatient_window.mainloop()
    def back(self):
        self.patient_frame.destroy()

    def addPatient(self):
        print("added Appointment")
        patient_id = self.patientID_entry.get()
        firstName = self.firstName_entry.get()
        lastName = self.lastName_entry.get()
        dob = self.dateOfBirth_entry.get()
        gender = self.gender_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()

        print(patient_id, firstName, lastName, dob, gender,phone,address)

        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor()
        if all([patient_id, firstName, lastName, dob, gender,phone,address]) != None:

            command = "INSERT INTO patient VALUES ('" + patient_id + "','" + firstName + "','" + lastName + "','" \
                      + dob + "','" \
                      + gender + "','" \
                      + phone + "','" \
                      + address + "')"
            print(command)
            try:
                mycursor.execute(command)
                db.commit()
            except Exception as e:
                tkinter.messagebox.showinfo("Sorry", "Please enter the Values")
                print("issue is with", e)
            else:
                print("inserted data")
                tkinter.messagebox.showinfo("Sucessfully", "Added Data")
                db.close()
        else:
            print("null values are there")