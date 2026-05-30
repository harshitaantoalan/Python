file=open('sample.txt','r')
print("\n Read in parts\n")
print(file.read(8))
file.close()

file=open('sample.txt','r')
print("Reading the first line")
print(file.readline())
file.close()

file=open('sample.txt','r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())

file1=open('sample.txt','r')
file2=open('sample2.txt','w')
for line in file1.readlines():
    if not(line.startswith('Coding')):
        print(line)
        file2.write(line)

file2.close()
file1.close()

fn=open('sample.txt','r')
fn1=open('oddnosample.txt','w')
cont=fn.readlines()
type(cont)
for i in range(1,len(cont)+1):
    if(i%2!=0):
        fn1.write(cont[i-1])
    else:
        pass
fn1.close()

