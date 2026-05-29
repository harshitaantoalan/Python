file=open('sample.txt')
print(file.read())
file.close()

file_write= open('sample.txt','w')
file_write.write("File in write mode....")
file_write.write("Hi I am Penguin I am 1 year old")
file_write.close()

file_append=open('sample.txt','a')
file_append.write("\n File in append mode...")
file_append.write("Hi i am Penguin,I'm a year old")
file_append.close()

file=open('sample.txt','r')
Counter=0
Content=file.read()
CoList=Content.split("\n")
for i in CoList:
    if i:
        Counter+=1
print("This is the number of lines in the file ")
print(Counter)