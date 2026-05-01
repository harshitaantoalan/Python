num=int(input("Enter number:"))
for i in range(1,11):
    print(f"{num} x {i}={num*i}")

n=int(input("Enter number of rows:"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end ='')
    print()