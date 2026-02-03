#Handle file-not-found error gracefully.
try:
    file = open("student.txt", "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("Error: File not found. Please check the file name or path.")
