
#1) Add the project title and topics.
  # a) Label the program as an algorithm analysis activity.
  # b) Mention the topics: algorithm, pseudocode, time complexity, space complexity, and efficiency comparison.
n=4
print("===Counting game points(n=",n,"rounds)===")
print()

#2) Define the problem.
   #a) Set `n = 4` rounds.
   #b) Explain that each round gives points equal to its round number.
   #c) Print the activity heading.
total =n*(n+1)//2
print("Formula way:total=",total,"|steps=1")


#3) Solve using the formula method.
   #a) Use the formula `n * (n + 1) // 2`.
   #b) Store the answer in `total`.
   #c) Print the total and show that it takes only 1 step.
total=0
steps=0
for round_num in range(1,n+1):
   total+=round_num
   steps+=1
print ("Loop way  : total=",total,"|steps=",steps)

#4) Solve using the loop method.
   #a) Start `total` and `steps` from 0.
   #b) Use a `for` loop from 1 to `n`.
   #c) Add each round number to the total.
   #d) Count one step for each loop run.
   #e) Print the total and number of steps.
total=0
steps=0
for round_num in range(1,n+1):
   for point in range(1,round_num+1):
      total+=1
      steps+=1
print("Nested loop:total=",total,"| steps=",steps)

#5) Solve using the nested loop method.
   #a) Start `total` and `steps` from 0.
   #b) Use one loop for rounds.
   #c) Use another loop to add points one by one.
   #d) Count each inner loop run as a step.
   #e) Print the total and number of steps.
n=10
nested_steps=0
for round_num in range(1,n+1):
   for point in range(1,round_num+1):
      nested_steps+=1


print()
print("===Now with n=",n,"rounds===")
print("Formula way: steps=1 (always just 1!)")
print("Loop way: steps =",n)
print("Nested loop: steps=",nested_steps,"(grows much faster!)")
print()
print("Same answer-but very different costs. That is time complexity")