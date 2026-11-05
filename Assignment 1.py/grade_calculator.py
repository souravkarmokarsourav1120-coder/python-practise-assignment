
# grade_calculator.py

# 1. Take student's name
name = input("Enter student name: ")

# 2. Take marks for three subjects

math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
python = float(input("Enter Python marks: "))

# 3. Check whether marks are valid
if (math < 0 or math > 100 or
    english < 0 or english > 100 or
    python < 0 or python > 100):

    print("Invalid marks! marks must be between 0 and 100.")

else:
    # 4. Calculate average marks
    average_marks = (math + english + python) / 3

    # 5. Determine grade
    if average_marks >= 80:
        grade = "A+"
    elif average_marks >= 70:
        grade = "A"
    elif average_marks >= 60:
        grade = "A-"
    elif average_marks >= 50:
        grade = "B"
    elif average_marks >= 40:
        grade = "C"
    else:
        grade = "F"

    # 6. Display final result
    print("\n========== Student Result ==========")
    print(f"Student Name: {name}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Final Grade: {grade}")
    print("====================================")
