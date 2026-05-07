import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

sortarr = np.sort(array1)
# Find indices where value matches in array1
index = np.where(array1 == search_value)[0]
index = np.array(index)
print(index)
# Count occurrences in array1
count = 0
for i in range(len(array1)):
	if count_value == array1[i]:
		count+=1
print(count)
# Broadcasting addition
array1 = array1 + broadcast_value
print(array1)
# Sort the first array
print(sortarr)