"""
I created this list of students on my iPhone.
Unfortunately, my screen is cracked and I can't
type the letter 'a'. Instead, I put the letter
'x' everywhere that there should be an 'a'.
Write a script to create a new list of students 
with the correct spellings.
"""

students = ["Chen", "Cxsey", "Brxndon", "Xndre", "Rui", "Dxve"]

#First, create a new empty list:
corrected_students = []

#Code a for loop to replace the x's with a's, and append them to the new list:
for s in students:
    new_s = s.replace("x", "a").replace("X", "A")
    corrected_students.append(new_s)

#Print the new list:
print(corrected_students)



"""
Challenge question: What if there was also a student
in the class named 'Alex', whose final 'x' should
stay? Type 'Xlex' in the list above and write a new
for loop.
"""

students = ["Chen", "Cxsey", "Brxndon", "Xndre", "Rui", "Dxve", "Xlex"]

#First, create a new empty list:
corrected_students = []

#Code a for loop to replace the x's with a's:
for s in students:
    if s == "Xlex":
        corrected_students.append("Alex")
    else:
        new_s = s.replace("x", "a").replace("X", "A")
        corrected_students.append(new_s)

#Print the new list:
print(corrected_students)