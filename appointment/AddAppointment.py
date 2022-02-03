import tkinter

import mysql.connector
import tkinter as tk
from PIL import ImageTk, Image
from tkcalendar import Calendar, DateEntry



class AddAppointment:
    def __init__(self):
        print("Appointment frame")

        self.BASE_DIR = "C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase"
        text_font = ("Times", "24")
        title_font = ("Times", "44")
        self.appointment_frame = tk.Toplevel()
        self.appointment_frame.title("Add Patient")
        width = self.appointment_frame.winfo_screenwidth()
        height = self.appointment_frame.winfo_screenheight()

        self.appointment_frame.geometry("%dx%d" % (width, height))
        self.appointment_frame.config(background="white")
        self.image = Image.open(self.BASE_DIR + "/res/docBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.addappoint_frame = tk.Label(self.appointment_frame, image=self.background_image, justify='center')
        self.addappoint_frame.place(relwidth=1, relheight=1)

        self.addAppoint_window = tk.Label(self.addappoint_frame, bg="white", justify='center')
        self.addAppoint_window.pack(fill='both', anchor='c', padx='300px', pady='50px')

        self.appointment_frame.title("Appointment")

        self.AppointmentTitle_frame = tk.Frame(self.addAppoint_window,bg='white')  # admissionID
        self.AppointmentTitle_frame.pack(fill='both')

        self.AppointmentId_frame = tk.Frame(self.addAppoint_window,bg='white')  # admissionID
        self.AppointmentId_frame.pack(fill='both')

        self.patientId_frame = tk.Frame(self.addAppoint_window,bg='white')  # admissionDate
        self.patientId_frame.pack(fill='both')

        self.apptStaffId_frame = tk.Frame(self.addAppoint_window,bg='white')  # patientid
        self.apptStaffId_frame.pack(fill='both')

        self.apptDate_frame = tk.Frame(self.addAppoint_window,bg='white')  # patientid
        self.apptDate_frame.pack(fill='both')

        self.apptTime_Frame = tk.Frame(self.addAppoint_window,bg='white')  # patientFirstName
        self.apptTime_Frame.pack(fill='both')

        self.apptCost_Frame = tk.Frame(self.addAppoint_window,bg='white')  # patientFirstName
        self.apptCost_Frame.pack(fill='both')

        self.apptButton_Frame = tk.Frame(self.addAppoint_window, bg='white')  # patientFirstName
        self.apptButton_Frame.pack(fill='both')

        self.apptTitle_label = tk.Label(self.AppointmentTitle_frame, text="Appointment",bg='white')
        self.apptTitle_label.config(font=title_font)
        self.apptTitle_label.pack(anchor='c', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.apptID_label = tk.Label(self.AppointmentId_frame, text="Appointment ID",bg='white')
        self.apptID_entry = tk.Entry(self.AppointmentId_frame, justify='left',bg='white')
        self.apptID_label.config(font=text_font)
        self.apptID_entry.config(font=text_font)
        self.apptID_label.pack(side='left', padx=15, pady=15)
        self.apptID_entry.pack(side='left', padx=15, pady=15)

        self.apptdate_label = tk.Label(self.apptDate_frame, text="Appointment Date",bg='white')
        self.apptdate_entry = DateEntry(self.apptDate_frame, width=12, background='black', foreground='white')
        self.apptdate_label.config(font=text_font)
        self.apptdate_entry.config(font=text_font)
        self.apptdate_label.pack(side='left', padx=15, pady=15)
        self.apptdate_entry.pack(side='left', padx=15, pady=15)

        self.apptTime_label = tk.Label(self.apptTime_Frame, text="Appointment Time",bg='white')
        self.apptTime_entry = tk.Entry(self.apptTime_Frame,justify="left",bg='white')
        self.apptTime_label.config(font=text_font)
        self.apptTime_entry.config(font=text_font)
        self.apptTime_label.pack(side='left', padx=15, pady=15)
        self.apptTime_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.patientID_label = tk.Label(self.patientId_frame, text="Patient ID",bg='white')
        self.patientID_entry = tk.Entry(self.patientId_frame, justify='left',bg='white')
        self.patientID_label.config(font=text_font)
        self.patientID_entry.config(font=text_font)
        self.patientID_label.pack(side='left', padx=15, pady=15)
        self.patientID_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.apptStaffID_label = tk.Label(self.apptStaffId_frame, text="appointed to StaffID",bg='white')
        self.apptStaffID_entry = tk.Entry(self.apptStaffId_frame, justify='left',bg='white')
        self.apptStaffID_label.config(font=text_font)
        self.apptStaffID_entry.config(font=text_font)
        self.apptStaffID_label.pack(side='left', padx=15, pady=15)
        self.apptStaffID_entry.pack(side='left', padx=15, pady=15)


        self.apptCost_label = tk.Label(self.apptCost_Frame, text="Appointment Cost",bg='white')
        self.apptCost_entry = tk.Entry(self.apptCost_Frame, justify='left',bg='white')
        self.apptCost_label.config(font=text_font)
        self.apptCost_entry.config(font=text_font)
        self.apptCost_label.pack(side='left', padx=15, pady=15)
        self.apptCost_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.compute_button = tk.Button(self.apptButton_Frame, text='Add Appointment',bg="#74d4cc", command=self.addAppoint)
        self.compute_button.config(font=text_font)
        self.compute_button.pack(side='right', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.back_button = tk.Button(self.apptButton_Frame, text='Back', command=self.back, bg="#74d4cc")
        self.back_button.config(font=text_font)
        self.back_button.pack(side='right', padx=15, pady=15)

        self.AppointmentId_frame.pack()
        self.patientId_frame.pack()
        self.apptStaffId_frame.pack()
        self.apptDate_frame.pack()
        self.apptTime_Frame.pack()
        self.apptCost_Frame.pack()
        self.addAppoint_window.mainloop()
    def back(self):
        self.appointment_frame.destroy()
    def addAppoint(self):
        print("added Appointment")
        patient_id = self.patientID_entry.get()
        appointID = self.apptID_entry.get()
        appointStaffID = self.apptStaffID_entry.get()
        appointDate = self.apptdate_entry.get()
        appointTime = self.apptTime_entry.get()
        appointCost = self.apptCost_entry.get()


        print(patient_id, appointID, appointStaffID, appointDate, appointTime,appointCost)

        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor()
        if all([patient_id, appointID, appointStaffID, appointDate, appointTime,appointCost]) != None:
            command = "INSERT INTO appointment VALUES ('" + appointID + "','" + patient_id + "','" + appointStaffID + "','" \
                      + appointDate + "','" \
                      + appointTime + "','" \
                      + appointCost + "')"
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