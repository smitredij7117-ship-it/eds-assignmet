# Initial dictionary with 10 predefined records
student = {
    1: "Amit",
    2: "Riya",
    3: "Kiran",
    4: "Neha",
    5: "Arjun",
    6: "Pooja",
    7: "Rahul",
    8: "Sneha",
    9: "Vikram",
    10: "Anjali"
}

# write your code here...
print(f"Original Dictionary: {student}")
new_key = int(input())
new_value = str(input())
student[new_key]=new_value
print(f"After Insertion: {student}")

upkey = int(input())

if upkey in student:
	upvalue = str(input())
	student[upkey] = upvalue
	print(f"After Update: {student}")
else: print(f"After Update: {student}")
	
delkey = int(input())
if delkey in student:
	del student[delkey]
	print(f"After Deletion: {student}")
else: print(f"After Deletion: {student}")

print("Traversing Dictionary:")
for k,v in student.items():
	print(f"{k} : {v}")