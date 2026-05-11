my_tuple=()
print(my_tuple)

my_tuple=(1,"Hello,",3.4)
print(my_tuple)

my_tuple=(1,2,3)
print(my_tuple)
my_tuple=('mouse',[8,4,6],(1,2,3))
print(my_tuple)

my_tuple=('p','e','r','m','i','t')
print(my_tuple[0])
print(my_tuple[5])
n_tuple=("mouse",[8,4,6],(1,2,3))
print(n_tuple[0][3])
print(n_tuple[1][1])
print("Sliced:", my_tuple[1:4])

for letter in(my_tuple):
    print("Hello",letter)
my_new=my_tuple+('a',)
print(my_new)
# set operation
my_set={1,2,2,3,4,4,4}
print("Set:",my_set)
my_set.add(5)
print("Updated set:",my_set)
set1=my_set
set2={2,4,4,6}
print("\nSet1:",set1)
print("Set 2:",set2)
print("Difference")
print(set1.difference(set2))
print("Symmetric difference")
print(set1.symmetric_difference(set2))
print(set1.union(set2))
print(set1.intersection(set2))