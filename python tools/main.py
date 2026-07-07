import PIL
import pdf2image
from pdf2image import convert_from_path
import time
import os
from PIL import Image

print("Welcome to PDF Converter Tool")
print("VERSION : 1.0.2 ")
select = input("Select type [1] PDF to Image [2] Image to PDF: ")
if select == "2":
    usr1 = input("Enter location of the image: ")
    ask1 = input("Do you want to add more images? (y/n): ")
    if ask1 == "y":
        usr2 = input("Enter location of the image: ")
        ask2 = input("Do you want to add more images? (y/n): ")
        if ask2 == "y":
            usr3 = input("Enter location of the image: ")
            ask3 = input("Do you want to add more images? (y/n):")
            if ask3 == "y":
                usr4 = input("Enter location of the image: ")
                ask4 = input("Do you want to add more images? (y/n): ")
                if ask4 == "y":
                    usr5 = input("Enter location of the image: ")
                    print("Converting images to PDF...") == time.sleep(2)
                    img1 = Image.open(usr1)
                    img2 = Image.open(usr2)
                    img3 = Image.open(usr3)
                    img4 = Image.open(usr4)
                    img5 = Image.open(usr5)
                    img1.save("5 images.pdf", "PDF", resolution=100.0, save_all=True, append_images=[img2, img3, img4, img5])
                    print("Images converted to PDF successfully! Saved as 5 images.pdf")
                    exit()
                elif ask4 == "n":
                    print("Converting images to PDF...") == time.sleep(2)
                    img1 = Image.open(usr1)
                    img2 = Image.open(usr2)
                    img3 = Image.open(usr3)
                    img4 = Image.open(usr4)
                    img1.save("4 images.pdf", "PDF", resolution=100.0, save_all=True, append_images=[img2, img3, img4])
                    print("Images converted to PDF successfully! Saved as 4 images.pdf")
                    exit()
                else:
                    print("Invalid input, we will proceed with 4 images only.")
                    print("Converting images to PDF...") == time.sleep(2)
                    img1 = Image.open(usr1)
                    img2 = Image.open(usr2)
                    img3 = Image.open(usr3)
                    img4 = Image.open(usr4)
                    img1.save("4 images.pdf", "PDF", resolution=100.0, save_all=True, append_images=[img2, img3, img4])
                    print("Images converted to PDF successfully! Saved as 4 images.pdf")
                    exit()
        elif ask2 == "n":
            img1 = Image.open(usr1)
            img2 = Image.open(usr2)
            print("Converting images to PDF...") == time.sleep(2)
            img1.save("2 images.pdf", "PDF", resolution=100.0, save_all=True, append_images=[img2])
            print("Images converted to PDF successfully! Saved as 2 images.pdf")
            exit()
        else:
            print("Invalid input, we will proceed with 2 images only.")
            img1 = Image.open(usr1)
            img2 = Image.open(usr2)
            print("Converting images to PDF...") == time.sleep(2)
            img1.save("2 images.pdf", "PDF", resolution=100.0, save_all=True, append_images=[img2])
            print("Images converted to PDF successfully! saved as 2 images.pdf")
            exit()
    elif ask1 == "n":
        img = Image.open(usr1)
        print("Converting image to PDF...") == time.sleep(2)
        img.save("image.pdf", "PDF", resolution=100.0)
        print("Image converted to PDF successfully! Saved as image.pdf")
        exit()
    else:
        print("Invalid input, Please try again.")
        exit()
elif select == "1":
    usrp1 = input("Enter location of the PDF: ")
    print("Converting PDF to images...") == time.sleep(2)
    pages = convert_from_path(usrp1, 500)
    for i, page in enumerate(pages):
        page.save(f'page_{i + 1}.png', 'PNG')
    print("PDF converted to images successfully! Saved as page_1.png, page_2.png, etc.")
    asking = input("Do you want to convert another PDF? (y/n): ")
    if asking == 'y':
        usrp2 = input("Enter location of the PDF: ")
        print("Converting PDF to images...") == time.sleep(2)
        pages = convert_from_path(usrp2, 500)
        for i, page in enumerate(pages):
            page.save(f'page_{i + 1}.png', 'PNG')
            print(f"page_{i + 1}.png saved successfully!")
    else:
        print("Thank you for using PDF Converter Tool!")
        exit()
else:
    print("Invalid selection, please try again.")
    os.system('py main.py')