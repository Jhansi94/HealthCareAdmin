import tkinter

import mysql.connector
import tkinter as tk
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry


class AddMedication:
    def __init__(self):
        print("Medication frame")

        self.BASE_DIR = "C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase"
        text_font = ("Times", "24")
        title_font = ("Times", "44")
        self.add_medication_frame = tk.Toplevel()
        self.add_medication_frame.title("Medication")
        width = self.add_medication_frame.winfo_screenwidth()
        height = self.add_medication_frame.winfo_screenheight()

        self.add_medication_frame.geometry("%dx%d" % (width, height))
        self.add_medication_frame.config(background="white")
        self.image = Image.open(self.BASE_DIR + "/res/docBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.addPatient_frame = tk.Label(self.add_medication_frame, image=self.background_image, justify='center')
        self.addPatient_frame.place(relwidth=1, relheight=1)

        self.addMedication_window = tk.Label(self.addPatient_frame, bg="white", justify='center')
        self.addMedication_window.pack(fill='both', anchor='c', padx='300px', pady='15px')

        self.MedicationTitle_label = tk.Label(self.addMedication_window, text="Add Patient", bg="white")
        self.MedicationTitle_label.config(font=title_font)
        self.MedicationTitle_label.pack(side=tk.TOP, anchor='c')

        self.medicationID_frame = tk.Frame(self.addMedication_window)  # Medicationid
        self.medicationID_frame.pack(fill='both')

        self.staﬀID_prescribedBy_frame = tk.Frame(self.addMedication_window)  # staﬀID_prescribedBy
        self.staﬀID_prescribedBy_frame.pack(fill='both')

        self.patientID_frame = tk.Frame(self.addMedication_window)  # patientID
        self.patientID_frame.pack(fill='both')

        self.medicationName_frame = tk.Frame(self.addMedication_window)  # medicationName
        self.medicationName_frame.pack(fill='both')

        self.date_frame = tk.Frame(self.addMedication_window)  # date
        self.date_frame.pack(fill='both')

        self.time_frame = tk.Frame(self.addMedication_window)  # time
        self.time_frame.pack(fill='both')

        self.medicationCost_frame = tk.Frame(self.addMedication_window)  # medicationCost
        self.medicationCost_frame.pack(fill='both')

        self.button_frame = tk.Frame(self.addMedication_window)
        self.button_frame.pack(fill='both')

        self.Medicationdate_frame = tk.Frame(self.addMedication_window)
        self.Medicationdate_frame.pack(fill='both')



        # Create and pack the widgets for MedicationID
        self.MedicationID_label = tk.Label(self.medicationID_frame, text="Medication ID")
        self.MedicationID_entry = tk.Entry(self.medicationID_frame, justify='left')
        self.MedicationID_label.config(font=text_font)
        self.MedicationID_entry.config(font=text_font)
        self.MedicationID_label.pack(side='left', padx=15, pady=15)
        self.MedicationID_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for MedicationName
        self.staﬀID_label = tk.Label(self.staﬀID_prescribedBy_frame, text="Staff ID")
        self.staﬀID_entry = tk.Entry(self.staﬀID_prescribedBy_frame, justify='left')
        self.staﬀID_label.config(font=text_font)
        self.staffID_entry.config(font=text_font)
        self.staﬀID_label.pack(side='left', padx=15, pady=15)
        self.staﬀID_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for MedicationName
        self.patientID_label = tk.Label(self.patientID_frame, text="Patient ID")
        self.patientID_entry = tk.Entry(self.patientID_frame, justify='left')
        self.patientID_label.config(font=text_font)
        self.patientID_entry.config(font=text_font)
        self.patientID_label.pack(side='left', padx=15, pady=15)
        self.patientID_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for medicationName
        self.medicationName_label = tk.Label(self.medicationName_frame, text="Medication Description")
        self.medicationName_entry = tk.Entry(self.medicationName_frame, justify='left')
        self.medicationName_label.config(font=text_font)
        self.medicationName_entry.config(font=text_font)
        self.medicationName_label.pack(side='left', padx=15, pady=15)
        self.medicationName_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for date
        self.date_label = tk.Label(self.date_frame, text="Given date")
        self.date_entry = DateEntry(self.date_frame, width=12, background='black',foreground='white', borderwidth=2)
        self.date_label.config(font=text_font)
        self.date_entry.config(font=text_font)
        self.date_label.pack(side='left', padx=15, pady=15)
        self.date_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for time
        self.time_label = tk.Label(self.time_frame, text="Given Time")
        self.time_entry = tk.Entry(self.time_frame, justify='left')
        self.time_label.config(font=text_font)
        self.time_entry.config(font=text_font)
        self.time_label.pack(side='left', padx=15, pady=15)
        self.time_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for medicationCost
        self.medicationCost_label = tk.Label(self.medicationCost_frame, text="Medical Cost")
        self.medicationCost_entry = tk.Entry(self.medicationCost_frame, justify='left')
        self.medicationCost_label.config(font=text_font)
        self.medicationCost_entry.config(font=text_font)
        self.medicationCost_label.pack(side='left', padx=15, pady=15)
        self.medicationCost_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.compute_button = tk.Button(self.button_frame, text='Add Medication',bg="#74d4cc",command=self.addMedication)
        self.compute_button.config(font=text_font)
        self.compute_button.pack(side='right', padx=15, pady=15)

        self.back_button = tk.Button(self.button_frame, text='Back', command=self.back, bg="#74d4cc")
        self.back_button.config(font=text_font)
        self.back_button.pack(side='right', padx=15, pady=15)

        self.medicationID_frame.pack()
        self.staﬀID_prescribedBy_frame.pack()
        self.patientID_frame.pack()
        self.medicationName_frame.pack()
        self.date_frame.pack()
        self.time_frame.pack()
        self.medicationCost_frame.pack()
        self.button_frame.pack()
        self.addMedication_window.mainloop()

    def back(self):
        self.add_medication_frame.destroy()

    def addMedication(self):
        print("added Appointment")
        Medication_id = self.MedicationID_entry.get()
        staﬀID = self.staﬀID_entry.get()
        patientID = self.patientID_entry.get()
        medicationName = self.medicationName_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        medicationCost = self.medicationCost_entry.get()

        print(Medication_id, staﬀID, patientID, medicationName, date,time,medicationCost)

        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor()
        if all([Medication_id, staﬀID, patientID, medicationName, date,time,medicationCost]) != None:
            command = "INSERT INTO medication VALUES ('" + Medication_id + "','" + staﬀID + "','" + patientID + "','" \
                      + medicationName + "','" \
                      + date + "','" \
                      + time + "','" \
                      + medicationCost + "')"
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