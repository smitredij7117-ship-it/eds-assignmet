# Type Content here...
n = int(input())
for i in range(1,n+1):
	for j in range (1,i+1):
		print(j,end=" ") #this prints j value but it give space in end after printing so it should not go on next line
	print() # this is to make a new line after every j loop ends 