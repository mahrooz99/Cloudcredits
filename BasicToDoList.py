#2- Basic ToDoList
def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for i, (task, status) in enumerate(tasks, 1):
            status_str = "Completed" if status else "Pending"
            print(f"{i}. {task} - {status_str}")



def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append((task, False))


def complete_task(tasks):
    display_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1] = (tasks[task_num - 1][0], True)
                print(f"Task {task_num} marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")


def todo_list():
    tasks = []

    while True:
        print("\n1. View tasks")
        print("2. Add a task")
        print("3. Mark a task as completed")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            print("Exiting To-Do List. Goodbye!")
            break
        else:
            print("Invalid input. Please choose a valid option.")


todo_list()
