total_sum=0
num=1
while num<=10:
    total_sum+=num
    num+=1
print(total_sum)
n=int(input("Enter a number:"))
if n>1:
    for i in range(2,int(n**0.5)+1):
        if num%i==0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")
else:
    print(f"{num }is not a prime number")