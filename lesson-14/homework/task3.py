import numpy as np

coefficients = np.array([[4,5,6],[3,-1,1],[2,1,-2]])
ys = np.array([7,4,5])

result = np.linalg.solve(coefficients,ys)