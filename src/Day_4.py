# Random Module
import random

# Random interger
random_integer = random.randint(1, 10)
print(random_integer)
# Random float
random_float = random.random() * 5
print(random_float)

# Exercise 1: Heads or Tails
"""write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails"."""
import random
random_integer = random.randint(0, 1)
if random_integer == 1:
    print("Heads")
else:
    print("Tails")

# Lists - Stores heterogenious data, Ordered, Mutable
# Support indexing (+ve and -ve), slicing etc 
states = ["Maharashtra", "Karnataka", 'UP', 'MP']
print(states[1])
print(states[-1])
print(states[1:3])

# Exercise 2: Banker roulette
"""You are going to write a program that will select a random name from a list of names. The person selected will have 
to pay for everybody's food bill."""
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
number = random.randint(0, len(names)-1)
name = names[number]
print(f"{name} is going to buy the meal today!")

# Nested lists
fruits = [["Apple", 200], ["Mango", 100]]

# Exercise 3: Treasure Map
"""Write a program that will mark a spot with an X

Example 1-
Input:
Where do you want to put the treasure? 23
Output:
['⬜️', '️⬜️', '️⬜️']
['⬜️', '⬜️', '️⬜️']
['⬜️️', 'X', '⬜️️']

Example 2-
Input:
Where do you want to put the treasure? 31
Output:
['⬜️', '️⬜️', '️X']
['⬜️', '⬜️', '️⬜️']
['⬜️️', '⬜️', '⬜️️']
"""

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
col = int(position[0]) - 1
row = int(position[1]) - 1
map[row][col] = "X"
print(f"{row1}\n{row2}\n{row3}")