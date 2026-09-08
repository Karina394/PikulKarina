name = "Karina"
surname = "Pikul"
group = "IT-32"
y = 2009


def print_age(year):
    age = 2026 - year
    print(f"Age: {age}")


def get_age(year, current_year=2026):
    if year > current_year or year < 0:
        return -1

    return current_year - year

    print("after return")


print(f"{name} {surname}, {group}")

print_age(y)

print("print_age returned:", print_age(y))

age = get_age(y)
print("Age from get_age:", age)

print("Age in months:", age * 12)
print("Age in weeks:", age * 52)

age_2030 = get_age(y, current_year=2030)
print("Age in 2030:", age_2030)

print("Invalid year 3000 gives:", get_age(3000))