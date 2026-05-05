def intro(name):
    print("Hello,Good Morning I am", name)
user_name=input("Enter your name")
intro(user_name)
def recur_factorial(number):
    if number==1:
        return number
    else:
        return number*recur_factorial(number-1)
n=int(input("Enter a number:"))
if n<0:
    print("Sorry factorial does not exist for negative numbers")
elif n==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of ",n,"is",recur_factorial(n))
print("Welcome to calculator")
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("1. Addition\n 2.Subtraction\n 3.Multiplication\n 4.Divison")
choice=int(input("Enter you choice:"))
num1=int(input("Enter number 1"))
num2=int(input("Enter number 2:"))
if choice==1:
    print("Addition:",add(num1,num2))
elif choice==2:
    print("Subtraction:",sub(num1,num2))
elif choice ==3:
    print("Multiplication:",multiply(num1,num2))
elif choice==4:
    print("Division:",divide(num1,num2))
else:
    print("Invalid choice")
        