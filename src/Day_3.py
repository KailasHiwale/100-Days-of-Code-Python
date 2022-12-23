# Conditionals: if / elif / else

# Exercise 1: Odd even number
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("This is an even number.")
else:ß
    print("This is an odd number.")

# Exercise 2: Wight Indicator based on BMI.
""" Weight indicator based on the BMI value -
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese. """
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
height_float = float(height)
weight_float = float(weight)
bmi = round(weight_float / height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {int(bmi)}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {int(bmi)}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {int(bmi)}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {int(bmi)}, you are obese.")
else:
    print(f"Your BMI is {int(bmi)}, you are clinically obese.")

# Exercise 3: Leap year
"""Find a year is a leaf year or not.
This is how you work out whether if a particular year is a leap year.
on every year that is evenly divisible by 4 
**except** every year that is evenly divisible by 100 
**unless** the year is also evenly divisible by 400
e.g. The year 2000:
2000 ÷ 4 = 500 (Leap)
2000 ÷ 100 = 20 (Not Leap)
2000 ÷ 400 = 5 (Leap!)
So the year 2000 is a leap year.
But the year 2100 is not a leap year because:
2100 ÷ 4 = 525 (Leap)
2100 ÷ 100 = 21 (Not Leap)
2100 ÷ 400 = 5.25 (Not Leap)
"""
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 != 0:
        print("Leap year.")
    elif year % 400 == 0:
        print("Leap year.")
    else:
        print("Not leap year")
else:
    print("Not leap year.")

# Exercise 4: Pizza order
"""Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
"""
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
else:
    if size == "M":
        bill = 20
    else:
        bill = 25
    if add_pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")

# Exercise 5: Love score
'''For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
"Your score is **z**."

Example -
name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5
L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3
Love Score = 53
Print: "Your score is 53."

Example Input 1
name1 = "Kanye West"
name2 = "Kim Kardashian"
Example Output 1
Your score is 42, you are alright together.'''

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1.lower() + name2.lower()
true_count, love_count = 0, 0
for ch in ["t", "r", "u", "e"]:
    true_count += name.count(ch)
for ch in ["l", "o", "v", "e"]:
    love_count += name.count(ch)
score = int(str(true_count) + str(love_count))
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")