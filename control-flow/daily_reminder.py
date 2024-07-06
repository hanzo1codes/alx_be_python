def get_task_reminder():
    # Prompt for task description
    task = input("Enter your task: ").strip()

    # Prompt for task priority
    priority = input("Priority (high/medium/low): ").strip().lower()

    # Prompt for time sensitivity
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Initialize the reminder message
    reminder = ""

    # Process the task based on priority using match-case
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
        case "medium":
            reminder = f"'{task}' is a medium priority task"
        case "low":
            reminder = f"'{task}' is a low priority task"
        case _:
            print("Invalid priority level entered. Please use high, medium, or low.")
            return

    # Modify the reminder if the task is time-bound
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    # Print the customized reminder
    print(f"Reminder: {reminder}")

# Call the function to execute the script
if __name__ == "__main__":
    get_task_reminder()
