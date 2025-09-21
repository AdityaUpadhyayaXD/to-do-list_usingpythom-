# To-Do List using a dictionary (map)

todo_list = {}
task_id = 1

def add_task(task_name):
    global task_id

    todo_list[task_id]={ "task":task_name , "status":"pending"}
    task_id+=1

def show_task():
    for tid in todo_list:
        if not todo_list:
            print("no task added")
        else:
            print("to-do list")
            for tid,details in todo_list.items():
                print(f"{tid} {details['task']} - {details['status']} ")



def  update_task(task_id,new_status):
    if task_id in todo_list:
        todo_list[task_id]["status"]=new_status
        print(f"{todo_list[task_id]["task"]} updated to {todo_list[task_id]["status"]}" )
    else:
        print("task not found")

def delete_task(tid):
    if tid in todo_list:
        del todo_list[tid]
        print(f"task {tid} deleted")
    else:
        print("task not found")

def show_pending_task():
    found = False
    for tid, detail in todo_list.items():
        if detail["status"] == "pending":
            print(f"{tid}. {detail['task']}")
            found = True
    if not found:
        print("no pending tasks")

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Show All Tasks")
    print("3. Update Task Status")
    print("4. Delete Task")
    print("5. Show Pending Tasks")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)

    elif choice == "2":
        show_task()

    elif choice == "3":
        tid = int(input("Enter task ID: "))
        new_status = input("Enter new status (pending/completed): ")
        update_task(tid, new_status)

    elif choice == "4":
        tid = int(input("Enter task ID to delete: "))
        delete_task(tid)

    elif choice == "5":
        show_pending_task()

    elif choice == "6":
        print("👋 Exiting To-Do List. Bye!")
        break

    else:
        print("⚠ Invalid choice. Please try again.")
