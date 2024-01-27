import shutil
from ABC.pages import header
from ABC.utils import center


class announcement():

    def __init__(self) -> None:
        self.TERMINAL_WIDTH = staticmethod(lambda: shutil.get_terminal_size().columns)

        header()
        print()
        self.main_page()

    def main_page(self):
        center("-:LATEST ANNOUNCEMENT:-")
        print()
        print("        1. New Admission started from now so, please Hurry up!!!!!! (last date 31/03/2020) **new** ")
        print("        2. Result of student of session 2019-2020 is now available (for result login as student) **new** ")
        print("        3. For New Admission registration starting from 23/12/2019")
        print("        4. Result of student of session 2019-2020 will be available on 20/12/2019.")
        print("        5. Teachers are requested to submit a result of there class on website using teachers login portal in login portal, (last date 1/12/2019)")
        print("        6. For New Admission registration starting soon, for more updates come again")
        print("        7. Result of student of session 2019-2020 will be available soon.")
        print("        8. For New Admission registration starting soon.")
        print("        9. Our school is organising a Scholarship Exam interested contact to your respective Head Teachers of there Department. EXAM DATE:- 25/11/2019.")
        print()
        print(f"more.......".rjust(self.TERMINAL_WIDTH()))