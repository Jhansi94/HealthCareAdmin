import mysql.connector
import re
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry


class AddMedicalHistory:
    def __init__(self):
        print("patient frame")

        self.BASE_DIR = "C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase"
        text_font = ("Times", "24")
        title_font = ("Times", "44")
        self.history_frame = tk.Toplevel()
        self.history_frame.title("Add Patient")
        width = self.history_frame.winfo_screenwidth()
        height = self.history_frame.winfo_screenheight()

        self.history_frame.geometry("%dx%d" % (width, height))
        self.history_frame.config(background="white")
        self.image = Image.open(self.BASE_DIR + "/res/docBg.jpg")
        # self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.addhistrory_frame = tk.Label(self.history_frame, image=self.background_image, justify='center')
        self.addhistrory_frame.place(relwidth=1, relheight=1)

        self.addHistory_window = tk.Label(self.addhistrory_frame, bg="white", justify='center')
        self.addHistory_window.pack(fill='both', anchor='c', padx='300px', pady='50px')

        self.history_frame.title("Medical History")

        self.historyTitle_frame = tk.Frame(self.addHistory_window, bg='white')  # patientid
        self.historyTitle_frame.pack(fill='both', padx=15, pady=15)

        self.patientID_frame = tk.Frame(self.addHistory_window,bg='white')  # patientid
        self.patientID_frame.pack(fill='both', padx=15, pady=15)

        self.problem_frame = tk.Frame(self.addHistory_window,bg='white')  # patientFirstName
        self.problem_frame.pack(fill='both', padx=15, pady=15)

        self.diagnosedBy_frame = tk.Frame(self.addHistory_window,bg='white')  # patientSecondName
        self.diagnosedBy_frame.pack(fill='both', padx=15, pady=15)

        self.diagnosedDate_frame = tk.Frame(self.addHistory_window,bg='white')  # dateOfBirth
        self.diagnosedDate_frame.pack(fill='both', padx=15, pady=15)

        self.reviewedStaffID = tk.Frame(self.addHistory_window,bg='white')  # gender
        self.reviewedStaffID.pack(fill='both', padx=15, pady=15)

        self.button_frame = tk.Frame(self.addHistory_window,bg='white')
        self.button_frame.pack(fill='both', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.title_label = tk.Label(self.historyTitle_frame, text="Medical History", bg='white')
        self.title_label.config(font=title_font)
        self.title_label.pack(anchor='c', padx=15, pady=15)

        # Create and pack the widgets for patientID
        self.patientID_label = tk.Label(self.patientID_frame, text="Patient ID",bg='white')
        self.patientID_entry = tk.Entry(self.patientID_frame, justify='left',bg='white')
        self.patientID_label.config(font=text_font)
        self.patientID_entry.config(font=text_font)
        self.patientID_label.pack(side='left', padx=15, pady=15)
        self.patientID_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientName
        self.problem_label = tk.Label(self.problem_frame, text="Problem",bg='white')
        self.problem_entry = tk.Entry(self.problem_frame, justify='left',bg='white')
        self.problem_label.config(font=text_font)
        self.problem_entry.config(font=text_font)
        self.problem_label.pack(side='left', padx=15, pady=15)
        self.problem_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for patientName
        self.diagnosedBy_label = tk.Label(self.diagnosedBy_frame, text="Diagnosed By",bg='white')
        self.diagnosedBy_entry = tk.Entry(self.diagnosedBy_frame, justify='left',bg='white')
        self.diagnosedBy_label.config(font=text_font)
        self.diagnosedBy_entry.config(font=text_font)
        self.diagnosedBy_label.pack(side='left', padx=15, pady=15)
        self.diagnosedBy_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for dateOfBirth
        self.diagnosedDate_label = tk.Label(self.diagnosedDate_frame, text="Diagnosed Date",bg='white')
        self.diagnosedDate_entry = DateEntry(self.diagnosedDate_frame, width=12, background='black',foreground='white', borderwidth=2)
        self.diagnosedDate_label.config(font=text_font)
        self.diagnosedDate_entry.config(font=text_font)
        self.diagnosedDate_label.pack(side='left', padx=15, pady=15)
        self.diagnosedDate_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for gender
        self.reviewedStaffID_label = tk.Label(self.reviewedStaffID, text="Reviewed By",bg='white')
        self.reviewedStaffID_entry = tk.Entry(self.reviewedStaffID, justify='left',bg='white')
        self.reviewedStaffID_label.config(font=text_font)
        self.reviewedStaffID_entry.config(font=text_font)
        self.reviewedStaffID_label.pack(side='left', padx=15, pady=15)
        self.reviewedStaffID_entry.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.compute_button = tk.Button(self.button_frame, text='Add', command=self.addHistory)
        self.compute_button.config(font=text_font)
        self.compute_button.pack(side='left', padx=15, pady=15)

        # Create and pack the widgets for the button widgets
        self.back_button = tk.Button(self.button_frame, text='Back', command=self.back, bg="#74d4cc")
        self.back_button.config(font=text_font)
        self.back_button.pack(side='right', padx=15, pady=15)

        self.patientID_frame.pack()
        self.problem_frame.pack()
        self.diagnosedBy_frame.pack()
        self.diagnosedDate_frame.pack()
        self.button_frame.pack()
        self.addHistory_window.mainloop()

    def addHistory(self):
        print("added History")
        patient_id = self.patientID_entry.get()
        problem = self.problem_entry.get()
        diagnosedBy = self.diagnosedBy_entry.get()
        diagnosedDate_entry = self.diagnosedDate_entry.get()
        reviewedBy = self.reviewedStaffID_entry.get()

        print(patient_id, problem, diagnosedBy, diagnosedDate_entry, reviewedBy)

        db = mysql.connector.connect(host="localhost", user="root", passwd="root", database="pms")
        mycursor = db.cursor()
        if all([patient_id, problem, diagnosedBy, diagnosedDate_entry, reviewedBy]) != None:
            command = "INSERT INTO medical_history VALUES ('" + patient_id + "','" + problem + "','" + diagnosedBy + "','" \
                      + diagnosedDate_entry + "','" \
                      + reviewedBy + "')"
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