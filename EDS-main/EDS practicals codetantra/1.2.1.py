n = int(input( ))
marks = list(map(int,input().split( )))

if any(mark < 40 for mark in marks) :
	print("Fail")
else:
	percentage = sum(marks)/n
	if(percentage > 75) :
		grade = "Distinction"
	elif(percentage >= 60 ) :
		grade = "First Division"
	elif(percentage >= 50) :
		grade = "Second Division"
	else:
		grade = "Third Division"
	print(f"Aggregate Percentage:{percentage: .2f}")
	print(f"Grade: {grade}")