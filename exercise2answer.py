history_class = {"Clancy":  
                  {"hw_grades": [10, 10, 9, 9], 
                  "exam_grades": [94, 91, 97], 
                  "participation": 10}, 
                 "Reba": 
                  {"hw_grades": [8, 9, 8, 10], 
                  "exam_grades": [89, 90, 94], 
                  "participation": 10}, 
                 "Leila": 
                  {"hw_grades": [8, 7, 6, 5], 
                  "exam_grades": [74, 80, 79, 68], 
                  "participation": 10}, 
                 "Ami": 
                  {"hw_grades": [10, 9, 10, 10], 
                  "exam_grades": [98, 97, 98, 91], 
                  "participation": 10}}

"""
You stored the dictionary of dictionaries above. Create a variable 
called 'Reba_p' that stores Reba's participation grade. You will
not need any loops or conditionals, just index the dictionaries
with the appropriate keys.
"""

Reba_p = history_class["Reba"]["participation"]


print("Reba's participation grade is:")
print(Reba_p)


"""
Create a new dictionary called hw_averages. It should have
each student's name as keys and each student's average hw score
as the values.
"""
#create an empty dictionary:
hw_averages = {}
#write a for loop to loop through the keys of the outer dictionary:
for student in history_class.keys():
    #calculate a student's average hw score:
    hw_scores = history_class[student]["hw_grades"]
    hw_avg = sum(hw_scores) / len(hw_scores)
    #add the score to the hw_averages dictionary:
    hw_averages[student] = hw_avg
    
print(hw_averages)

