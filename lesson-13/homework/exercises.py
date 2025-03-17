import numpy as np

vector = np.arange(10, 50)
matrix = np.arange(9).reshape(3, 3)
identity_matrix = np.eye(3)
random_arr = np.random.rand(3, 3, 3)
arr_10 = np.random.rand(10,10)
max_arr10 = np.max(arr_10)
min_arr10 = np.min(arr_10)
random_vec = np.random.randint(1,100,size=30)
random_vec_mean = np.mean(random_vec)
matrix5_3 = np.random.randint(5,3)
matrix3_2 = np.random.randint(3,2)
matrix_product = matrix5_3 @ matrix3_2
a3_3 = np.random.randint(3,3)
b3_3 = np.random.randint(3,3)
dot_product = np.dot(a3_3,b3_3)
a4_4 = np.random.randint(4,4)
transpose4_4 = np.transpose(a4_4)
determinant = np.linalg.det(a3_3)
matrix3_4 =  np.random.randint(3,4)
matrix4_3 =  np.random.randint(4,3)
dot_product2 = matrix3_4 @ matrix4_3
elem3 = np.array([1,2,3])
dot_product3 = a3_3 @ elem3
b3_1 = np.random.randint(3,1)
b3_1 = np.linalg.inv(b3_1)
dot_division = b3_1 @ a3_3
a5_5 = np.random.randint(5,5)
row_sum=np.sum(a5_5,axis=1)
column_sum = np.sum(a5_5,axis=0)
