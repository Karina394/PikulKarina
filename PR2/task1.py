#Завдання 1, Пікуль, ІТ-32

birth_year = 2009
height = 1.70
name = "Karina Pikul"
has_scholarship = False
print(f"birth_year = {birth_year}, type = {type(birth_year)}")
print(f"height = {height}, type = {type(height)}")
print(f"name = {name}, type = {type(name)}")
print(f"has_scholarship = {has_scholarship}, type = {type(has_scholarship)}")
print("Before change:")
print(f"birth_year = {birth_year}, type = {type(birth_year)}")
print(f"has_scholarship = {has_scholarship}, type = {type(has_scholarship)}")
birth_year = "2009"
has_scholarship = 1.0
print("After change:")
print(f"birth_year = {birth_year}, type = {type(birth_year)}")
print(f"has_scholarship = {has_scholarship}, type = {type(has_scholarship)}")