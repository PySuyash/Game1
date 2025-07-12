import json

FILENAME = "tasks.json"

def save_tasks(tasks, filename = "tasks.json"):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=4)

def load_tasks():
    try:
        with open(FILENAME, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []

def view_tasks(tasks):
    if not tasks:
        print("No task found.")
    for idx, task in enumerate(tasks):
        status = "Done" if task["Completed"] else "Not Done"
        print(f"{idx+1}. [{status}] {task['Task']}")
        save_tasks(tasks)

def add_tasks(tasks):
    task = input("Enter new task: ")
    tasks.append({"Task": task, "Completed": False})
    print("Task added")
    save_tasks(tasks)

def mark_complete(tasks):
    view_tasks(tasks)
    try:
        i = int(input("Enter the index number of the task to mark complete: ")) - 1
        tasks[i]["Completed"] = True
        print("Task Completed")
        save_tasks(tasks)
    except:
        print("No task found")
    
def delete_task(tasks):
    try:
        i = int(input("Enter the task number to delete: ")) - 1
        tasks.pop(i)
        print("Task deleted.")
        save_tasks(tasks)
    except:
        print("No task found to delete.")

def main():

    tasks = load_tasks()

    while True:
        print("\nTo-Do List App.")
        print("1. View Tasks.")
        print("2. Add Tasks.")
        print("3. Mark Task as Completed.")
        print("4. Delete Task.")
        print("5. Exit.")

        choice = int(input("Enter your choice -> "))

        if choice == 1:
            view_tasks(tasks)
        elif choice == 2:
            add_tasks(tasks)
        elif choice == 3:
            mark_complete(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            save_tasks(tasks)
            print("Goodbye")
            break
        else:
            print("Wrong choice!")

if __name__ == "__main__":
    main()