# Function to perform the arithmetic operations
def perform_operation(num1: float, num2: float, operation: str) -> float:
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."

# Collect user input for numbers and operation
def get_user_input():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()
        
        result = perform_operation(num1, num2, operation)
        print(f"Result: {result}")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

# Call the function to get user input and show the result
get_user_input()

