import os
import shutil
import matplotlib.pyplot as py

from ABC import database

from ABC.pages import header
from ABC.utils import separator

class Student:
    clear = staticmethod(lambda: os.system('cls'))

    def __init__(self) -> None:
        self.TERMINAL_WIDTH = staticmethod(lambda: shutil.get_terminal_size().columns)
        
        self.clear()
        header()
        self.main_page()

    def main_page(self):
        print()
        menu_options = [
            ("BASIC INFORMATION", 1),
            ("SUBJECT OPT", 2),
            ("FULL DETAILS", 3),
            ("FEE DETAILS", 4),
            ("PAY FEES", 5),
            ("RESULT", 6),
        ]

        print("\nMENU:-")

        for option, value in menu_options:
            print(f"{'For'.rjust(10)} {option.ljust(30)} -> (press {value})")
        
        print()
        print(f"For EXIT (press 7)".rjust(self.TERMINAL_WIDTH()))
        print()
        print()

        ch = int(input(f"Enter Your Choice: ".rjust(26)))
        if ch == 1:
            self.info()
        elif ch == 2:
            self.subjectopt()
        elif ch == 3:
            self.fulldetails()
        elif ch == 4:
            self.feedetails()
        elif ch == 5:
            self.payment()
        elif ch == 6:
            self.result()
        else:
            Student()

    def info(self, isback = False):
        self.clear()
        header()
        print()

        if isback:
            print ('Please Enter a valid Roll No & Password')
            print()
        no=int(input("Enter Roll No: "))
        passw=int(input("Enter Password: "))
        db = database.initialize()
        cursor= db.cursor()
        st= "SELECT * from Student_basic where Roll_no={} and Password={}".format(no,passw)
        cursor.execute(st)
        data=cursor.fetchall()
        count=len(data)
        if count == 0 :
            self.info(isback = True)
        else:
            for row in data:
                rollno,n,f,m,passwd=row
            print("   Student Rollno:      ",rollno)
            print("   Student Name  :      ",n)
            print("   Father's Name :      ",f)
            print("   Mother's Name :      ",m)
            print("   Password      :      ",passwd)
            db.close()
            
        self.main_page()

    def subjectopt(self, isback = False):
        self.clear()
        header()
        print()

        if isback:
            print ('Please Enter a valid Roll No & Password')
            print()
        
        no=int(input("Enter Roll No: "))
        passw=int(input("Enter Password: "))
        db = database.initialize()
        cursor= db.cursor()
        st= "SELECT Roll_no, Students_name from Student_basic where Roll_no={} and Password={} ".format(no,passw)
        cursor.execute(st)
        data=cursor.fetchall()
        count=len(data)
        if count == 0 :
            self.subjectopt(isback = True)
        else:
            for row in data:
                rollno,n=row
            st2= "SELECT Subject_1, Subject_2, Subject_3,Subject_4, Subject_5 from Student_subjectopt where Roll_no={}".format(no)
            cursor.execute(st2)
            data2=cursor.fetchall()
            for row in data2:
                ap1,ap2,ap3,ap4,ap5=row
            print("   Student Rollno        :      ",rollno)
            print("   Student Name          :      ",n)
            print("   Applied For Subject 1 :      ",ap1)
            print("   Applied For Subject 2 :      ",ap2)
            print("   Applied For Subject 3 :      ",ap3)
            print("   Applied For Subject 4 :      ",ap4)
            print("   Applied For Subject 5 :      ",ap5)
            db.close()
            
        self.main_page()
    
    def fulldetails(self, isback = False):
        self.clear()
        header()
        print()

        if isback:
            print ('Please Enter a valid Roll No & Password')
            print()
        
        no=int(input("Enter Roll No: "))
        passw=int(input("Enter Password: "))
        db = database.initialize()
        cursor= db.cursor()
        st= "SELECT * from Student_basic where Roll_no={} and Password={} ".format(no,passw)
        cursor.execute(st)
        data=cursor.fetchall()
        count=len(data)
        if count == 0 :
            self.fulldetails(isback = True)
        else:
            for row in data:
                rollno,n,f,m,passwd=row
            st2= "SELECT Age, Address, Contact_No, Class_10th_Marks, Class_12th_roll_no, Fathers_Occupation from Student_data where Roll_no={} ".format(no)
            cursor.execute(st2)
            data2=cursor.fetchall()
            for row in data2:
                a,ad,c,ma,ro,oc=row
            print("   Student Rollno        :      ",rollno)
            print("   Student Name          :      ",n)
            print("   Father's Name         :      ",f)
            print("   Mother's Name         :      ",m)
            print("   Password              :      ",passwd)
            print("   Age                   :      ",a)
            print("   Address               :      ",ad)
            print("   Contact No            :      ",c)
            print("   Class 10th Marks      :      ",ma)
            print("   Class_12th_roll_no    :      ",ro)
            print("   Fathers_Occupation    :      ",oc)
            db.close()

        self.main_page()

    def feedetails(self, isback = False):
        self.clear()
        header()
        print()

        if isback:
            print('Please Enter a valid Roll No & Password')
            print()
        
        no=int(input("Enter Roll No: "))
        passw=int(input("Enter Password: "))
        db = database.initialize()
        cursor= db.cursor()
        st= "SELECT Roll_no, Students_name from Student_basic where Roll_no={} and Password={} ".format(no,passw)
        cursor.execute(st)
        data=cursor.fetchall()
        count=len(data)
        if count == 0 :
            self.subjectopt(isback = True)
        else:
            for row in data:
                rollno,n=row
            st2= "SELECT Subject_1, Subject_2, Subject_3,Subject_4, Subject_5 from Student_subjectopt where Roll_no={}".format(rollno)
            cursor.execute(st2)
            data2=cursor.fetchall()
            for row in data2:
                ap1,ap2,ap3,ap4,ap5=row
            st3= "SELECT * from Student_feedetails where Roll_no={}".format(rollno)
            cursor.execute(st3)
            data3=cursor.fetchall()
            for row2 in data3:
                rollno,n,f1,f2,f3,f4,f5,f6,f7,fee=row2
            st2= "SELECT Fee_status from Student_feedata where Roll_no={}".format(rollno)
            cursor.execute(st2)
            data2=cursor.fetchone()
            for row in data2:
                st=row
            if st == 'Paid':
                sta = ("You have already submitted a fees!!!!!!!")
            elif st == 'Not Paid':
                sta = ("""You have not submitted a fees till now!!!!!!!
                            Please Submit on a time...........""")
            print("   Student Rollno            :      ",rollno)
            print("   Student Name              :      ",n)
            print('')
            print("   Educational Fees:-")
            print("    Fees Of Subject_1",ap1,"  :      ",f1)
            print("    Fees Of Subject_2",ap2,"  :      ",f2)
            print("    Fees Of Subject_3",ap3,"  :      ",f3)
            print("    Fees Of Subject_4",ap4,"  :      ",f4)
            print("    Fees Of Subject_5",ap5,"  :      ",f5)
            print('')
            print("   Extra Fees(if applied):-")
            print("    Fees Of Hostel   :      ",f4)
            print("    Fees Of Canteen  :      ",f5)
            print('')
            print("    Total Fee You Have to pay is   :",fee)
            print('')
            print('')
            print("     ******",sta,"******")
            db.close()
            
        input("\nEnter to go back to main menu.")
        Student()

    def pay(self, rollNo):
        db = database.initialize()
        cursor = db.cursor()
        st2= "SELECT Payable_amount from Student_feedata where Roll_no={}".format(rollNo)
        cursor.execute(st2)
        data2=cursor.fetchone()
        for row in data2:
            st=row
        print("You Have to Pay Amount of ",st)
        card=int(input("Enter a our card number: "))
        amou=int(input("Enter a Amount :"))
        otp=int(input("Enter OTP :"))
        cd=str(card)
        ot=str(otp)
        counto=len(ot)
        countc=len(cd)
        if countc == 7 and counto == 5 and amou == st:
            cond="UPDATE Student_feedata SET Fee_status = '{}' WHERE Roll_no = {} ".format('Paid', rollNo)
            cursor.execute(cond)
            db.commit()
            db.close()
            print( "Your Fees is submitted successfully!!!" )
            input("\nEnter to go back to main menu.")
            Student()
        elif countc == 7 and counto == 5 and amou != st:
            print("Please input a correct amount...." )
            self.pay(rollNo)
        else :
            print("Please input a valid card number or OTP")
            self.pay(rollNo)

    def payment(self, isback = False):
        self.clear()
        header()
        print()

        if isback:
            print('Please Enter a valid Roll No & Password')
            print()

        no = int(input("Enter Roll No: "))
        passw = int(input("Enter Password: "))
        db = database.initialize()
        cursor = db.cursor()
        st = "SELECT Roll_no, Students_name from Student_basic where Roll_no={} and Password={} ".format(no, passw)
        cursor.execute(st)
        data = cursor.fetchall()
        count = len(data)
        if count == 0:
            db.close()
            self.payment(isback=True)
        else:
            st2 = "SELECT Fee_status from Student_feedata where Roll_no={}".format(no)
            cursor.execute(st2)
            data2 = cursor.fetchone()
            st = data2[0]
            if st == 'Paid':
                print("You have already submitted a fees!!!!")
                input("\nEnter to go back to main menu.")
                Student()
            elif st == 'Not Paid':
                self.pay(no)

    def result(self, isback = False):
        self.clear()
        header()
        print()

        if isback:
            print('Please Enter a valid Roll No & Password')
            print()

        no=int(input("Enter Roll No: "))
        passw=int(input("Enter Password: "))
        db = database.initialize()
        cursor= db.cursor()
        st= "SELECT Roll_no, Students_name from Student_basic where Roll_no={} and Password={} ".format(no,passw)
        cursor.execute(st)
        data = cursor.fetchall()
        count = len(data)
        if count == 0 :
            db.close()
            self.result(isback=True)
        else:
            for row in data:
                rollno, n = row
            st2= "SELECT Marks_in_subject_1, Marks_in_subject_2, Marks_in_subject_3, Marks_in_subject_4, Marks_in_subject_5,Percentage, Overall from Student_marks where Roll_no={}".format(no)
            cursor.execute(st2)
            data2 = cursor.fetchall()

            for row in data2:
                ms1, ms2, ms3, ms4, ms5, p, o = row
            
            if o is None:
                print("Results not announced yet!")
                input("\nEnter to go back to main menu.")
                db.close()
                Student()
            else:
                print("   Student Rollno         :     ",rollno)
                print("   Student Name           :     ",n)
                print("   Marks in subject 1     :     ",ms1)
                print("   Marks in subject 2     :     ",ms2)
                print("   Marks in subject 3     :     ",ms3)
                print("   Marks in subject 4     :     ",ms4)
                print("   Marks in subject 5     :     ",ms5)
                print()
                print("   Percentage             :     ",p,"%")
                print()
                print("   Overall                :     ",o)
                separator()
            
        print()

        menu_options = [
            ("SUCCESS GRAPH(in Pie Chart)", 1),
            ("SUCCESS GRAPH(in Bar Graph)", 2),
            ("EXIT", 3),
        ]

        for option, value in menu_options:
            print(f"{'For'.rjust(10)} {option.ljust(30)} -> (press {value})")
        print()
        ch = int(input(f"Enter Your Choice: ".rjust(26)))

        if ch in [1, 2]:
            st2= "SELECT Subject_1, Subject_2, Subject_3, Subject_4, Subject_5 from Student_subjectopt where Roll_no={}".format(no)
            cursor.execute(st2)
            subjects = cursor.fetchall()[0]

        if ch == 1:
            val=[ms1,ms2,ms3,ms4,ms5]
            countri=val
            marks = subjects
            py.title("RESULT (in form of pie chart)")
            py.axis("equal")
            py.pie(countri, labels = marks, autopct = "%2.2f%%")
            py.savefig("Resultpiechart")
            py.show()
        elif ch == 2:
            val1=[ms1,ms2,ms3,ms4,ms5,p]
            head=list(subjects) + ['Percentage']
            py.title("RESULT (in form of bar graph)")
            py.bar(head,val1,color='blue')
            py.xlabel('MARKS')
            py.ylabel('OVERALL PERFORMANCE')
            py.savefig("Resultgraph")
            py.show()
        db.close()
        input("\nEnter to go back to main menu.")
        Student()