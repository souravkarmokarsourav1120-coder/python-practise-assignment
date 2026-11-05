# personal_calculator.py

name = input("Enter your name: ")
age = int(input("Enter your age: "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num2 != 0:
    division = num1 / num2
else:
    division = "Cannot divide by zero"

print("/n-------------Personal Calculator---------------")
print(f"Hello,{name}!")
print(f"Your age is{age}.")
print("-----------------------------------------")
print(f"Addition: {int(addition)}")
print(f"Subtraction: {int(subtraction)}")
print(f"Multiplication: {int(multiplication)}")
print(f"Division: {int(division)}")

