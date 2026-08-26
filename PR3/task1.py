print("Karina Pikul, IT-32")

name = input("Enter your name: ")
age = int(input("Enter your age (integer): "))

if not name:
    name = "Anonymous"

if age < 0:
    category = "invalid value"
elif age <= 6:
    category = "child"
elif age <= 17:
    category = "schoolchild"
elif age <= 64:
    category = "adult"
else:
    category = "senior"

print(f"Hello, {name}! Your category is {category}.")