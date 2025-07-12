import json     # import build-in json module to work with json files.

FILENAME = "tasks.json" # This defines the file name from where the tasks will be loaded and saved

def load_tasks():   # Defines a function that loads the tasks from the file.
    try:
        with open(FILENAME, "r") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except FileNotFoundError:
        return []
    
def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    for idx, tasks in enumerate(tasks):
        status = "Done" if tasks["completed"] else "Not Done"
        print(f"{idx+1}. [{status}] {tasks['task']}")

def add_tasks(tasks):
    task = input("Enter a new task: ")
    tasks.append({"task": task, "completed": False})
    print("Task added.")

def mark_complete(tasks):
    show_tasks(tasks)
    try:
        i = int(input("Enter task number to mark as complete: ")) - 1
        tasks[i]["complete"] = True
        print("Task marked as completed.")
    except:
        print("Invalid Selection.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        i = int(input("Enter task number to delete: ")) - 1
        tasks.pop(i)
        print("Task Deleted.")
    except:
        print("Invalid Selection.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List App")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()