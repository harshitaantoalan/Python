num=int(input("Enter number to be checked"))
if num>50:
    print("It is greater than 50")
    if num%2==0:
        print("It is an even number")
    else:
        print("It is a odd number")

else:
    print("Number is less than 50")