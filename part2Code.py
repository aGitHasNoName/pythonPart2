#grades = [73, 64, 89, 93, 59, 100, 79]
#1
#for grade in grades:
#	print(grade)
#Notice that the order matches

#1.5
#for g in grades:
#	print(g)
	
#2	
#for g in grades:
#	print(g + 5)

#3	
#new_grades = []

#for g in grades:
#	new_grades.append(g + 5)
	
#print(new_grades)

#4 More explicit for more complicated calculations
#new_grades = []

#for g in grades:
#	new_g = g + 5
#	new_grades.append(new_g)
	
#print(new_grades)

#5 ERROR
#for g in grades:
#	print(grade)
	
#6 ERROR
#for g in grades
#	print(g)

#7 ERROR
#for g in grades:
#print(g)

#8 BOOLEANS
#for g in grades:
#	if g >= 90:
#		print(g)
#		print("grade is A")
#	elif g >= 80:
#		print(g)
#		print("grade is B")
#	elif g >= 70:
#		print(g)
#		print("grade is C")
#	elif g >= 60:
#		print(g)
#		print("grade is D")
#	else:
#		print(g)
#		print("grade is Fail")

#9
#passing_grades = []
#for g in grades:
#	if g >= 60:
#		passing_grades.append(g)
#print(passing_grades)

#10 More explicit
#passing_grades = []
#for g in grades:
#	if g >= 60:
#		passing_grades.append(g)
#	else:
#		pass
#print(passing_grades)

#11 Break
#for g in grades:
#	if g >= 70:
#		print("This student is doing ok.")
#	else:
#		print("I give up. I quit.")
#		break

#12 Predict:
#for g in grades:
#	if g >= 70:
#		print("This student is doing ok.")
#	else:
#		break
#		print("I give up. I quit.")

#13 New boolean operator
#grades_to_round = [59, 69, 79, 89]
#rounded_grades = []
#for g in grades:
#	if g in grades_to_round:
#		rounded_grades.append(g + 1)
#	else:
#		rounded_grades.append(g)
		
#print(rounded_grades)

#14 not in
#grades_to_round = [59, 69, 79, 89]
#rounded_grades = []
#for g in grades:
#	if g not in grades_to_round:
#		rounded_grades.append(g)
#	else:
#		rounded_grades.append(g + 1)
		
#print(rounded_grades)


#grade_dict = {"Charlie": [90, 96, 89, 79], 
#             "Tony": [99, 98, 96, 93], 
#             "Suman": [85, 88, 83, 87],
#             "Yuvie": [66, 76, 80, 62],
#             "May": [97, 94, 89, 91]}
#1
#print(grade_dict)

#1.5 Index
#print(grade_dict["Tony"])

#1.75
#print(grade_dict["Tony"][-1])

#1.8 Add entry to dict
#grade_dict["Ben"] = [82, 88, 90]

#2 loop
#for entry in grade_dict:
#	print(entry)

#3
#for key in grade_dict.keys():
#	print(key)
	
#for value in grade_dict.values():
#	print(value)

#4	
#for k in grade_dict.keys():
#	print(k)
	
#for v in grade_dict.values():
#	print(v)
	
#5
#for k in grade_dict.keys():
#	print(k)
	
#for k in grade_dict.values():
#	print(k)
	
#6
#for k, v in grade_dict.items():
#	print(k)
#	print(v)
	
#7
#for student, grade_list in grade_dict.items():
#	print(student)
#	print(grade_list)
	
#8
#for student, grade_list in grade_dict.items():
#	print(student)
#	for grade in grade_list:
#		print(grade)

#9 assigning to empty dict
#final_dict = {}
#for student, grade_list in grade_dict.items():
#	final_grade = sum(grade_list) / len(grade_list)
#	final_dict[student] = final_grade
#print(final_dict)

#10 With conditional
#final_dict = {}
#for student, grade_list in grade_dict.items():
#	if len(grade_list) < 4:
#		print(student + " has missing grades.")
#	else:
#		final_grade = sum(grade_list) / len(grade_list)
#		final_dict[student] = final_grade
#print(final_dict)

#11 fail - expect TypeError
#grade_dict["Ben"].append("Missed")

#final_dict = {}
#for student, grade_list in grade_dict.items():
#	final_grade = sum(grade_list) / len(grade_list)
#	final_dict[student] = final_grade
	
#print(final_dict)

#12 Try/except fix
#grade_dict["Ben"].append("Missed")

#final_dict = {}
#for student, grade_list in grade_dict.items():
#	try:
#		final_grade = sum(grade_list) / len(grade_list)
#		final_dict[student] = final_grade
#	except TypeError:
#		print(student + " has missing grades.")
	
#print(final_dict)


alice_filename = "alice.txt"
dog_filename = "dogs.txt"
grades_filename = "gradebook.csv"

#1 Won't work
#with open(alice_filename, "r") as f:
#    print(f)

#2 read function
#with open(alice_filename, "r") as f:
#	alice_text = f.read()
#print(alice_text)

#3 the f can be anything, just like in a for loop
#with open(alice_filename, "r") as fffff:
#	alice_text = fffff.read()
#print(alice_text)

#4 readlines function
#with open(alice_filename, "r") as f:
#	alice_lines = f.readlines()

#print(len(alice_lines))
	
#for line in alice_lines:
#	if "Alice" in line:
#		print(line)

#5 
#with open(dog_filename, "r") as f:
#	dog_lines = f.readlines()
	
#for line in dog_lines:
#	print(line)

#6 remove new line characters - rstrip function
#with open(dog_filename, "r") as f:
#	dog_lines = f.readlines()

#for line in dog_lines:
#	print(line.rstrip("\n"))
	
#7 make a list from a file
#dog_list = []
#with open(dog_filename, "r") as f:
#	for line in f.readlines():
#		dog_list.append(line.rstrip("\n"))
		
#print(dog_list)

#Comment that out because we might want to use it later

#8
#with open(grades_filename, "r") as f:
#	gradebook = f.readlines()

#for line in gradebook:
#	print(line)

#9 it is a list of lines
#with open(grades_filename, "r") as f:
#	gradebook = f.readlines()

#print(gradebook[0])
	
#10 Let's turn the gradebook file into a dictionary
# and learn the split function
#with open(grades_filename, "r") as f:
#	gradebook = f.readlines()

#gradebook = gradebook[1:]

#grade_dict = {}

#for line in gradebook:
#	line = line.split(",")
#	print(line)

#11 Using logic to figure out a way to do it
with open(grades_filename, "r") as f:
	gradebook = f.readlines()

grade_dict = {}

for line in gradebook[1:]:
	line = line.rstrip("\n").split(",")
	grade_dict[line[0]] = []
	for i in line[1:]:
		grade_dict[line[0]].append(i)
		
#print(grade_dict)
	
#12 write a file
with open("homeworkReport.txt", "w") as f:
	for student, grades in grade_dict.items():
		to_print = student + " earned the following grades on homework: "
		to_print2 = str(grades[0]) + ", " + str(grades[1]) + ", " + str(grades[2]) + "\n"
		f.write(to_print + to_print2)



