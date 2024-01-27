import os
import webbrowser

from ABC.pages import header
from ABC.utils import separator

class downloads():
    def __init__(self) -> None:
        self.clear = staticmethod(lambda: os.system('cls'))

        self.Employment_Application_2019 = os.path.join(os.getcwd(), "ABC", "docs", "2019-20", "Employment Application 2019-20.pdf")
        self.Canteen_Menu_Rate_List_2019 = os.path.join(os.getcwd(), "ABC", "docs", "2019-20", "Canteen Menu & Rate List 2019-20.pdf")
        self.Fees_Structure_2019 = os.path.join(os.getcwd(), "ABC", "docs", "2019-20", "Fees Structure 2019-20.pdf")
        self.Hostel_Room_Type_Charge_List_2019 = os.path.join(os.getcwd(), "ABC", "docs", "2019-20", "Hostel Room Type & Charge List 2019-20.pdf")

        self.Employment_Application_2018 = os.path.join(os.getcwd(), "ABC", "docs", "2018-19", "Employment Application 2018-19.pdf")
        self.Canteen_Menu_Rate_List_2018 = os.path.join(os.getcwd(), "ABC", "docs", "2018-19", "Canteen Menu & Rate List 2018-19.pdf")
        self.Fees_Structure_2018 = os.path.join(os.getcwd(), "ABC", "docs", "2018-19", "Fees Structure 2018-19.pdf")
        self.Hostel_Room_Type_Charge_List_2018 = os.path.join(os.getcwd(), "ABC", "docs", "2018-19", "Hostel Room Type & Charge List 2018-19.pdf")
        
        separator()
        self.clear()
        header()
        print()
        self.main_page()

    def main_page(self):
        print()
        year_options = [
            "2019-20",
            "2018-19",
        ]
        menu_options = [
            ("Application Form", 1),
            ("Canteen Menu & Rate List", 2),
            ("Fees Structure", 3),
            ("HostelRoomType & ChargeList", 4),
        ]

        print("\nMENU:-")

        for index, year in enumerate(year_options):
            print(f"Rate List & Application form of {year.rjust(5)}:-")
            for option, value in menu_options:
                print(f"{'For'.rjust(10)} {option.ljust(30)} -> (press {(index*4)+value})")
            print()

        print()
        print(f"{'For'.rjust(10)}", " GO TO BACK".ljust(30),"->", "(press 9)")
        
        print()
        ch = int(input(f"Enter Your Choice: ".rjust(26)))
        if ch == 1:
            webbrowser.open(self.Employment_Application_2019)
            downloads()
        elif ch == 2:
            webbrowser.open(self.Canteen_Menu_Rate_List_2019)
            downloads()
        elif ch == 3:
            webbrowser.open(self.Fees_Structure_2019)
            downloads()
        elif ch == 4:
            webbrowser.open(self.Hostel_Room_Type_Charge_List_2019)
            downloads()
        elif ch == 5:
            webbrowser.open(self.Employment_Application_2018)
            downloads()
        elif ch == 6:
            webbrowser.open(self.Canteen_Menu_Rate_List_2018)
            downloads()
        elif ch == 7:
            webbrowser.open(self.Fees_Structure_2018)
            downloads()
        elif ch == 8:
            webbrowser.open(self.Hostel_Room_Type_Charge_List_2018)
            downloads()
        elif ch == 9:
            return
        else:
            downloads()