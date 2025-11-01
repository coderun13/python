tasks = []

print("WELCOME TO THE TASK MANAGEMENT APP")

while True:
    try:
        total_tasks = int(input("Enter how many tasks you want to add: "))
        break
    except ValueError:
        print("Please enter a valid number.")

for i in range(1, total_tasks + 1):
    task_name = input(f"Enter Task {i}= ")
    tasks.append(task_name)

print(f"Today's Tasks Are\n{tasks}")

while True:
    operation = input("Enter 1 for Add\nEnter 2 for Update\nEnter 3 for Delete\nEnter 4 for View\nEnter 5 for Exit or Stop\n")

    if operation == "1":
        add = input("Enter task you want to add: ")
        tasks.append(add)
        print(f"Task {add} has been successfully added")

    elif operation == "2":
        updated_val = input("Enter the task name you want to update: ")
        if updated_val in tasks:
            up = input("Enter new task: ")
            ind = tasks.index(updated_val)
            tasks[ind] = up
            print(f"Updated Task: {up}")
        else:
            print("Invalid Task")

    elif operation == "3":
        delete_val = input("Which task you want to delete: ")
        if delete_val in tasks:
            ind = tasks.index(delete_val)
            del tasks[ind]
            print(f"Task {delete_val} has been deleted")
        else:
            print("Invalid Task")

    elif operation == "4":
        print(f"Total Tasks = {tasks}")

    elif operation == "5":
        print("Closing the program....")
        break
        
    else:
        print("Invalid Input")