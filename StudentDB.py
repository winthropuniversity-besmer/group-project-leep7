import mysql.connector

mydb = mysql.connector.connect(
    host="deltona.birdnest.org",
    user="my.leep7",
    password="547%9sb2i",
    database="my_leep7_StudentDB"
)

mycursor = mydb.cursor() #these can be inserted into the class StudentDB

sql_createStudents = "INSERT INTO Students (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
sql_createCourses = "INSERT INTO Courses (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
sql_createGrades = "INSERT INTO Grades (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
sql_editStudents = "UPDATEGtudents SET name = %s, age = %s WHERE id = %s"
sql_editGrades = "UPDATE Grades SET name = %s, age = %s WHERE id = %s"
sql_editCourses = "UPDATE Courses SET name = %s, age = %s WHERE id = %s"
sql_selectStudent = "SELECT * FROM Students" #Commands for cursor to execute to select from the 3 tables
sql_selectCourse = "SELECT * FROM Courses"
sql_selectGrade = "SELECT * FROM Grades"
sql_delete = "DELETE FROM students where id = %s"


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




