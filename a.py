"""
#1) Add the project title and topics.
   a) Label the program as "Score Tracker".
   b) Mention topics like Big-O, Omega, Theta, and best/worst/average cases.

2) Create the leaderboard.
   a) Store player names in a list.
   b) Store player scores in another list.
   c) Find the total number of players using `len()`.
   d) Print all players with their scores.

3) Demonstrate Theta(1).
   a) Access the first score directly using index `0`.
   b) Show that direct access always takes 1 step.
   c) Label it as `Theta(1)` because the cost stays constant.

4) Demonstrate linear search.
   a) Search for a player name by checking the list from the beginning.
   b) Count each check as one step.
   c) Show best case as `Omega(1)` when the player is found first.
   d) Show worst case as `O(n)` when the player is found last.

5) Demonstrate pair checking.
   a) Set a target score sum.
   b) Use nested loops to compare every pair of players.
   c) Count each comparison as one step.
   d) Print pairs whose scores match the target sum.
   e) Label the operation as `O(n^2)`.

6) Print the asymptotic summary.
   a) Explain `Theta(1)` for direct index access.
   b) Explain `Omega(1)` for best-case search.
   c) Explain `O(n)` for worst-case search.
   d) Explain `O(n^2)` for pair checking.

7) End with the main idea.
   a) Drop constants.
   b) Ignore smaller terms.
   c) Keep the fastest-growing term.
"""
names=["Aarav","Priya","Dev","Meera","Kabir"]
scores=[90,75,88,62,95]
n=len(scores)
print("===Score Tracker(n=",n,"players)===")
for i in range(n):
    print(i+1,".",names[i],":",scores[i],sep="")
print()
#Part 2
steps=1
print("Score at index 0:",scores[0],"|steps=",steps,"|Theta(1)-tight bound")
print()
#Part 3
target="Aarav"
steps=0
for name in names:
    steps+=1
    if name==target:
        break
print("Search for",target,"steps=",steps,"Omega(1)")

target="Kabir"
steps=0
for name in names:
    steps+=1
    if name==target:
        break
print("Search for",target,"steps=",steps,"O(n)=",n,"worst case upper bound")
print()
steps=0
target_sum=150
print("Pairs with total score=",target_sum,":")
for i in range(n):
    for j in range(i+1,n):
        steps+=1
        if scores[i]+scores[j]==target_sum:
            print("",names[i],"+",names[j],"=",scores[i]+scores[j])
print("Total comparions:",steps,"O(n^2)-drop constants,keep n^2")
print()