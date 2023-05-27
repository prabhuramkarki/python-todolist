tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully.")
    else:
        print("Task not found in list.")

def show_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for task in tasks:
            print(f"- {task}")

while True:
    print("Select an option:")
    print("1. Add task")
    print("2. Remove task")
    print("3. Show tasks")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter task to add: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == "3":
        show_tasks()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
