import random

lst = [33,45,67,89,37,28,63,96,58,30]


num = random.choice(lst)


while True:
    n = int(input("Enter the number you want to choose from the list: "))

    if n > num:
        print("Number is higher")
    elif n < num:
        print("Number is lower")
    else:
        print("You found the number")
        break



    