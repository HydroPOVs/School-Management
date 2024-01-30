import os
import webbrowser

from ABC.pages import header
from ABC.utils import separator


class Downloads:
    def __init__(self) -> None:
        self.exitCmd = None
        self.clear = staticmethod(lambda: os.system('cls'))
        self.DOCS_PATH = os.path.join(os.getcwd(), "ABC", "docs")

        separator()
        self.clear()
        header()
        print()
        self.main_page()

    def main_page(self):
        print()
        year_options = [year for year in os.listdir(self.DOCS_PATH) if os.path.isdir(os.path.join(self.DOCS_PATH, year))]

        print("\nMENU:-\n")

        print(f"Select Downloads Year:-")
        for index, year in enumerate(year_options):
            print(f"{'For'.rjust(10)} {year.ljust(30)} -> (press {(index + 1)})")
        print()

        year = int(input(f"Enter Your Choice: ".rjust(26)))

        if year not in list(range(1, len(year_options)+1)):
            year = len(year_options)

        year = year_options[year - 1]

        separator()
        self.clear()
        header()
        print()

        menu_options = [
            (file, i+1) for i, file in enumerate(os.listdir(os.path.join(self.DOCS_PATH, year)))
            if os.path.isfile(os.path.join(self.DOCS_PATH, year, file))
        ]

        print(f"\nRate List & Application form of {year.rjust(5)}:-")
        for option, value in menu_options:
            print(f"{'For'.rjust(10)} {option.rsplit(' ', 1)[0].ljust(30)} -> (press {value})")
        print()

        print(f"{'For'.rjust(10)}", " GO TO BACK".ljust(30), "->", f"(press {len(menu_options)+1})")
        print()

        ch = int(input(f"Enter Your Choice: ".rjust(26)))

        self.exitCmd = len(menu_options)+1

        match ch:
            case self.exitCmd:
                return
            case _:
                if ch in range(1, len(menu_options)+1):
                    file = os.path.join(os.getcwd(), "ABC", "docs", year, menu_options[ch-1][0])
                    webbrowser.open(file)
                    Downloads()
                else:
                    return Downloads()

        webbrowser.open(file)
        Downloads()
