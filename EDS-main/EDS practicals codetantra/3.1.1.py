import numpy as np
rows, columns = map(int,input().split())
arr1 = []
for i in range (rows):
	row = list(map(int,input().split()))
	arr1.extend(row)
arr2 = np.array(arr1).reshape(rows, columns)
print(arr2)
print(arr2.ndim)
print(arr2.shape)
print(arr2.size)