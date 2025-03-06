from abc import ABC, abstractmethod
import json
import csv

# Interface for Storage Strategies

class TaskStorage(ABC):
    
    #loading
    @abstractmethod
    def load_task(self):
        pass
    
    #saving
    @abstractmethod
    def save_task(self):
        pass
    
#JSON storage

class JsonStorage(TaskStorage):
    
    def __init__(self,filename = "tasks.json"):
        self.filename = filename
        
    #loading
    
    def load_task(self):
        try:
            with open(self.filename,"r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    #saving
    
    def save_task(self,tasks):
        with open(self.filename,"w") as file:
            json.dump(tasks,file,indent=4)
            
#CVS storage

class CvsStorage(TaskStorage):
    def __init__(self,filename="tasks.cvs"):
        self.filename=filename
    
    #saving
    
    def save_task(self):
        try:
            with open(self.filename,"r") as file:
                reader = csv.DictReader(file)
                return[row for row in reader]
        except FileNotFoundError:
            return []
    
    #loading 
    
    def load_task(self,tasks):
        with open(self.filename,'w',newline="") as file:
            fieldnames = ["id", "title", "description", "due_date", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(tasks)
#ToDo app

class ToDoApp:
    def __init__(self,storage:TaskStorage):
        self.storage = storage
        self.tasks = self.storage.load_task()
        
    #adding task
    
    def add_task(self,task_id, title, description, due_date, status):
        self.tasks({
            "id":task_id,
            "title":title,
            "description":description,
            "due_date":due_date,
            "status": status
        })
        self.storage.save_task(self.tasks)
        print("Tasks added successfully")
    
    #viewing task
    
    def view_task(self):
        for task in self.tasks:
            print(task)
    
    #updating a task
    
    def update_task(self,task_id, title=None, description=None, due_date=None, status=None):
        for task in self.tasks:
            if task["id"]==task_id:
                if title: task["title"]=title
                if description: task["description"]=description
                if due_date: task["due_date"]=due_date
                if status: task["status"]=status
                self.storage.save_task(self.tasks)
                print("Task updated successfully!")
                return
        print("Task not found!")

    # deleting a task
    
    def delete_task(self,task_id):
        self.tasks = [task for task in self.tasks if task["id"]!=task_id]
        self.storage.save_task(self.tasks)
        print("Task deleted successfully!")   
        
    #filtering a task
    
    def filter_task(self,status):
        filtered = [task for task in self.tasks if task["status"]==status] 
        for task in filtered:
            print(task)
            
    def save_task(self):
        self.storage.save_task(self.tasks)
        print("Tasks saved successfully!")
    
    def load_task(self):
        self.tasks = self.storage.load_task()
        print("Tasks loaded successfully!")
        
if __name__ == "__main__":
    storage = JsonStorage()  # Swap with CSVStorage() if needed
    todo = ToDoApp(storage)
    
    while True:
        print("""
Welcome to the To-Do Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit
        """)
        
        choice = input("Enter your choice: ")
        if choice == "1":
            task_id = input("Enter Task ID: ")
            title = input("Enter Title: ")
            description = input("Enter Description: ")
            due_date = input("Enter Due Date (YYYY-MM-DD): ")
            status = input("Enter Status (Pending/In Progress/Completed): ")
            todo.add_task(task_id, title, description, due_date, status)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            task_id = input("Enter Task ID to update: ")
            title = input("Enter new Title (leave blank to keep unchanged): ") or None
            description = input("Enter new Description (leave blank to keep unchanged): ") or None
            due_date = input("Enter new Due Date (YYYY-MM-DD, leave blank to keep unchanged): ") or None
            status = input("Enter new Status (Pending/In Progress/Completed, leave blank to keep unchanged): ") or None
            todo.update_task(task_id, title, description, due_date, status)
        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            todo.delete_task(task_id)
        elif choice == "5":
            status = input("Enter status to filter by (Pending/In Progress/Completed): ")
            todo.filter_tasks(status)
        elif choice == "6":
            todo.save_tasks()
        elif choice == "7":
            todo.load_tasks()
        elif choice == "8":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")
