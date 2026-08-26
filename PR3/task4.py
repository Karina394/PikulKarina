print ("Karina Pikul, IT-32")

score = int(input("Enter your score (0-12): "))
missed_questions = int(input("Enter the number of missed questions: "))

if score < 0 or score > 12:
    print(f"EROORRR: I won't calculate this!!!")
else:
    if score == 12:
        grade = "A+"
    elif score >= 10:
        grade = "A"
    elif score >= 8:
        grade = "B"
    elif score >= 6:
        grade = "C"
    else:
        grade = "F"

if missed_questions > 16 * 0.30:
    print(f"You have missed too many questions.")
if missed_questions > 16 * 0.30:
    passed = "failed"
elif score >= 6:
    passed = "passed"
else:
    passed = "failed"

print(f"Score: {score}. Your grade is: {grade}. You have {passed} the test.")