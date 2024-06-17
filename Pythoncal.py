# PythonCalculator.py

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Function to display the menu and get user choice
def get_user_choice():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter choice (1/2/3/4/5): ")
    return choice

# Main function to run the calculator
def calculator():
    while True:
        choice = get_user_choice()

        if choice in ('1', '2', '3', '4'):
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
            print("Calculator exiting. Goodbye!")
            break

        else:
            print("Invalid input. Please enter a valid number (1-5).")

# Run the calculator
calculator()
