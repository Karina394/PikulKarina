#Завдання 4, Пікуль, ІТ-32

birth_day = 24
birth_month = 3
surname = "Pikul"
a = birth_day
b = birth_month
c = len(surname)
result_1 = a > b
result_2 = a >= c
result_3 = b <= c
result_4 = a < b
result_5 = a == b
result_6 = c != c
print(f"a > b = {result_1}, type = {type(result_1)}")
print(f"a >= c = {result_2}, type = {type(result_2)}")
print(f"b <= c = {result_3}, type = {type(result_3)}")
print(f"a < b = {result_4}, type = {type(result_4)}")
print(f"a == b = {result_5}, type = {type(result_5)}")
print(f"c != c = {result_6}, type = {type(result_6)}")