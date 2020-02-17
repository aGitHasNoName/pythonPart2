#Good practice to assign your file path to a variable
alice_filename = "alice.txt"
dog_filename = "dogs.txt"
grades_filename = "gradebook.csv"


with open(alice_filename, "r") as f:
    print(f)

