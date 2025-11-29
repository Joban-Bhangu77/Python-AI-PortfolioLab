# Day 10: Functions and Loops

# Function to display the menu
def show_menu():
    print("\n--- To do List Menu ---")
    print("1. View Tasks")
    print("2. Add task")
    print("3. Remove Task")
    print("4. Exit")

  # Function to view tasks
def view_tasks(tasks):
    if not tasks:
        print("Your To-Do list is empty!")
    else:
        print("Your Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

# Function to add a task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"'{task}' has been added to your To-Do list!")

# Function to remove a task
def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"'{removed_task}' has been removed!")
        else:
            print("Invalid task number!")

# Main program
def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-4.")

if __name__ == "__main__":
    main()  