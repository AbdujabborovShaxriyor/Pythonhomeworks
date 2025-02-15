number = int(input("Enter a positive number: "))
def factor(number):
    for num in range(1,number+1):
        if num<=number and number%num==0:
            print(f"{num} is a factor of {number}") 
factor(number)