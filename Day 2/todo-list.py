tasks = []

def show_tasks():

    if not tasks:
        print("No tasks to show")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task number")

while True:
    print("\nTodo List Options:")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '3':
        task_number = int(input("Enter task number to delete: "))
        delete_task(task_number)
    elif choice == '4':
        print("Exiting the Todo List.")
        break
    else:
        print("Invalid choice, please choose again.")