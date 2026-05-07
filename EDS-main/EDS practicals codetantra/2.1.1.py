# write the code..
l1 = []
while(True):
	print("1. Add\n2. Remove\n3. Display\n4. Quit")
	ch = int(input("Enter choice: "))

	if(ch==1):
		n = int (input("Integer: "))
		l1.append(n)
		print(f"List after adding: {l1}")
	elif(ch==2):
		if(l1==[]):
			print("List is empty")
		else:
			m = int (input("Integer: "))
			if m in l1:
				l1.remove(m)
				print(f"List after removing: {l1}")
			else:
				print("Element not found")
	elif(ch==3):
		if(l1==[]):
			print("List is empty")
		else:
			print(l1)
	elif(ch>4):
		print("Invalid choice")
	elif(ch==4):
		break