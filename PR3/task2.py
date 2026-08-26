print ("Karina Pikul, IT-32")

number = int(input("Enter a number: "))

if number < 0:
    print(f"The number is negative.")
elif number == 0:
    print(f"The number is zero.")
else:
    print(f"The number is positive.")    

if number !=0:
    if number % 2 == 0:
        print(f"The number is even.")
    else:
        print(f"The number is odd.")