import docx2pdf
from docx2pdf import convert
import os
import time

def office():
    print("Loading data.....") == time.sleep(1)
    print("INFORMATION! DO NOT ENTER PATH WITH QUOTATION MARK!")
    usr1 = input("Enter the path of the Microsoft Office file: ")

    if usr1 == "":
        print("You have not Enter the path please try again!")
        os.system("py office.py")
    else:
        print("Process convert file.....") == time.sleep(2)
        convert(usr1)
        print("Convert succesfully!")
        os.system("py office.py")