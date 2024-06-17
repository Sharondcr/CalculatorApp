# AdvanceCalculator.py
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculate_percentage(x, y):
    return (x * y) / 100

def square_root(x):
    if x < 0:
        return "Error: Imaginary number"
    return math.sqrt(x)

def power_of(x, y):
    return x ** y

def factorial(x):
    if x < 0:
        return "Error: Factorial undefined for negative numbers"
    elif x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

def get_user_choice():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")
    print("6. Square Root")
    print("7. Power of")
    print("8. Factorial")
    print("9. Exit")
    choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")
    return choice

def calculator():
    while True:
        choice = get_user_choice()

        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", calculate_percentage(num1, num2))

        elif choice == '6':
            num = float(input("Enter a number to find its square root: "))
            print("Result:", square_root(num))

        elif choice == '7':
            base = float(input("Enter the base number: "))
            exponent = float(input("Enter the exponent: "))
            print("Result:", power_of(base, exponent))

        elif choice == '8':
            num = int(input("Enter a number to find its factorial: "))
            print("Result:", factorial(num))

        elif choice == '9':
            print("Calculator exiting. Goodbye!")
            break

        else:
            print("Invalid input. Please enter a valid number (1-9).")

calculator()
