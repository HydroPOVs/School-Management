import os

from .pages import header
from .utils import separator, center
from .main import A_B_C_INSTITUTE_OF_TECHNOLOGY

if __name__ == "__main__":
    school = None
    try:
        school = A_B_C_INSTITUTE_OF_TECHNOLOGY()
    except KeyboardInterrupt:
        separator()
        os.system('cls')
        header()
        center("Thanks for visiting")
        center("We hope you enjoyed!!!!!!!!")