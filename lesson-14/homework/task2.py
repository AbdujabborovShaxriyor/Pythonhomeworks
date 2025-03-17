import numpy as np

@np.vectorize
def rise_to_power(x,y):
    return x**y

base = np.array([2, 3, 4, 5])
power = np.array([1, 2, 3, 4])
print(rise_to_power(base,power))