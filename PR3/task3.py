print ("Karina Pikul, IT-32")

number_one = int(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /, %, **, //): ")
number_two = int(input("Enter the second number: "))

if operation == "+":
    result = number_one + number_two
    print(f"The result of {number_one} + {number_two} is: {result:.4f}")
elif operation == "-":
    result = number_one - number_two
    print(f"The result of {number_one} - {number_two} is: {result:.4f}")
elif operation == "*":
    result = number_one * number_two
    print(f"The result of {number_one} * {number_two} is: {result:.4f}")
elif operation == "/":
    if number_two != 0:
        result = number_one / number_two
        print(f"The result of {number_one} / {number_two} is: {result:.4f}")
    else:
        result = "undefined (division by zero)"
elif operation == "%":
    if number_two != 0:
        result = number_one % number_two
        print(f"The result of {number_one} % {number_two} is: {result:.4f}")
    else:
        result = "undefined (modulus by zero)"
elif operation == "**":
    result = number_one ** number_two
    print(f"The result of {number_one} ** {number_two} is: {result:.4f}")
elif operation == "//":
    if number_two != 0:
        result = number_one // number_two
        print(f"The result of {number_one} // {number_two} is: {result:.4f}")
    else:
        result = "undefined (floor division by zero)"
else:
    result = "invalid operation"

if operation in ["+", "-", "*", "/", "%", "**", "//"]:
    print(f"The result of {number_one} {operation} {number_two} is: {result}")  
else:
    print(f"Invalid operation. Please enter one of the following: +, -, *, /, %, **, //.")

