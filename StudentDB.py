import mysql.connector

mydb = mysql.connector.connect(
    host="deltona.birdnest.org",
    user="my.leep7",
    password="",
    database="sample"
)

mycursor = mydb.cursor() #these can be inserted into the class StudentDB
sql_create = "INSERT INTO students (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
sql_create = "INSERT INTO courses (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
sql_create = "INSERT INTO grades (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
sql_edit = "UPDATE students SET name = %s, age = %s WHERE id = %s"
sql_edit = "UPDATE grades SET name = %s, age = %s WHERE id = %s"
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
    print("6. Select Student")
    print("7. Delete Student")
    print("8. Exit")
    return input("Choice: ")


def main(): #

    while True:  #keeps showing the menu until user chooses 
        choice = menu()

        if choice == '1':
            db.add_student(
                input("First Name: "),
                input("Last Name: "),
                input("Email: "),
                input("Phone: ")
            )

        if choice == '2':
            db.add_course(
                input("Course ID: "), 
                input("Course Name")

            )

        if choice == '3':
            db.add_grade(
                int(input("Student ID: ")),
                int(input("Course ID: ")),
                input("Grade: ")
            )

        if choice == '4':
            db.update_student(
                int(input("Student ID: ")),
                input("New Email: "),
                input("New Phone: ")
            )

        if choice == '5':
            db.update_grade(
                int(input("Grade ID: ")),
                input("New Grade: ")
            )

         if choice == '6':
            db.show_students()

        if choice == '7':
            db.delete_student(int(input("Student ID: ")))

        if choice == '8':
            print("Bye!")
            break

        else:
            print("Invalid choice!")




