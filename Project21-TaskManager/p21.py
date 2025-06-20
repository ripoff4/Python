task_list = []
while True:
    print("====Task Manager====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("0. Exit")
    print("===================")
    your_choice = int(input("Enter your choice (0-4) : "))
    if your_choice == 0:
        break
    elif your_choice == 1:
        task = input("Enter task title : ")
        print(f"Task '{task}' is added succesfully")
        value = "[] "+task
        task_list.append(value)
    elif your_choice == 2:
        print("====My Tasks====")
        for i in range(len(task_list)):
            print(f"{i+1}. {task_list[i]}")
    elif your_choice == 3:
        completed_index = int(
            input("Enter task number to mark as completed : "))
        value = task_list[completed_index-1]
        task_list[completed_index-1] = "[✅] " + value
        print(f"Task '{value}' is marked complete")
    elif your_choice == 4:
        remove_index = int(input("Enter task number to mark as deleted : "))
        value = task_list[remove_index-1]
        task_list.remove(value)
        print(f"Task '{value}' is removed ")
    else:
        print("No such option exist.Try again!")
    print("===================")

    try_again = input("Try another option? (yes/no) : ")
    if try_again == 'no':
        break
