number=int(input("Enter Number to check"))
print("Number to be checked:",number)

if number%2==0 :
    print("This is an even number")
else :
    print("This is an odd number")
height = float(input("Enter your height in cm"))
weight =float(input("Enter your weight in kg"))
 
BMI = weight/(height/100)**2
print("Your BMI is",BMI)
if BMI<=18.4:
    print("You are underweight")
elif BMI<=24.9:
    print("You're healthy")
elif BMI<=29.9:
    print("You're overweight")
elif BMI<=34.9:
    print("You are severly overweight")
elif BMI<=39.9:
    print("You are obese")
else:
    print("You are severly obese")
num = int(input("Enter a number"))
print("Number to check",num)
if num>0 :
    print("It is a positive number")
elif num==0:
    print("It is neither positive nor negative")
else:
    print ("it is a negative number")