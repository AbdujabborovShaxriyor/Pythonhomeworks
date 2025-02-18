with open("employees.txt","w") as file:
    file.write("Employee list")

while True:
    choice = int(input("""
    1. Add new employee record
    2. View all employee records
    3. Search for an employee by Employee ID
    4. Update an employee's information
    5. Delete an employee record
    6. Exit """))
    if  choice == 1:
        emp_id = int(input("Enter the employee id: "))
        name = input("Enter the name of the employee: ")
        position = input('Enter the position of the employee: ')
        salary = int(input("Enter the salary of the employee: "))
        with open("employees.txt","a") as file:
            file.write(f"{emp_id} {name} {position} {salary}\n")
    elif choice == 2:
        with open("employees.txt","r") as file:
            print(file.read())
    elif choice == 3:
        user_id = int(input("Enter the id of the employee: "))
        with open("employees.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                for i in line.split():
                    if user_id==i:
                        print(file.read(line))
                    else:
                        print("There is no such user with this ID")
    elif choice==4:
        user_id = int(input("Enter the id of the employee whom details you wanna change: "))
        with open("employees.txt","r+") as file:
            lines = file.readlines()
            for line in lines:
                data = line.split()
                if data and data[0] == user_id:
                    print("\nEmployee Found:", line.strip())
                else:
                    print("There is no such user with this ID")
    elif choice == 5:
        user_id = int(input("Enter the id of the employee whom details you wanna change: "))
        with open("employees.txt","r+") as file:
            lines = file.readlines()
            for line in lines:
                for i in line.split():
                    if user_id==i:
                        line=""
                    else:
                        print("There is no such user with this ID") 
    elif choice == 6:
        break       
        