n = int(input())

if(0<=n<10) :
	print(n*n)
elif(10<=n<100) :
	print("%.2f"%(n**(1/2)))
elif(100<=n<1000) :
	print("%.2f"%(n**(1/3)))
else :
	print("Invalid")