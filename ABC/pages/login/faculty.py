import os
import shutil
from ABC import database

from ABC.pages import header


class Faculty:
    clear = staticmethod(lambda: os.system('cls'))

    def __init__(self) -> None:
        self.TERMINAL_WIDTH = staticmethod(lambda: shutil.get_terminal_size().columns)

        self.clear()
        header()
        self.main_page()

    def main_page(self):
        print()
        menu_options = [
            ("BASIC INFORMATION", "1"),
            ("FULL DETAILS", "2"),
            ("SALARY", "3"),
            ("UPLOAD RESULT", "4"),
        ]

        print("\nMENU:-")

        for option, value in menu_options:
            print(f"{'For'.rjust(10)} {option.ljust(30)} -> (press {value})")

        print()
        print(f"For EXIT (press 5)".rjust(self.TERMINAL_WIDTH()))
        print()
        print()

        ch = int(input(f"Enter Your Choice: ".rjust(26)))
        if ch == 1:
            self.info()
        elif ch == 2:
            self.fulldetails()
        elif ch == 3:
            self.salary()
        elif ch == 4:
            self.uploadresult()
        elif ch == 5:
            return
        else:
            Faculty()

    def info(self, isback=False):
        self.clear()
        header()
        print()

        if isback:
            print('Please Enter a valid Faculty Id & Password')
            print()

        no = int(input("Enter Faculty Id: "))
        passw = int(input("Enter Password: "))

        db = database.initialize()
        cursor = db.cursor()
        st = "SELECT * from Faculty_basic where Faculty_id={} and Password={}".format(no, passw)
        cursor.execute(st)
        data = cursor.fetchall()
        count = len(data)
        if count == 0:
            print('Please Enter a valid Faculty Id & Password')
            self.info(isback=True)
        else:
            for row in data:
                fid, fn, d, s, passwd = row
            print("   Faculty Id       :     ", fid)
            print("   Faculty Name     :     ", fn)
            print("   Department_name  :     ", d)
            print("   Subject_name     :     ", s)
            print("   Password         :     ", passwd)
            db.close()

        self.main_page()

    def fulldetails(self, isback=False):
        self.clear()
        header()
        print()

        if isback:
            print('Please Enter a valid Faculty Id & Password')
            print()

        no = int(input("Enter Faculty Id: "))
        passw = int(input("Enter Password: "))
        db = database.initialize()
        cursor = db.cursor()
        st = "SELECT * from Faculty_basic where Faculty_id={} and Password={}".format(no, passw)
        cursor.execute(st)
        data = cursor.fetchall()
        count = len(data)
        if count == 0:
            print('Please Enter a valid Faculty Id & Password')
            self.fulldetails(isback=True)
        else:
            for row in data:
                fid, fn, d, s, passwd = row
            st2 = "SELECT Age, Address, Contact_No from Faculty_data where Faculty_id={} ".format(no)
            cursor.execute(st2)
            data2 = cursor.fetchall()
            for row in data2:
                a, ad, c = row
            print("   Faculty Id      :      ", fid)
            print("   Faculty Name    :      ", fn)
            print("   Department_name :      ", d)
            print("   Subject_name    :      ", s)
            print("   Password        :      ", passwd)
            print("   Age             :      ", a)
            print("   Address         :      ", ad)
            print("   Contact No      :      ", c)
            db.close()

        self.main_page()

    def salary(self, isback=False):
        self.clear()
        header()
        print()

        if isback:
            print('Please Enter a valid Faculty Id & Password')
            print()

        no = int(input("Enter Faculty Id: "))
        passw = int(input("Enter Password: "))
        db = database.initialize()
        cursor = db.cursor()
        st = "SELECT * from Faculty_basic where Faculty_id={} and Password={}".format(no, passw)
        cursor.execute(st)
        data = cursor.fetchall()
        count = len(data)
        if count == 0:
            self.salary(isback=True)
        else:
            st2 = "SELECT Salary_status from Faculty_salary where Faculty_id={}".format(no)
            cursor.execute(st2)
            data2 = cursor.fetchone()
            # print(data2)
            for row in data2:
                st = row
            if st == 'Paid':
                print("Salary is already send to your Account!!!!")
                self.main_page()
            elif st == 'Not Paid':
                self.pay(db, no)

    def pay(self, db, id):
        card = int(input("Enter a our Account number :"))
        cd = str(card)
        countc = len(cd)
        cursor = db.cursor()
        if countc == 11:
            cond = ("UPDATE Faculty_salary SET Salary_status = '{}' WHERE Faculty_id = {} ".format('Paid', id))
            cursor.execute(cond)
            db.commit()
            db.close()
            print("Your Salary is send to your account successfully!!!")
            self.main_page()
        else:
            print("Please input a valid Acoount number")
            self.pay(db, id)

    def uploadresult(self, isback=False):
        self.clear()
        header()
        print()

        if isback:
            print('Please Enter a valid Faculty Id & Password')
            print()

        no = int(input("Enter Faculty Id: "))
        passw = int(input("Enter Password: "))
        db = database.initialize()
        cursor = db.cursor()
        st = "SELECT * from Faculty_basic where Faculty_id={} and Password={}".format(no, passw)
        cursor.execute(st)
        data = cursor.fetchall()
        count = len(data)
        db.close()
        if count == 0:
            self.uploadresult(isback=True)
        else:
            self.resultentry(db)

    def resultentry(self, db):
        print()

        roll = int(input("Enter Student Roll No: "))
        ms1 = int(input("Enter a Marks in Subject 1 : "))
        ms2 = int(input("Enter a Marks in Subject 2 : "))
        ms3 = int(input("Enter a Marks in Subject 3 : "))
        ms4 = int(input("Enter a Marks in Subject 4 : "))
        ms5 = int(input("Enter a Marks in Subject 5 : "))
        p = ((ms1 + ms2 + ms3 + ms4 + ms5) / 500) * 100
        if p >= 65:
            ov = "PASS"
        elif p <= 65 and p >= 40:
            ov = "COMPARTMENT"
        else:
            ov = "FAIL"
        db = database.initialize()
        cursor = db.cursor()
        st2 = "UPDATE Student_marks SET Marks_in_subject_1 = {}, Marks_in_subject_2 = {}, Marks_in_subject_3 = {}, Marks_in_subject_4 = {}, Marks_in_subject_5 = {}, Percentage = {}, Overall = '{}' WHERE Roll_no = {} ".format(
            ms1, ms2, ms3, ms4, ms5, p, ov, roll)
        cursor.execute(st2)
        db.commit()
        db.close()
        self.resultchoice(db)

    def resultchoice(self, db, isback=False):
        if isback:
            print()
            print("Please make choice between given option only..")

        print()
        menu_options = [
            ("ENTERING A NEW RECORD", "1"),
            ("EXIT", "2"),
        ]

        print("\nMENU:-")

        for option, value in menu_options:
            print(f"{'For'.rjust(10)} {option.ljust(30)} -> (press {value})")

        ch = int(input(f"Enter Your Choice: ".rjust(26)))
        if ch == 1:
            self.resultentry(db)
        elif ch == 2:
            self.main_page()
        else:
            self.resultchoice(db, isback=True)
