name ="Penguin"
age =15
is_student=True
weight=38.5

print("Name:",name)
print("DataType of name is ",type(name))
print("Age", age)
print("Data Type of Age is",type(age))
print("is_student:", is_student)
print("DataType of is_student is",type(is_student))
print("Weight:",weight)
print("Datatype of weight is ",type(weight))

print("\n After type casting")
age=str(age)
print(age)
print("Datatype of age is",type(age))
weight=int(weight)
print(weight)
print ("Datatype of weight is" ,type(weight))
#Python operators
num1 =50
num2=30
print("Number 1",num1)
print("Number 2",num2)
print("Addition",num1 + num2)
print("Difference",num1 - num2)
print("Product",num1 * num2)
print("Division",num1 / num2)
print("Floor division",num1 // num2)
print("Modulus operation",num1 % num2)
print("Square",num2 ** 2)
print("Square root",num1**0.5)

print("Equal?",num1==num2)
print("Number 1 greater?",num1>num2)
print("Number 2 greater?",num1<num2)
print("Not Equal?",num1!=num2)
num1 += 10
print(num1)

first_name= "Harshita"
last_name="Alan"
full_name= first_name+last_name
example ="Haa"*5
print("First name",first_name)
print("Last_name",last_name)
print("Full name",full_name)
word="Coding"
print("Length of the string:",len(word))
print("1st letter of the string:",word[0])
print("Last letter of the string",word[-1])
print("String sliced:",word[0:3])
