import os

FILE_NAME = "task.txt"

def load_task():
    task = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as file:
            for line in file:
                task_id, title, status = line.strip().split(" | ") 
                task[int(task_id)]={"title" : title,"status" : status}
    return task

def save_task(task):
    with open(FILE_NAME,"w") as file:
        for task_id,task in task.items():
            file.write(f"{task_id} | {task['title']} | {task['status']} \n")


def add_task(tasks):
    title = input("Add new task : ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title":title,"status":"incompleted"}
    print(f"taks {title} added.")

def view_task(tasks):
    if not tasks:
        print("no tasks avilable")
    else:
        for task_id,task in tasks.items():
            print(f"{task_id}. {task['title']} - {task['status']}")

def mark_task(tasks):
    task_id = int(input("enter task id to mark as completed : "))
    if task_id in tasks:
        tasks[task_id]['status'] = "completed"
        print(f"{tasks[task_id]['title']} is completed hurrrreeeeeeeeeyyyyy!!!!!.......")
    else:
        print("Task ID not Found.")


def delete_task(tasks):
    task_id = int(input("Enter task id to delete a task : "))
    if task_id in tasks:
        delete = tasks.pop(task_id)
        print(f"{delete['title']} is deleted.")
    else:
        print("Task ID not Found.")

def main():
    tasks = load_task()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Exit put of this program")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_task(tasks)
        elif choice == 3:
            mark_task(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            save_task(tasks)
            print("Exiting this programme....")
            break
        else:
            print("Invalid input Try again....")

if __name__ == "__main__":
    main()