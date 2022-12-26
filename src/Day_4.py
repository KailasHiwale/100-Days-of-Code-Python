# Random Module
import random

# Random interger
random_integer = random.randint(1, 10)
print(random_integer)
# Random float
random_float = random.random() * 5
print(random_float)

# Exercise 1: Heads or Tails
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