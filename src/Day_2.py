# Exercise 1: Add digits of Two digit number
two_digit_number = input("Type a two digit number: ")
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(first_digit + second_digit)

# Operator Precedence
'''
PEMDAS - (), **, * /, + -
'''
print(3*3-2/4+4)
# Out: 12.5
print(3*(3-2/4)+4)
# Out: 11.5

# Exercise 2: BMI calculator
'''
Formula: BMI = weight (kg) / height ** 2 (m^2)
'''
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
height_float = float(height)
weight_float = float(weight)
bmi = int(weight_float // (height_float * height_float))
print(bmi)

# f-string
height = 1.6
weight = 64
name = 'Ram'
print(f"{name}'s height is {height}m, and wight is {weight}kg")

# Exercise 3: Life in days, weeks and months
'''
Assume you will live till 90 years. Enter the current age and calculate life remains in days, weeks and months
hints - 1 year is equal to 365 days or 52 weeks or 12 months.
'''
age = input("What is your current age? ")
age_in_integer = int(age)
remaining_age_in_years = 90 - age_in_integer
number_of_days = int(remaining_age_in_years * 365)
number_of_weeks = int(remaining_age_in_years * 52)
number_of_months = int(remaining_age_in_years * 12)
message = f"You have {number_of_days} days, {number_of_weeks} weeks, and {number_of_months} months left."
print(message)
