def perform_operation(num1: float, num2: float, operation: str) -> float:
    # Check the operation and perform the corresponding arithmetic operation
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operation."

# Collect user input for numbers and the operation
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()
    
    # Perform the operation and display the result
    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

except ValueError:
    print("Invalid input! Please enter valid numbers.")

