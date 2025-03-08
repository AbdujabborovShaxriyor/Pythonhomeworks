import json
import csv
def load_json():
    with open("tasks.json","r") as file:
        data = json.load(file)
        for row in data:
            print(row)
def calculations():
    with open("tasks.json","r+") as file:
        data = json.load(file)
        completed = 0
        pending = 0
        every = 0
        avg = 0
        for row in data:
            every+=1
            if row["status"]=="completed":
                completed+=1
            elif row["status"]=="pending":
                pending+=1    
            if row["priority"]=="average":
                avg+=1
        print(f"The number of completed tasks is {completed}")
        print(f"The number of pending tasks is {pending}")
        print(f"The number of all tasks is {every}")
        print(f"The number of average priority tasks is {avg}")  

def converting(json_file="tasks.json",csv_file="tasks.csv"):
    with open(json_file,"r") as json_file:
        tasks = json.load(json_file)
    with open(csv_file,"w") as csv_file:
        fieldnames = ["ID","Task","Completed","Priority"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for task in tasks:
            csv_writer.writerow({
                "ID": task.get("id"),
                "Task": task.get("task"),
                "Completed": task.get("completed"),
                "Priority": task.get("priority")
            })


