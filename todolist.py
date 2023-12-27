todo_list = []

while True:
    print("Options:")
    print("1. Add task")
    print("2. Remove task")
    print("3. View tasks")
    print("4. Quit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        todo_list.append(task)
    elif choice == "2":
        task = input("Enter task to remove: ")
        if task in todo_list:
            todo_list.remove(task)
        else:
            print("Task not found")
    elif choice == "3":
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")
    elif choice == "4":
        break
    else:
        print("Invalid choice")

print(todo_list)
