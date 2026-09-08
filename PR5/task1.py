name = "Karina"
surname = "Pikul"
group = "IT-32"
year = 2009


def print_card():
    print(f"Name: {name} {surname}")
    print(f"Group: {group}")
    print(f"Birth year: {year}")


def print_card_args(name, surname, group="IT-32", year=2009):
    print(f"{name} {surname}, {group}, {year}")


print(f"{name} {surname}, {group}")

print("--- no parameters, call 1 ---")
print_card()

print("--- no parameters, call 2 ---")
print_card()

print("--- no parameters, call 3 ---")
print_card()

print("--- positional arguments ---")
print_card_args("Karina", "Pikul", "IT-32", 2009)

print("--- keyword arguments ---")
print_card_args(year=2009, group="IT-32", surname="Pikul", name="Karina")

print("--- mixed arguments ---")
print_card_args("Karina", "Pikul", group="IT-32", year=2009)

print("--- default group ---")
print_card_args("Karina", "Pikul", year=2009)