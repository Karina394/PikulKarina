print("Karina Pikul, IT-32")

day = int(input("Enter the day (integer): "))
month = int(input("Enter the month (integer): "))
year = int(input("Enter the year (integer): "))

if year <= 0:
    print(f"Date is invalid: year must be positive.")
elif month < 1 or month > 12:
    print(f"Date is invalid: month must be between 1 and 12.")
else:
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            print(f"Date is invalid: month {month} has only 31 days.")
        else:
            print(f"Date is valid: {day}/{month}/{year}.")
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            print(f"Date is invalid: month {month} has only 30 days.")
        else:
            print(f"Date is valid: {day}/{month}/{year}.")
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day < 1 or day > 29:
                print(f"Date is invalid: February has only 29 days in a leap year.")
            else:
                print(f"Date is valid: {day}/{month}/{year}.")
        else:
            if day < 1 or day > 28:
                print(f"Date is invalid: February has only 28 days in a non-leap year.")
            else:
                print(f"Date is valid: {day}/{month}/{year}.")
