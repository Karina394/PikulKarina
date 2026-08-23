#Завдання 6, Пікуль, ІТ-32

name = input("Enter your name: ")
age = float(input("Enter your age: "))
in_range = 18 <= age <= 60
is_even = age % 2 == 0
both = in_range and is_even
one_condition = in_range or is_even
years_left = 60 - age
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Age is from 18 to 60: {in_range}")
print(f"Age is even: {is_even}")
print(f"Both conditions are true: {both}")
print(f"At least one condition is true: {one_condition}")
print(f"Years until 60: {years_left}")
