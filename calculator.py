# Simple Calculator Program

# Function to perform the arithmetic operations
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error! Division by zero."
        return num1 / num2
    else:
        return "Invalid operator. Please use +, -, *, or /."

# Get input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")

    # Perform the operation and print the result
    result = calculate(num1, num2, operator)
    print(f"The result of {num1} {operator} {num2} = {result}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
