import os
import time
import shutil
import webbrowser
from datetime import date

from ABC.pages import (
    Admission,
    Announcement,
    Career,
    contact,
    Downloads,
    Login,
    successGraph
)
from .pages import (
    about,
    header
)
from .utils import (
    center,
    separator
)


class A_B_C_INSTITUTE_OF_TECHNOLOGY:

    clear = staticmethod(lambda: os.system('cls'))
    TERMINAL_WIDTH = staticmethod(lambda: shutil.get_terminal_size().columns)

    def __init__(self) -> None:
        self.clear()

        self.WELCOME_FILE = os.path.join(os.getcwd(), "ABC", "docs", "welcome.pdf")
        self.welcome()
        self.main_page()

    def welcome(self):
        webbrowser.open(self.WELCOME_FILE)
        pass

    def main_page(self):
        t = time.localtime()
        Time = time.strftime("%I:%M:%S %p", t)
        today = date.today()
        Date= today.strftime("%d/%B/%Y")
        center(" ")
        center("A.B.C INSTIUTE OF TECHNOLOGY")
        center("ADDRESS:-2400 6th St NW")
        center("Washington, DC 20059, United States")
        center("PHONE no. +1 202-806-6100")
        separator()
        print(f"{Time.ljust(self.TERMINAL_WIDTH() - len(Date))}{Date}")

        center("We Warmly Welcomes to you!!!!!!!!!!!!!!!")

        print()
        print()

        self.choice()

    def options(self, ch: int):
        match ch:
            case 1:
                self.main_page()
            case 2:
                about()
                self.choice()
            case 3:
                Admission()
                separator()
                self.clear()
                header()
                self.choice()
            case 4:
                successGraph()
                separator()
                self.clear()
                header()
                self.choice()
            case 5:
                Announcement()
                self.choice()
            case 6:
                Career()
                separator()
                self.clear()
                header()
                self.choice()
            case 7:
                Downloads()
                separator()
                self.clear()
                header()
                self.choice()
            case 8:
                contact()
                self.choice()
            case 9:
                Login()
                separator()
                self.clear()
                header()
                self.choice()
            case 10:
                self.exit()
            case _:
                header()
                self.choice(capture_res=False)
                print()
                print("Please enter a value in between 1-10".rjust(5))
                ch = int(input(f"{'Enter Your Choice:- '.rjust(10)}"))
                separator()
                self.clear()
                self.options(ch)

    def choice(self, capture_res=True):
        menu_options = [
            ("HOME", "1"),
            ("ABOUT", "2"),
            ("ADMISSION", "3"),
            ("SUCCESS GRAPH", "4"),
            ("LATEST ANNOUNCEMENT", "5"),
            ("CAREER @ INSTITUTE", "6"),
            ("DOWNLOADS", "7"),
            ("CONTACT US", "8"),
            ("LOGIN", "9"),
        ]

        print("\nMENU:-")

        for option, value in menu_options:
            print(f"{'For'.rjust(10)} {option.ljust(30)} -> (press {value})")

        print()
        print(f"For EXIT (press 10)".rjust(self.TERMINAL_WIDTH()))
        print()
        print()

        if capture_res:
            ch = int(input(f"Enter Your Choice: ".rjust(26)))
            separator()
            self.clear()
            self.options(ch)

    def exit(self):
        header()
        center("Thanks for visiting")
        center("We hope you enjoyed!!!!!!!!")