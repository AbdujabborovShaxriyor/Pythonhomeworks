def check(func):
    def wrapper(a,b):
        if b==0:
            raise ZeroDivisionError("you cannot divide by zero")
        return func(a,b)
    return wrapper

@check
def div(a, b):
   return a / b

div(10,0)