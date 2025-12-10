import mysql.connector

mydb = mysql.connector.connect(
    host="deltona.birdnest.org",
    user="my.leep7",
    password="547%9sb2i",
    database="my_leep7_StudentDB"
)

mycursor = mydb.cursor() #these can be inserted into the class StudentDB

sql_createstudents = "INSERT INTO Students (student_id, first_name, last_name, email, phone_number) VALUES (6, Elena, Gilbert, salvatored@winthrop.edu, 4432822612)"
sql_createcourses = "INSERT INTO Courses (course_id, course_name) VALUES (106, 'Culinary Arts')"
sql_creategrades = "INSERT INTO Grades (student_id, course_id, grade) VALUES (6, 106, 'B')"
sql_editstudents = "UPDATE Students SET last_name = 'Salvatore', email = 'salvatorej@winthrop.edu' WHERE student_id = 2"
sql_editgrades = "UPDATE Grades SET course_id = 102 WHERE student_id = 5"
sql_editcourses = "UPDATE Courses SET course_name = 'Fine Arts' WHERE course_id = 105"
sql_selectstudent = "SELECT * FROM students" #Commands for cursor to execute to select from the 3 tables
sql_selectcourse = "SELECT * FROM courses"
sql_selectgrade = "SELECT * FROM grades"
sql_delete = "DELETE FROM Students where id = %s"


class StudentDB:
    
def add students(self,first_name, last_name, email,):
def add courses(self, course_id, course_name):
def add grades(self, grade_id, student_id, course_id, grade);
def select students(self); 
def update student(self, student_id):
def update grades():
def delete student():

   
def menu(): #shows the choices 
    print("1. Add Student")
    print("2. Add Course")
    print("3. Add Grade")
    print("4. Update Student")
    print("5. Update Grade")
    print("6. Search Student")
    print("7. Search Course")
    print("8. Search Grade")
    print("9. Delete Grade")
    print("10. Exit")
    return input("Choice: ")


def main():
    choice = 0
    while choice != 10:
        os.system('cls')
        choice = int(menu())

        match choice:    
            case 1:
                db.add_student(
                input("First Name: "),
                input("Last Name: "),
                input("Email: "),
                input("Phone: ")
                )
            case 2:
                db.add_student(
                input("First Name: "),
                input("Last Name: "),
                input("Email: "),
                input("Phone: ")
                )

            case 3:
                db.add_grade(
                int(input("Student ID: ")),
                int(input("Course ID: ")),
                input("Grade: ")
                )
            case 4:
                 db.update_student(
                int(input("Student ID: ")),
                input("New Email: "),
                input("New Phone: ")
                )
            case 5:
                db.update_grade(
                int(input("Grade ID: ")),
                input("New Grade: ")
                )
            case 6:
                student = int(input("Provide Student ID: "))
                mycursor.execute(sql_selectStudent, (student,))
                output = mycursor.fetchall()
                for row in output:
                    print(row)
                input("Press Enter to continue...")
            case 7:
                course = int(input("Provide Course ID: "))
                mycursor.execute(sql_selectCourse, (course,))
                output = mycursor.fetchall()
                for row in output:
                    print(row)
                input("Press Enter to continue...")
            case 8:
                grade = int(input("Provide Grade ID: "))
                mycursor.execute(sql_selectGrade, (grade,))
                output = mycursor.fetchall()
                for row in output:
                    print(row)
                input("Press Enter to continue...")
            case 9:
                db.delete_student(int(input("Student ID: ")))
            case 10:
                print("Bye!")
                mycursor.close()
                mydb.close()
                break
            case _:
                print("Invalid choice!")

main()









