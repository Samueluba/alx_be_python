task = input("Enter your task:")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")
if task == "high":
    print("Reminder: 'Finish project report' is a high priority task that requires immediate attention today!")
elif task == "medium":
    print("take it easyy")
elif task == "low" and time_bound == "No":
    print("Note: 'Read a book' is a low priority task. Consider completing it when you have free time")
else:
    print("enter your task")
