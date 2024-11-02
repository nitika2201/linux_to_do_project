import os
TODO_FILE = "todo_list.txt"
def load_tasks():
    if not os.path.exists(TODO_FILE):
       return[]
    with open(TODO_FILE, "r")as file:
        return file.read().splitlines()
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
     file.write("\n".join(tasks))
def add_task(task):
    tasks= load_tasks()
    tasks.append(task)
    save_tasks(tasks)
def view_tasks():
    tasks=load_tasks()
    if not tasks:
        print("no tasks found.")
    else:
         for index, task in enumerate(tasks , start=1):
             print(f"{index}. {task}")
def delete_task(task_index):
    tasks = load_tasks()
    if 0<task_index <= len(tasks):
       tasks.pop(task_index - 1)
       save_tasks(tasks)
       print("task deleted.")
    else:
         print("invalid task number.")
def main():
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("choose an option :")

        if choice =="1":
           task = input("enter a task: ")
           add_task(task)
        elif choice == "2":
             view_tasks()
        elif choice == "3":
             view_tasks()
             task_number= int(input("enter task number to delete: "))
             delete_task(task_number)
        elif choice == "4":
             print("Goodbye!")
             break
        else:
             print("invalid choice. please try again.")

if __name__ == "__main__":
    main()
