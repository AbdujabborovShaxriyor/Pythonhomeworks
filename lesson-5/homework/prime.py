n = int(input("Enter the number: "))
def is_prime(n):
    checker=0
    for i in range(2,n//2+1):
        if n%i==0:
            checker+=1
    if checker!=0:
        print(False)
    else:
        print(True)
is_prime(n)
        