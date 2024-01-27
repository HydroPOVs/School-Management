import time
import shutil
from datetime import date

from ABC.utils import (
    center,
    separator
)

def header():
    TERMINAL_WIDTH = shutil.get_terminal_size().columns

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
    print(f"{Time.ljust(TERMINAL_WIDTH - len(Date))}{Date}")