# Empty list
list = []

# Add task in list
# append is used to add task in list
def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter a task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")

# View task if you want to see your list of tasks
# enumerate is used to get index and task
def view_tasks(tasks):
    """Display all tasks in the list."""
    if not tasks:
        print("No tasks in the list!")
        return
    
    print("\nYour To-Do List:")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")

# Remove task from list
# pop is used to remove task from list
# try, except is used to handle the error
# len is used to get the length of the list
def remove_task(tasks):
    """Remove a task from the list."""
    if not tasks:
        print("No tasks to remove!")
        return
    
    view_tasks(tasks)
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

# Main function
# while loop is used to run the program again and again
# Choice is used to get user's choice
# if, elif, else statements is used to check the availability of task
def main():
    """Main program loop."""
    tasks = []  # Initialize empty task list
    
    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Thankyou for using this app")
            break
        else:
            print("Invalid choice! Please try again.")

# __name__ is used to check the availability of main function
if __name__ == "__main__":
    main()