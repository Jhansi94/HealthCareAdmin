import re
import tkinter
import tkinter.messagebox

import PIL
from PIL import ImageTk, Image

from appointment.AddAppointment import AddAppointment
from appointment.EditAppointment import EditAppointment
from appointment.SearchAppointment import SearchAppointment

from department.AddDepartment import AddDepartment
from department.EditDepartment import Editdepartment
from department.SearchDepartment import SearchDepartment

from admission.AddAdmission import AddAdmission
from admission.SearchAdmission import SearchAdmission
from admission.EditAdmission import EditAdmission

from healthService.AddHealthService import AddHealthService
from healthService.EditHealthService import EditHealthService
from healthService.SearchHealthService import SearchHealthService

from medication.AddMedication import AddMedication
from medication.EditMedication import EditMedication
from medication.SearchMedication import SearchMedication

from patient.AddPatient import AddPatient
from patient.EditPatient import EditPatient
from patient.SearchPatient import SearchPatient

from medicalHistory.AddMedicalHistory import AddMedicalHistory
from medicalHistory.EditMedicalHistory import EditMedicalHistory
from medicalHistory.SearchMedicalHistory import SearchMedicalHistory

from staff.AddStaff import AddStaff
from staff.EditStaff import EditStaff
from staff.SearchStaff import SearchStaff

patientID = ""
x = []


