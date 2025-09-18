# pattern_drawing.py

# Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to handle rows
while row < size:
    # Use a for loop to print columns (asterisks)
    for col in range(size):
        print("*", end="")
    # Move to the next line after one row is printed
    print()
    row += 1

