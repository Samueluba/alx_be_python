# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the date as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # Return it in case we want to reuse

def calculate_future_date(current_date, days_to_add):
    # Add the specified number of days using timedelta
    future_date = current_date + timedelta(days=days_to_add)
    # Format the future date as "YYYY-MM-DD"
    formatted_future = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future}")
    return future_date

def main():
    current_date = display_current_datetime()

    try:
        # Prompt the user to enter number of days to add
        days_input = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer number of days.")

if __name__ == "__main__":
    main()
