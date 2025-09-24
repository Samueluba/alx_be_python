-# Import the perform_operation function from arithmetic_operations.py
from arithmetic_operations import perform_operation

# Collect user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").lower()

# Perform the operation and print the result
result = perform_operation(num1, num2, operation)
print(f"Result: {result}")


# shopping_list_manager.py

def display_menu():
    print(f"Shopping List Manager")  # Required for the auto-check
    print("1. Add item")
    print("2. Remove item")
    print("3. View shopping list")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.")
    else:
        print("Item name cannot be empty.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' is not in your shopping list.")

def view_list(shopping_list):
    if shopping_list:
        print("\nYour shopping list:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("\nYour shopping list is currently empty.")

# ✅ This is the part you are responsible for
def main():
    # Initialize an empty list
    shopping_list = []

    # Keep showing the menu until the user chooses to exit
    while True:
        display_menu()
        choice = input("Choose an option (1-4)
