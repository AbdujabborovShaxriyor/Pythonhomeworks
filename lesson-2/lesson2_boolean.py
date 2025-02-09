#Problem 1

username = input("Enter the username: ")
password = input("Enter the password: ")

if not (bool(username.strip()) and bool(password.strip())):
    print("Please enter somthing. One or both of the fields are empty")
else:
    print("you entered",username,password)

#Problem 2

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1==num2:
    print(True)
else:
    print(False)

#Problem 3

num = int(input("Enter the number: "))
if num%2==0 and num>0:
    print(True)
else:
    print(False)

#Problem 4

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
num3 = int(input("Enter the number 3: "))

if num1!=num2:
    if num2!=num3:
        print("They are different")
    else:
        print("They have similar ones")
else:
    print("They have similar ones")     

#Problem 5

username = input("Enter the username: ")
password = input("Enter the password: ")

if len(username)==len(password):
    print(True)
else:
    print(False)

#Problem 6

num = int(input("Enter the number: "))

if num%3==0 and num%5==0:
    print("The number is divisible by 3 and 5")
else:
    print("The number is either not divisible by 3 or 5 or both")

#Problem 7

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))

if num1+num2>50.8:
    print(True)
else:
    print(False)

#Problem 8

num = int(input("Enter the number: "))
if num>=10 and num<=20:
    print(True)
else:
    print(False)







