# First problem

number = float(input("Enter the number: \n>>>"))
rounded_number = round(number,2)
print(f"Rounded number is: {rounded_number}")

# Second problem

a = float(input("Enter the first number: \n>>>"))
b = float(input("Enter the second number: \n>>>"))
c = float(input("Enter the third number: \n>>>"))

num_list = [a,b,c]
biggest = num_list[0]

for num in num_list:
    if biggest>num:
        continue
    else: 
        biggest=num
print(f"{biggest} is the biggest")

for num in num_list:
    if biggest<num:
        continue
    else: 
        biggest=num
print(f"{biggest} is the smallest")

#Third problem 

km = int(input("Enter the kilometers: \n>>>"))
m=km*1000
cm = km*100000
print(f"{km} kilometer is {m} meter.")
print(f"{km} kilometer is {cm} centimeter.")

# Problem 4

a = int(input)
b = int(input)
print(f"Integer division: {a//b}")
print(f"Remaineder: {a%b}")

# Probelem 5

celcius = float(input("Enter the temperature in celcius: \n>>>"))
farenheit = celcius*1.8+32
print(f"{celcius} celcius is {farenheit} farenheit")

# Problem 6

number = int(input("Enter the number: \n>>>"))
last_digit = number%10
print(last_digit)

# Problem 7

number = int(input("Enter the number: \n>>>"))
if number%2==0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")