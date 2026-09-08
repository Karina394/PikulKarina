def read_grade(prompt):
    """Read and validate a grade from 0 to 100."""
    while True:
        value = input(prompt)

        if not value.isdigit():
            print("Error: digits only")
            continue

        grade = int(value)

        if grade < 0 or grade > 100:
            print("Error: the value must be between 0 and 100")
            continue

        return grade


def to_letter(grade):
    """Convert a numeric grade to a letter grade."""
    if grade >= 90:
        return "A"
    if grade >= 82:
        return "B"
    if grade >= 74:
        return "C"
    if grade >= 64:
        return "D"
    if grade >= 60:
        return "E"
    return "F"


def average(grades):
    """Calculate the arithmetic mean of grades."""
    return sum(grades) / len(grades)


def count_above(grades, limit):
    """Count grades greater than the given limit."""
    count = 0

    for grade in grades:
        if grade > limit:
            count += 1

    return count


def print_report(name, group, grades):
    """Print a report with student grades and results."""
    avg = average(grades)
    letter = to_letter(avg)
    above = count_above(grades, avg)

    print("--- Report ---")
    print(f"Student: {name}, group {group}")
    print("Grades:", *grades)
    print(f"Average: {avg:.2f} -> {letter}")
    print(f"Best: {max(grades)}, worst: {min(grades)}")
    print(f"Above average: {above}")


def main():
    """Run the grade report program."""
    name = "Karina"
    group = "IT-32"

    grades = []

    for i in range(6):
        grade = read_grade(f"Grade {i + 1} (0-100): ")
        grades.append(grade)

    print_report(name, group, grades)

main()