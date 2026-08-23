#Завдання 5, Пікуль, ІТ-32

birth_day = 24
birth_month = 3
positive = birth_day > 0
even = birth_day % 2 == 0
both = positive and even
print(f"Birth day: {birth_day}")
print(f"Positive: {positive}")
print(f"Even: {even}")
print(f"Positive and even: {both}")
number = birth_day * birth_month
positive_2 = number > 0
even_2 = number % 2 == 0
both_2 = positive_2 and even_2
print(f"Second number: {number}")
print(f"Positive: {positive_2}")
print(f"Even: {even_2}")
print(f"Positive and even: {both_2}")