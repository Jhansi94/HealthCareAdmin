import os
import PIL
import tkinter as tk
from PIL import ImageTk, Image

from OperationsClass import OperationsClass



class MainPage:

    def __init__(self):
        #Create main Window
        self.main_frame = tk.Tk()
        self.main_frame.configure(bg="white")
        width = self.main_frame.winfo_screenwidth()
        height = self.main_frame.winfo_screenheight()
        self.main_frame.geometry("%dx%d" % (width, height))

        self.BASE_DIR = os.path.dirname(__file__)

        text_font = ("Times", "24")
        title_font = ("Times", "44")

        self.main_frame.config(background="white")
        self.image = Image.open(self.BASE_DIR+"/res/docBg.jpg")
        #self.image = Image.open(RESOURCE_PATH+"docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.main_window = tk.Label(self.main_frame, image=self.background_image, justify='center')
        self.main_window.place(relwidth=1, relheight=1)

        # setting tk window size
        self.main_frame.title("Patient Management System")
        self.title_frame = tk.Frame(self.main_window, bg="#74d4cc")
        self.title_frame.pack(side=tk.TOP, padx=10, pady=10)
        self.one_frame = tk.Frame(self.main_window,bg="#74d4cc")
        self.one_frame.pack(side= tk.LEFT,padx=100, pady=100)
        self.two_frame = tk.Frame(self.main_window,bg="#74d4cc")
        self.two_frame.pack(side= tk.LEFT,padx=75, pady=75)
        self.three_frame = tk.Frame(self.main_window,bg="#74d4cc")
        self.three_frame.pack(side= tk.LEFT,padx=75, pady=75)
        self.four_frame = tk.Frame(self.main_window,bg="#74d4cc")
        self.four_frame.pack(side= tk.LEFT,padx=50, pady=50)
        self.five_frame = tk.Frame(self.main_window,bg="#74d4cc")
        #self.five_frame.pack(side=tk.LEFT, padx=15, pady=15)


        #Create the six frames
        self.patient_frame = tk.Frame(self.one_frame)
        self.patient_frame.pack(side= tk.TOP,padx=15, pady=15)

        # Creating a photoimage object to use image

        self.title_label = tk.Label(self.title_frame, text="CONNECTICUT HEALTH CARE", bg="white")
        self.title_label.config(font=title_font)
        self.title_label.pack(side=tk.TOP, padx=15, pady=15)

        patient_fp = open(self.BASE_DIR + "/res/patient.png", "rb")
        patient_photo = PIL.Image.open(patient_fp)
        patient_image = ImageTk.PhotoImage(patient_photo)

        self.patient_img = tk.Button(self.patient_frame, justify='right', image=patient_image,
                                          relief='flat',bg="white",command=self.getPatientFrame)
        self.patient_img.pack(side=tk.TOP, padx=15, pady=15)
        self.patient_label = tk.Label(self.patient_frame, text="Patient",font=40,bg="white")
        self.patient_label.config(font=text_font)
        self.patient_label.pack(side=tk.BOTTOM, padx=15, pady=15)


        staff_fp = open(self.BASE_DIR+"/res/staff.png", "rb")
        staff_photo = PIL.Image.open(staff_fp)
        staff_image = ImageTk.PhotoImage(staff_photo)


        self.staff_frame = tk.Frame(self.one_frame)
        self.staff_frame.pack(side= tk.BOTTOM,padx=15, pady=15)
        self.staff_img = tk.Button(self.staff_frame, justify='right', image=staff_image,
                                        relief='flat', bg="white",command=self.getStaffFrame)
        self.staff_img.pack(side=tk.TOP, padx=15, pady=15)
        self.staff_label = tk.Label(self.staff_frame, text="Staff",font=40,bg="white")
        self.staff_label.config(font=text_font)
        self.staff_label.pack(side=tk.BOTTOM, padx=15, pady=15)


        department_fp = open(self.BASE_DIR+"/res/department.png", "rb")
        department_photo = PIL.Image.open(department_fp)
        department_image = ImageTk.PhotoImage(department_photo)


        self.department_frame = tk.Frame(self.two_frame)
        self.department_frame.pack(side= tk.TOP,padx=15, pady=15)
        self.department_img = tk.Button(self.department_frame, justify='right', image=department_image,
                                             relief='flat',bg="white",command=self.getDepartmentFrame)
        self.department_img.pack(side=tk.TOP, padx=15, pady=15)
        self.department_label = tk.Label(self.department_frame, text="Department",font=40,bg="white")
        self.department_label.config(font=text_font)
        self.department_label.pack(side=tk.BOTTOM, padx=15, pady=15)

        appointment_fp = open(self.BASE_DIR+"/res/appointment.png", "rb")
        appointment_photo = PIL.Image.open(appointment_fp)
        appointment_image = ImageTk.PhotoImage(appointment_photo)

        self.appointment_frame = tk.Frame(self.two_frame)
        self.appointment_frame.pack(side=tk.BOTTOM, padx=15, pady=15)
        self.appointment_img = tk.Button(self.appointment_frame, justify='right', image=appointment_image,
                                              relief='flat',bg="white",command=self.getAppointmentFrame)
        self.appointment_img.pack(side=tk.TOP, padx=15, pady=15)
        self.appointment_label = tk.Label(self.appointment_frame, text="Appointment",font=40, bg="white")
        self.appointment_label.config(font=text_font)
        self.appointment_label.pack(side=tk.BOTTOM, padx=15, pady=15)

        medication_fp = open(self.BASE_DIR+"/res/medication.png", "rb")
        medication_photo = PIL.Image.open(medication_fp)
        medication_image = ImageTk.PhotoImage(medication_photo)

        self.medication_frame = tk.Frame(self.three_frame)
        self.medication_frame.pack(side=tk.TOP, padx=15, pady=15)
        self.medication_img = tk.Button(self.medication_frame, justify='right', image=medication_image,
                                             relief='flat',bg="white",command=self.getMedicationFrame)
        self.medication_img.pack(side=tk.TOP, padx=15, pady=15)
        self.medication_label = tk.Label(self.medication_frame, text="Medication",font=40, bg="white")
        self.medication_label.config(font=text_font)
        self.medication_label.pack(side=tk.BOTTOM, padx=15, pady=15)

        admission_fp = open(self.BASE_DIR+"/res/admission.png", "rb")
        admission_photo = PIL.Image.open(admission_fp)
        admission_image = ImageTk.PhotoImage(admission_photo)

        self.admission_frame = tk.Frame(self.three_frame)
        self.admission_frame.pack(side=tk.BOTTOM, padx=15, pady=15)
        self.admission_img = tk.Button(self.admission_frame, justify='right', image=admission_image,
                                            relief='flat', bg="white",command=self.getAdmissionFrame)
        self.admission_img.pack(side=tk.TOP, padx=15, pady=15)
        self.admission_label = tk.Label(self.admission_frame, text="Admission",font=40, bg="white")
        self.admission_label.config(font=text_font)
        self.admission_label.pack(side=tk.BOTTOM, padx=15, pady=15)

        healthService_fp = open(self.BASE_DIR+"/res/services.png", "rb")
        healthService_photo = PIL.Image.open(healthService_fp)
        healthService_image = ImageTk.PhotoImage(healthService_photo)

        self.healthService_frame = tk.Frame(self.four_frame)
        self.healthService_frame.pack(side=tk.TOP, padx=15, pady=15)
        self.healthService_img = tk.Button(self.healthService_frame, justify='right', image=healthService_image,
                                                relief='flat', bg="white",command=self.getHealthServiceFrame)
        self.healthService_img.pack(side=tk.TOP, padx=15, pady=15)
        self.healthService_label = tk.Label(self.healthService_frame, text="Health Services",font=40, bg="white")
        self.healthService_label.config(font=text_font)
        self.healthService_label.pack(side=tk.BOTTOM, padx=15, pady=15)

        medicalHistory_fp = open(self.BASE_DIR+"/res/history.png","rb")
        medicalHistory_photo = PIL.Image.open(medicalHistory_fp)
        medicalHistory_image = ImageTk.PhotoImage(medicalHistory_photo)

        self.medicalHistory_frame = tk.Frame(self.four_frame)
        self.medicalHistory_frame.pack(side=tk.BOTTOM, padx=15, pady=15)
        self.medicalHistory_img = tk.Button(self.medicalHistory_frame, justify='right', image=medicalHistory_image,
                                                 relief='flat',bg="white",command=self.getMedicalHistoryFrame)
        self.medicalHistory_img.pack(side=tk.TOP, padx=15, pady=15)
        self.medicalHistory_label = tk.Label(self.medicalHistory_frame, text="Medical History",font=40, bg="white")
        self.medicalHistory_label.config(font=text_font)
        self.medicalHistory_label.pack(side=tk.BOTTOM, padx=15, pady=15)

        insurance_fp = open(self.BASE_DIR+"/res/insurance.png",
                                 "rb")
        insurance_photo = PIL.Image.open(insurance_fp)
        insurance_image = ImageTk.PhotoImage(insurance_photo)

        self.insurance_frame = tk.Frame(self.five_frame)
        self.insurance_frame.pack(side=tk.TOP, padx=15, pady=15)
        self.insurance_img = tk.Button(self.insurance_frame, justify='right', image=insurance_image,
                                            relief='flat',bg="white",command=self.getInsuranceFrame)
        self.insurance_img.pack(side=tk.TOP, padx=15, pady=15)
        self.insurance_label = tk.Label(self.insurance_frame, text="Insurance",font=40, bg="white")
        self.insurance_label.config(font=text_font)
        self.insurance_label.pack(side=tk.BOTTOM, padx=15, pady=15)

        bill_fp = open(self.BASE_DIR+"/res/bill.png",
                            "rb")
        bill_photo = PIL.Image.open(bill_fp)
        bill_image = ImageTk.PhotoImage(bill_photo)

        self.bill_frame = tk.Frame(self.five_frame)
        self.bill_frame.pack(side=tk.BOTTOM, padx=15, pady=15)
        self.bill_img = tk.Button(self.bill_frame, justify='right', image=bill_image,relief='flat',
                                           bg="white")
        self.bill_img.pack(side=tk.TOP, padx=15, pady=15)
        self.bill_label = tk.Label(self.bill_frame, text="Bill",font=40, bg="white")
        self.bill_label.config(font=text_font)
        self.bill_label.pack(side=tk.BOTTOM, padx=15, pady=15)

        self.patient_frame.pack()
        self.staff_frame.pack()
        self.department_frame.pack()
        self.healthService_frame.pack()
        self.medicalHistory_frame.pack()
        self.medication_frame.pack()
        self.insurance_frame.pack()
        self.bill_frame.pack()

        tk.mainloop()


    def getPatientFrame(self,event=None):
        print("ntg")
        patientDetails = OperationsClass("Patient")


    def getStaffFrame(self):
        print("ntg")
        patientDetails = OperationsClass("Staff")

    def getDepartmentFrame(self):
        print("ntg")
        patientDetails = OperationsClass("Department")

    def getAdmissionFrame(self):
        print("subFrame")
        patientDetails = OperationsClass("Admission")

    def getAppointmentFrame(self):
        print("subFrame")
        patientDetails = OperationsClass("Appointment")

    def getInsuranceFrame(self):
        print("subFrame")
        patientDetails = OperationsClass("Insurance")

    def getHealthServiceFrame(self):
        print("subFrame")
        patientDetails = OperationsClass("HealthService")

    def getMedicalHistoryFrame(self):
        print("subFrame")
        patientDetails = OperationsClass("MedicalHistory")

    def getMedicationFrame(self):
        print("subFrame")
        patientDetails = OperationsClass("Medication")

    def mouseClick(event):
        print("mouse clicked")



mainPage = MainPage()
