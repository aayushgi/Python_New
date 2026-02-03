import json

name = input("Enter name: ")
roll = int(input("Enter roll: "))
branch = input("Enter branch: ")

student = {
    "name": name,
    "roll": roll,
    "branch": branch
}

with open("students.json", "w") as file:
    json.dump({"students": [student]}, file, indent=4)

print("Student data saved in JSON file")
