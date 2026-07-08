from tools import images
from tools import office
import os

print('Welcome to python tools')
asking1 = print("What do you want to convert")
choise = input("[1].Microsoft Office to PDF, [2].Images to PDF: ")
choint = int(choise)
if choint == 1:
    images.tool1()
elif choint == 2:
    office.office()
else:
    print("Wrong input! try again!")
    os.system("py main.py")