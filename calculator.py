import time
print("WELCOME TO YANN CALCULATOR")
select = int(input("select calculation [1.Plus, addiction, times. 2.times decimal]: "))
if select == 1:
    first_number = int(input("Input first number: "))
    second_number = int(input("Input second number: "))
    choose = int(input("Select type [1.Plus,2.addiction, 3,times]:"))
    print("Loading.....")
    time.sleep(3)
    if choose == 1:
        print("Results:", first_number + second_number)
    elif choose == 2:
        print("Results:", first_number - second_number)
    elif choose == 3:
        print("Results:", first_number * second_number)
    else:
        print("please enter the correct number!")
        exit()
elif select == 2:
    first_number_decimal = float(input("Input first number:" ))
    second_number_decimal = float(input("Input second number:"))
    print("Loading....")
    time.sleep(1)
    print("Results:", first_number_decimal * second_number_decimal)
