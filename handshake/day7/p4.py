
#Create a JSON file storing student info.
import json
student={
    "name":"shyam",
    "rollno":12,
    "marks":{
        "physics":123,
        "maths":243,
        "art":0
    }
}
file=open("student.json","w")
json.dump(student,file)
file.close()