import os

from ABC.pages import header
from ABC.utils import separator

from .student import Student
from .faculty import Faculty


class Login:
    def __init__(self) -> None:
        self.clear = staticmethod(lambda: os.system('cls'))

        separator()
        self.clear()
        header()
        print()
        self.main_page()

    def main_page(self):
        menu_options = [
            ("STUDENT LOGIN", "1"),
            ("TEACHER LOGIN", "2"),
            ("GO TO BACK", "3"),
        ]

        print("\nMENU:-")

        for option, value in menu_options:
            print(f"{'For'.rjust(10)} {option.ljust(30)} -> (press {value})")

        print()
        ch = int(input(f"Enter Your Choice: ".rjust(26)))
        if ch == 1:
            Student()
        elif ch == 2:
            Faculty()
        elif ch == 3:
            return
        else:
            Login()
