# Ask for inputs
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

# Calculate savings
monthly_savings = monthly_income - monthly_expenses

# Project savings for 1 year with 5% growth
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display result
print("Your projected savings for the year (with 5% growth) is:", projected_savings)
