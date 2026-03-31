                            STUDENT RESULT ANALYZER
Description:
This is a Python-based project used to manage student data, marks, and results.
It allows users to add students, enter marks, calculate results, and generate report cards.

-----------------------------------------------------------------------------------------------
Features:

* Add student details (roll number, name, class)
* Enter marks for subjects (Python, Maths, DBMS, OS)
* Calculate total, percentage, and grade
* Search students by grade
* Generate subject topper report
* Export report card to text file
* Save and load data using JSON
* Delete student records
* Error logging system (errors stored in error_log.txt)

-------------------------------------------------------------------------------------------------

Project Structure:

student_result_analyzer/
│
├── main.py
├── error_log.txt
├── README.txt
│
├── data/
│   └── students.json
│
├── templates/
│   └── report_<roll>.txt

------------------------------------------------------------------------------------------------

How to Run:

1. Install Python (if not installed)
2. Open terminal in project folder
3. Run the program using:

   python main.py

-------------------------------------------------------------------------------------------------

Usage:

* Select options from menu (1–10)
* Follow instructions on screen
* Data will be saved in 'data' folder
* Report cards will be saved in 'templates' folder

--------------------------------------------------------------------------------------------------

Error Handling:

* All runtime errors are saved in:
  error_log.txt

* Example:
  invalid input (like entering 'abc' instead of number)

---------------------------------------------------------------------------------------------------

Author:
Ayush Saxena

