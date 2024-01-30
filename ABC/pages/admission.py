import os
import random
import webbrowser

from ABC import database
from ABC.pages import header
from ABC.utils import separator


class Admission:
    def __init__(self) -> None:
        self.clear = staticmethod(lambda: os.system('cls'))
        self.HOSTEL_CHARGES = os.path.join(os.getcwd(), "ABC", "docs", "Hostel Room Type & Charge List 2024-25.pdf")
        self.CANTEEN_CHARGES = os.path.join(os.getcwd(), "ABC", "docs", "Canteen Menu & Rate List 2024-25.pdf")

        separator()
        self.clear()
        header()
        print()
        self.main_page()

    def rollno(self):
        db = database.initialize()
        cursor = db.cursor()
        cond = "SELECT COUNT(*) FROM Student_data"
        cursor.execute(cond)
        data = cursor.fetchone()
        return 101 + data[0]

    def main_page(self):
        self.name = input("Enter Student Name: ")
        self.father = input("Enter Father Name: ")
        self.mother = input("Enter Mother Name: ")
        self.age = int(input("Enter Age: "))
        self.address = input("Enter Address: ")
        self.contact_num = int(input("Enter Contact No.: "))
        self.subjects = []

        print("Choose Subject in between:-")
        print("""
                Mathematics
                Physics
                Chemistry
                English
                Hindi
                Sanskrit
                Physical Education
                Business Studies
                Accounts
                Economics
        """)

        for i in range(5):
            self.subjects.append(input(f"Enter Applying For Subject {i + 1}: "))

        self.marks_10 = float(input("Enter Class 10th Marks: "))
        self.roll_no_12 = int(input("Enter Class 12th roll no.: "))
        self.father_occupation = input("Enter Father's Occupation: ")

        print()

        menu_options = [
            ("YES", 1),
            ("NO", 2),
        ]

        print("Do you want to use a our Hostel service?")
        for option, value in menu_options:
            print(f"{'For'.rjust(10)} {option.ljust(30)} -> (press {value})")

        ch = int(input(f"Enter Your Choice: ".rjust(26)))
        if ch == 1:
            print("\nChoose a any one type of room here.")
            print("We are opening Hostel Room Type & Charge List 2024-25....")

            webbrowser.open(self.HOSTEL_CHARGES)

            menu_options = [
                ("Room G12", 1),
                ("Room G10", 2),
                ("Room G8", 3),
                ("Room G6", 4),
                ("Room G5", 5),
                ("Room G4", 6),
                ("Room G3", 7),
                ("Room PS1", 8),
                ("Room PS2", 9),
                ("Room PS2", 10),
                ("Room PSS", 11),
            ]

            for option, value in menu_options:
                print(f"{'For'.rjust(10)} {option.ljust(30)} -> (press {value})")
            print()

            ch = int(input(f"Enter Your Choice: ".rjust(26)))
            if ch in range(1, 12):
                self.room = menu_options[ch - 1][0].split(" ")[-1]
            else:
                print("OK, You don't use our Hostel service.")
                self.room = 'NO'
        elif ch == 2:
            print("OK, You don't use our Hostel service.")
            self.room = 'NO'

        print()

        menu_options = [
            ("YES", 1),
            ("NO", 2),
        ]

        print("Do you want to use a our Canteen service?")
        for option, value in menu_options:
            print(f"{'For'.rjust(10)} {option.ljust(30)} -> (press {value})")
        print()

        ch = int(input(f"Enter Your Choice: ".rjust(26)))
        if ch == 1:
            print("\nChoose a any one type of plate here.")
            print("We are opening Canteen Menu & Rate List 2024-25.....")

            webbrowser.open(self.CANTEEN_CHARGES)

            menu_options = [
                ("Room LS", 1),
                ("Room LM", 2),
                ("Room LL", 3),
                ("Room LSD", 4),
            ]

            for option, value in menu_options:
                print(f"{'For'.rjust(10)} {option.ljust(30)} -> (press {value})")
            print()

            ch = int(input(f"Enter Your Choice: ".rjust(26)))
            if ch in range(1, 5):
                self.lunch = menu_options[ch - 1][0].split(" ")[-1]
            else:
                print("OK, You don't use our Canteen service.")
                self.lunch = 'NO'

        elif ch == 2:
            print("OK, You don't use our Canteen service.")
            self.lunch = 'NO'

        self.passwd = random.randint(0000, 9999)
        self.gen_rollno = self.rollno()

        self.check()

    def check(self):
        rol = str(self.roll_no_12)
        count = len(rol)
        if self.marks_10 >= 75 and count == 5:
            print("Congralutaions your registration form is successfully submitted !!")
            print('\n\n\n')

            subjects = "\n"

            for i, sub in enumerate(self.subjects):
                subjects += f"{' '.rjust(10)} {' '.ljust(30)} " + f"{i + 1}. {sub}" + "\n"

            details = [
                ("Roll Number", self.gen_rollno),
                ("Password", self.passwd),
                ("Name", self.name),
                ("Father Name", self.father),
                ("Mother Name", self.mother),
                ("Age", self.age),
                ("Address", self.address),
                ("Subjects applied for", subjects),
                ("Batch", "ER01"),
            ]

            print("Your Details are as follows:-")

            for option, value in details:
                print(f"{' '.rjust(10)} {option.ljust(30)}: {value}")
            print()
            self.save()
            input("\nEnter to go back to main menu.")
        elif self.marks_10 >= 75 and count != 5:
            print("Please Enter correct 12th roll no !!!")
            self.roll_no_12 = int(input("Enter Class 12th roll no. : "))
            self.check()
        else:
            print("You are not eligible to take admission")
            print()
            print("Best of luck for next time!!")

    def note(self):
        file = open('Student_Data.txt', 'a')
        no = self.gen_rollno - 100
        rec1 = "Studentno" + str(no) + "-" + '\n'
        file.write(rec1)
        rec2 = "          Roll no :" + str(
            self.gen_rollno) + '\n' + "          Student Name :" + self.name + '\n' + "          Father Name :" + self.father + '\n' + "          Mother Name :" + self.mother + '\n' + "          Age :" + str(
            self.age) + '\n' + "          Address :" + self.address + '\n' + "          Contact No. :" + str(
            self.contact_num) + '\n' + "          Subjects opt : " + ','.join(
            self.subjects) + '\n' + "          Class 10th Marks :" + str(
            self.marks_10) + '\n' + "          Class 12th roll no. :" + str(
            self.roll_no_12) + '\n' + "          Password  :" + str(
            self.passwd) + '\n' + "          Father's Occupation :" + self.father_occupation + '\n' + "          Room Type :" + self.room + '\n' + "          Lunch Type :" + self.lunch + '\n'
        file.write(rec2)
        file.close()

        # Backup
        file = open('Student_Data_Backup.txt', 'a')
        rec3 = str(self.gen_rollno) + ',' + self.name + ',' + self.father + ',' + self.mother + ',' + str(
            self.age) + ',' + self.address + ',' + str(self.contact_num) + ',' + ','.join(self.subjects) + ',' + str(
            self.marks_10) + ',' + str(self.roll_no_12) + ',' + str(
            self.passwd) + ',' + self.father_occupation + ',' + self.room + ',' + self.lunch + '\n'
        file.write(rec3)
        file.close()

    def feecalculator(self):
        db = database.initialize()
        cursor = db.cursor()

        fee = 0
        hostelFee = 0
        canteenFee = 0
        subjectsFee = []
        for sub in self.subjects:
            cmd = "SELECT Fee from Fee where Subjects_name='{}'".format(sub)
            cursor.execute(cmd)
            data = cursor.fetchone()
            fee += data[0]
            subjectsFee.append(data[0])

        if self.room != "NO":
            cmd = "SELECT Fee from Hostel_fee where Code_no='{}'".format(self.room)
            cursor.execute(cmd)
            data = cursor.fetchone()
            fee += data[0]
            hostelFee = data[0]

        if self.lunch != "NO":
            cmd = "SELECT Fee from Canteen_fee where Code_no='{}'".format(self.lunch)
            cursor.execute(cmd)
            data = cursor.fetchone()
            fee += data[0]
            canteenFee = data[0]

        cmd = "INSERT INTO Student_feedetails(Roll_no, Students_name, Fees_of_subject_1, Fees_of_subject_2, Fees_of_subject_3, Fees_of_subject_4, Fees_of_subject_5, Hostel_fee, Canteen_fee, Total_Fee) VALUES({}, '{}', {}, {}, {}, {}, {}, {}, {}, {})".format(
            self.gen_rollno, self.name, *subjectsFee, hostelFee, canteenFee, fee)
        cursor.execute(cmd)
        db.commit()
        db.close()

        return fee

    def basic(self):
        db = database.initialize()
        cursor = db.cursor()
        cond = (
            "INSERT INTO Student_basic(Roll_no, Students_name, Fathers_name, Mothers_name, Password) VALUES({}, '{}', '{}', '{}', {})".format(
                self.gen_rollno, self.name, self.father, self.mother, self.passwd))
        cursor.execute(cond)
        db.commit()
        db.close()

    def data(self):
        db = database.initialize()
        cursor = db.cursor()
        cond = (
            "INSERT INTO Student_data(Roll_no, Students_name, Age, Address, Contact_No, Class_10th_Marks, Class_12th_roll_no, Fathers_Occupation) VALUES({}, '{}', {}, '{}', {}, {}, {}, '{}')".format(
                self.gen_rollno, self.name, self.age, self.address, self.contact_num, self.marks_10, self.roll_no_12,
                self.father_occupation))
        cursor.execute(cond)
        db.commit()
        db.close()

    def subjectopt(self):
        db = database.initialize()
        cursor = db.cursor()
        cond = (
            "INSERT INTO Student_subjectopt(Roll_no, Students_name, Subject_1, Subject_2, Subject_3, Subject_4, Subject_5 ) VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}')".format(
                self.gen_rollno, self.name, *self.subjects))
        cursor.execute(cond)
        db.commit()
        db.close()

    def marks(self):
        db = database.initialize()
        cursor = db.cursor()
        cond = ("INSERT INTO Student_marks(Roll_no, Students_name) VALUES({}, '{}')".format(self.gen_rollno, self.name))
        cursor.execute(cond)
        db.commit()
        db.close()

    def studentsfee(self, fees):
        db = database.initialize()
        cursor = db.cursor()
        cond = ("INSERT INTO Student_feedata(Roll_no, Students_name, Payable_amount) VALUES({}, '{}', {})".format(
            self.gen_rollno, self.name, fees))
        cursor.execute(cond)
        db.commit()
        db.close()

    def sql(self):
        self.basic()
        self.data()
        self.subjectopt()
        self.marks()
        fees = self.feecalculator()
        self.studentsfee(fees)

    def save(self):
        self.note()
        self.sql()
