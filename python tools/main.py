import PIL
import time
import os
from PIL import Image

print("You have 3 times for convert image to PDF")
print("Do you want input one image or two or three images? (1, 2, or 3)")
answ = input('Answer: ')
if answ == '1':
    usr = input("Input location image: ")
    img = Image.open(usr)
    print("Converting...") == time.sleep(2)
    img.save("output.pdf", "PDF")
    print("Successfully!")
    exit()
elif answ == '2':
    usr1 = input("Input location image 1: ")
    usr2 = input("Input location image 2: ")
    img1 = Image.open(usr1)
    img2 = Image.open(usr2)
    print("Converting...") == time.sleep(2)
    img1.save("output.pdf", "PDF", append_images=[img2], save_all=True)
    print("Successfully!")
    exit()
elif answ == '3':
    usr1 = input("Input location image 1: ")
    usr2 = input("Input location image 2: ")
    usr3 = input("Input location image 3: ")
    img1 = Image.open(usr1)
    img2 = Image.open(usr2)
    img3 = Image.open(usr3)
    print("Converting...") == time.sleep(2)
    img1.save("output.pdf", "PDF", append_images=[img2, img3], save_all=True)
    print("Successfully!")
    exit()
else:
    print("Invalid input. Please enter 1, 2, or 3.")
    exit()