import mysql.connector

class StudentDB:

   
def menu(): #shows the choices 
    print("1. Add Student")
    print("2. Add Course")
    print("3. Add Grade")
    print("4. Update Student")
    print("5. Update Grade")
    print("6. Delete Student")
    print("7. Exit")
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
            db.delete_student(int(input("Student ID: ")))

        if choice == '7':
            print("Bye!")
            break

        else:
            print("Invalid choice!")


