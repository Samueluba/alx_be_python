-# Import the perform_operation function from arithmetic_operations.py
from arithmetic_operations import perform_operation

# Collect user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()

# Perform the operation and print the result
result = perform_operation(num1, num2, operation)
print(f"Result: {result}")


