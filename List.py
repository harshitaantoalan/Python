lst=['Apple','Guava','Mango','Banana','Kiwi']

print("Length of list",len(lst))
print("First Element",lst[0])
print("Last Element:",lst[-1])

lst.append('Papaya')
print("Updated List:",lst)

lst.remove('Guava')
print("Updated List:",lst)

lst.sort()
print("Sorted List:",lst)

lst.pop(1)
print("Updated List:" ,lst)

lst.reverse()
print("Reversed List:",lst )
print("Multiplication on List:",lst*2)

lst=lst[:4]
print("Sliced List:",lst)

lst.clear()
print("Updated List:",lst)
# dictionary
my_dict={}
my_dict={1:'apple',2:'ball'}
my_dict={'name':'Jack','age':26}
print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age']=27
print(my_dict)
#add item
my_dict['address']='Downtown'
print(my_dict)
#remove particular element
my_dict.pop('age')
print(my_dict)
#List addition

def test(ls):
    result={}
    for item in ls:
        result[item[0]]=item[1:]
        return result
students=[[1,'Jean Cstro','V'],[2,'Lula Powell','V'],[3,'Brian','VI'],[4,'Lynne','VI'],[5,'Zach','VII']]
print("\nOriginal list of lists:")

print(students)
print("\nConverted lists to a dictionary")
print(test(students))
