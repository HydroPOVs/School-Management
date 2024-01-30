import matplotlib.pyplot as py

from ABC.pages import header


def successGraph():
    header()
    Years = ['1865-1915', '1916-1966', '1967-2017', '2018-Till now']
    Number_of_Selections = [52550, 95580, 383622, 148757]
    py.title("A.B.C INSTIUTE OF TECHNOLOGY")
    py.bar(Years, Number_of_Selections, color='red')
    py.xlabel('Years')
    py.ylabel('Number of Selections')
    py.show()