class OperationsClass():
    def __init__(self,*args):
        #Create main Window
        self.name = args[0]

        self.main_frame = tkinter.Toplevel()
        self.main_frame.title(self.name)
        self.main_frame.configure( bg="white")

        width = self.main_frame.winfo_screenwidth()
        height = self.main_frame.winfo_screenheight()
        self.main_frame.config(background="white")
        self.image = Image.open(r"C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase/res/docBg.jpg")
        # The (450, 350) is (height, width)
        self.image = self.image.resize((width, height), Image.ANTIALIAS)

        self.background_image = ImageTk.PhotoImage(self.image)
        self.main_window = tkinter.Label(self.main_frame, image=self.background_image, justify='center')
        self.main_window.place(relwidth=1, relheight=1)

        Font_tuple = ("Comic Sans MS", 20)

        #Create the six frames

        self.patientTitle_frame = tkinter.Frame(self.main_window)
        self.patientTitle_frame.pack(fill='both', padx=15, pady=15)
        self.one_frame = tkinter.Frame(self.main_window)
        self.one_frame.pack(anchor="c", padx=15, pady=15)

        self.entry_frame = tkinter.Frame(self.one_frame, bg="white")
        self.entry_frame.pack(side=tkinter.LEFT)

        self.search_frame = tkinter.Frame(self.one_frame, bg="white")
        self.search_frame.pack(side=tkinter.LEFT)

        self.edit_frame = tkinter.Frame(self.one_frame, bg="white")
        self.edit_frame.pack(side=tkinter.LEFT)

        self.add_frame = tkinter.Frame(self.one_frame,bg="white")
        self.add_frame.pack(side=tkinter.LEFT)


        #Create and pack the widgets for patientFrame
        self.Title_label = tkinter.Label(self.patientTitle_frame, text=self.name +" Details")
        self.Title_label.configure(font=Font_tuple)
        self.Title_label.pack(side='left', padx=15, pady=15)

        self.ID_entry = tkinter.Entry(self.entry_frame, justify='left')
        self.ID_entry.configure(font=Font_tuple)
        self.ID_entry.pack(side=tkinter.LEFT, padx=15, pady=15)

        # Creating a photoimage object to use image

        add_fp = open("C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase/res/add.png", "rb")
        add_photo = PIL.Image.open(add_fp)
        add_image = ImageTk.PhotoImage(add_photo)

        self.Add_img = tkinter.Button(self.add_frame, justify='right', image=add_image,
                                          relief='flat', bg="white", command=self.addPatient)
        self.Add_img.pack(side=tkinter.TOP, padx=15, pady=15)
        self.add_label = tkinter.Label(self.add_frame, text="Add", font=40, bg="white")
        self.add_label.configure(font=Font_tuple)
        self.add_label.pack(side=tkinter.BOTTOM, padx=15, pady=15)

        #search frame

        search_fp = open("C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase/res/search.png", "rb")
        search_photo = PIL.Image.open(search_fp)
        search_image = ImageTk.PhotoImage(search_photo)

        self.ID_label = tkinter.Label(self.entry_frame,text="Search",bg="white")
        self.ID_label.configure(font=Font_tuple)
        self.ID_label.pack(side=tkinter.BOTTOM, padx=15, pady=15)
        self.Search_img = tkinter.Button(self.entry_frame, justify='right', image=search_image,
                                       relief='flat', bg="white", command=self.searchPatient)
        self.Search_img.configure(font=Font_tuple)
        self.Search_img.pack(side=tkinter.TOP, padx=15, pady=15)


        #edit frame

        edit_fp = open("C:/Users/jhans/PycharmProjects/pythonProject/PatientDatabase/res/edit.png", "rb")
        edit_photo = PIL.Image.open(edit_fp)
        edit_image = ImageTk.PhotoImage(edit_photo)

        self.ID_label = tkinter.Label(self.edit_frame, text="Edit",bg="white")
        self.ID_label.configure(font=Font_tuple)
        self.ID_label.pack(side=tkinter.BOTTOM, padx=15, pady=15)


        self.Edit_img = tkinter.Button(self.edit_frame, justify='right',image=edit_image,
                                              relief='flat',bg="white",command=self.editPatient)
        self.Edit_img.configure(font=Font_tuple)
        self.Edit_img.pack(side=tkinter.TOP, padx=15, pady=15)


        self.one_frame.pack()
        self.entry_frame.pack()
        self.edit_frame.pack()
        self.search_frame.pack()
        self.add_frame.pack()



        tkinter.mainloop()

    def addPatient(self):
        print("Adding ")
        if self.name is 'Patient':
            print("patient")
            addPatient = AddPatient()
        elif self.name is 'Staff':
            addStaff = AddStaff()
        elif self.name is 'Department':
            addDepartment = AddDepartment()
        elif self.name is 'Admission':
            admission = AddAdmission()
        elif self.name is 'Appointment':
            addAppointment = AddAppointment()
        elif self.name is 'Medication':
            print("medication")
            addMedication = AddMedication()
        elif self.name is 'MedicalHistory':
            addMedicalHistory = AddMedicalHistory()
        elif self.name is 'Health Service':
            print("healthservice")
            addHealthService = AddHealthService()
        else:
            print("None")

    def searchPatient(self):
        print("Searching")
        value = self.ID_entry.get()
        id = re.sub('[^A-Za-z0-9]+', '', value)
        if len(id) != 0:
            print(id)
            if self.name is 'Patient':
                searchPatient = SearchPatient(id)
            elif self.name is 'Staff':
                searchStaff = SearchStaff(id)
            elif self.name is 'Department':
                searchDepartment = SearchDepartment(id)
            elif self.name is 'Admission':
                searchAdmission = SearchAdmission(id)
            elif self.name is 'Appointment':
                searchAppointment = SearchAppointment(id)
            elif self.name is 'Medication':
                searchMedication = SearchMedication(id)
            elif self.name is 'MedicalHistory':
                searchMedicalHistory = SearchMedicalHistory(id)
            elif self.name is 'HealthService':
                searchHealthService = SearchHealthService(id)
            else:
                print("None")
        else:
            tkinter.messagebox.showinfo("Sorry", "Please enter the ID")
    def editPatient(self):
        print("Editing")
        patientID = self.ID_entry.get()
        id = re.sub('[^A-Za-z0-9]+', '', patientID)
        if len(id) != 0:
            print(id)
            if self.name is 'Patient':
                editPatient = EditPatient(id)
            elif self.name is 'Staff':
                editStaff = EditStaff(id)
            elif self.name is 'Department':
                editDeaprtment = Editdepartment(id)
            elif self.name is 'Admission':
                editAdmission = EditAdmission(id)
            elif self.name is 'Appointment':
                editAppointment = EditAppointment(id)
            elif self.name is 'Medication':
                editMedication = EditMedication(id)
            elif self.name is 'MedicalHistory':
                editMedicalHistory = EditMedicalHistory(id)
            elif self.name is 'HealthService':
                edithealthService = EditHealthService(id)
            else:
                print("None")
        else:
            tkinter.messagebox.showinfo("Sorry", "Please enter the ID")





