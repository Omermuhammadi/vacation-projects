tasks = []

def addTask():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully")

def deleteTask():
    listTask()  
    if not tasks:
        print("No tasks to delete")
        return
    try:
        index = int(input("Enter the index of the task you want to delete: "))
        tasks.pop(index)
        print("Task deleted successfully")
    except (IndexError, ValueError):
        print("Invalid index. Task not deleted.")

def listTask():
    if not tasks:
        print("No tasks to list")
    else:
        print("Current tasks:")
        for i in range(len(tasks)):
            print("Task",i, tasks[i])

if __name__ == "__main__":
    print("Welcome to the to-do list app :)")
    while True:
        print("Select one of the following:")
        print("---------------------------")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. List all tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTask()
        elif choice == "4":
            break
        else:
            print("Invalid input. Please try again.")
            
    print("Goodbye")
