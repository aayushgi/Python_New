#Append new data to existing CSV file
import csv

# new student
new_student = ["Neha", 103, "IT"]

# append 
with open("student.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_student)

print("New studend appended successfully")
