import numpy as np

coefficients = np.array([[10,-2,3],[-2,8,-1],[3,-1,6]])
ys = np.array([12,-5,15])

result = np.linalg.solve(coefficients,ys)