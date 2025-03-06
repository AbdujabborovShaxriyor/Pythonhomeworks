with open("employees.txt","w") as file:
    file.write("Employees list:")

#Employee class

class Employee:
    def __init__(self,employee_id,name,position,salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
    
#EmployeeManager class 
    
class EmployeeManager(Employee):
    def __init__(self,employee_id,name,position,salary):
        super().__init__(employee_id,name,position,salary)
    
    #Adding an employee
    
    def add(self):
        with open("employees.txt","a") as file:
            id = int(input("Enter the employee id: "))
            name = input("Enter the employee name: ")
            position = input("Enter the employee position: ")
            salary = int(input("Enter the employee id: "))
            file.write(f"id:{id},name:{name},position:{position},salary:{salary}")

    #Display
    
    def display(self):
        with open("employees.txt","r") as file:
            print(file.readlines)
            
    #Search
    
    def search(self):
        with open("employees.txt","r") as file:
            id  = int(input("Enter the id of the employee: "))
            while True:
                line = file.readline()
                if not line:
                    break
                for part in line.split(","):
                    if id in part:
                        return(f"Employee has been found: {line}")
            return("Employee not found")        

    #Update
    
    def update(self):
        with open("employees.txt","r+") as file:
            id  = int(input("Enter the id of the employee: "))
            content = file.read()
            coordinate = content.find(id)
            if coordinate:
                id = int(input("Enter the new employee id: "))
                name = input("Enter the new employee name: ")
                position = input("Enter the new employee position: ")
                salary = int(input("Enter the new employee id: "))
                file.seek(coordinate)
                file.write(f"id:{id},name:{name},position:{position},salary:{salary}")
            else:
                return("Employee not found") 
    # Delete 
    
    def delete(self):
        with open("employees.txt","r+") as file:
            id  = int(input("Enter the id of the employee: "))
            content = file.read()
            coordinate = content.find(id)
            if coordinate:
                file.seek(coordinate)
                file.write(f"")
            else:
                return("Employee not found") 
employee = EmployeeManager()
while True:
    choice = int(input("""1. Add new employee record
    2. View all employee records
    3. Search for an employee by Employee ID
    4. Update an employee's information
    5. Delete an employee record
    6. Exit
    Enter your choice: """))
    if choice ==1:
        employee.add()
    elif choice == 2:
        employee.display()
    elif choice == 3:
        employee.search()
    elif choice == 4:
        employee.update()
    elif choice == 5:
        employee.delete()  
    elif choice == 6:
        break
            
        
        