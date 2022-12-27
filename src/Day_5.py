# Loops
# For Loop
# fruits = ["Apple", "Pear", "Mango"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie.")

# Exercise 1: Average Student Height
"""Calculate average sudents height from given heights.

Note - sum, len function not allowed.

Example Input
156 178 165 171 187
In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]
Example Output
171"""
# student_heights = input("Input a list of student heights ").split()
# count, sum = 0, 0
# for height in student_heights:
#     sum += int(height)
#     count += 1
# avg_height = round(sum / count)
# print(avg_height)

# Exercise 2: Highest Score in The Class
"""write a program that calculates the highest score from a List of scores.
e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
Important you are not allowed to use the max or min functions. The output words must match the example. i.e
The highest score in the class is: x

Example Input:
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]
Example Output
The highest score in the class is: 91"""
# student_scores = input("Input a list of student scores ").split()
# max_score = 0
# for score in student_scores:
#     score = int(score)
#     if score > max_score:
#         max_score = score
# print(f"The highest score in the class is: {max_score}")

# Exercise 3: Add Even Numbers
"""write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2
and the last one is 100:
i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
Important, there should only be 1 print statement in your console output. It should just print the final total and not 
every step of the calculation."""
# total = 0
# for number in range(2, 101, 2):
#     total += number
# print(total)

# Exercise 4: FizzBuzz Game
"""write a program that automatically prints the solution to the FizzBuzz game.

Your program should print each number from 1 to 100 in turn.

When the number is divisible by 3 then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz".` 
And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print 'FizzBuzz'
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
... """
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


