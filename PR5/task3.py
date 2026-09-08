name = "Karina"
surname = "Pikul"
group = "IT-32"


def get_initials(name: str, surname: str) -> str:
    return f"{name[0].upper()}.{surname[0].upper()}."


def count_letters(text: str, letter: str = "a") -> int:
    """Return how many times letter occurs in text."""
    count = 0

    for char in text:
        if char.lower() == letter.lower():
            count += 1

    return count


def count_vowels(text: str) -> int:
    vowels = "aeiouy"
    count = 0

    for char in text.lower():
        if char in vowels:
            count += 1

    return count


def reverse_text(text: str) -> str:
    result = ""

    for char in text:
        result = char + result

    return result


print(f"{name} {surname}, {group}")

print("Initials:", get_initials(name, surname))

c = len(surname)
vowels = count_vowels(surname)
consonants = c - vowels

print("Letters in surname:", c)
print(f"Vowels: {vowels}, consonants: {consonants}")

for vowel in "aeiou":
    print(f"{vowel}:", count_letters(surname, letter=vowel))

print("Default letter 'a':", count_letters(surname))

print("Reversed surname:", reverse_text(surname))

print("Docstring:", count_letters.__doc__)
print("Annotations:", count_letters.__annotations__)