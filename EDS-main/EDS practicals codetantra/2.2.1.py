
arr = list(map(int, input().split()))


key = int(input().strip())


index = -1
for i in range(len(arr)):
	if arr[i] == key:
		index = i
		break


if index == -1:
	print("Not found")
else:
	print(index)