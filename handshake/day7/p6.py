#Convert dictionary to JSON and save.
import json
#dictonary
employee={
    "name":"ayush",
    "empid":122,
    "salary":50000,
    "department":"IT"

}
with open("employee.json","w") as file:
    json.dump(employee,file,indent=4)
print("employees data will save succesfully")