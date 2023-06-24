import student
import course
import database as db


def add_student():
    student_id = input("Enter student ID: ")

    # Check if the student ID already exists in the database
    if student.student_exists(student_id):
        print("Student ID already exists. Please enter a different ID.")
        add_student()  # Prompt user for a new student ID
        return

    first_name = input("Enter first name: ")
    middle_initial = input("Enter middle initial: ")
    last_name = input("Enter last name: ")
    gender = input("Enter gender: ")
    year_level = input("Enter year level: ")
    course_code = input("Enter course code: ")

    # Check if the course code exists in the course database
    if not course.course_exists(course_code):
        choice = input("Course code does not exist. Do you want to add this course? (Yes/No): ")
        if choice.lower() == "yes":
            # Add the course to the course database
            course_name = input("Enter course name: ")
            course.create(course_code, course_name)
        else:
            print("Course not added. Student not added.")
            return

    # Continue with creating the student
    student.create(student_id, first_name, middle_initial, last_name, gender, year_level, course_code)
    print("Student added successfully!")
    input("Press Enter to Continue")


def add_course():
    print("----------")
    print("ADD COURSE")
    print("----------")
    course_code = input("Enter Course code: ")
    course_name = input("Enter Course name: ")
    course.create(course_code, course_name)
    print("Course added successfully!\n")
    input("Press Enter to Continue")


def search_course():
    cursor = db.connection.cursor()
    search_key = input("Search Course: ")

    # Execute the query to search for students matching the search key
    query = "SELECT * FROM course WHERE courseCode LIKE %s OR courseName LIKE %s"
    values = (f"%{search_key}%", f"%{search_key}%")
    cursor.execute(query, values)
    results = cursor.fetchall()

    if results:
        found = True
        for row in results:
            print("\nCourse Code: ", row[0])
            print("Course Title: ", row[1], "\n")
    else:
        found = False
        print("Course not found.\n")


def search_student():
    search_query = input("Enter search student: ")

    fields = ["StudentID", "FirstName", "MiddleInitial", "LastName", "Gender", "YearLevel", "CourseCode"]

    print("Search Results:")
    for field in fields:
        student.read_by_field(field, search_query)

    input("Press Enter to Continue")


def update_student():
    student_id = input("Enter student ID: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")

    # Find the student first
    student_data = student.find_student(student_id, first_name, last_name)

    if student_data:
        print("Student found:")
        print("Student ID:", student_data["StudentID"])
        print("First Name:", student_data["FirstName"])
        print("Last Name:", student_data["LastName"])
        print("Gender:", student_data["Gender"])
        print("Year Level:", student_data["YearLevel"])
        print("Course Code:", student_data["CourseCode"])

        # If the student is found, proceed with updating the information
        confirm = input("Confirm update? (Yes/No): ")
        if confirm.lower() == "yes":
            # Prompt for updated information
            new_first_name = input("Enter new first name: ")
            new_last_name = input("Enter new last name: ")
            new_gender = input("Enter new gender: ")
            new_year_level = input("Enter new year level: ")
            new_course_code = input("Please make sure the course code already exists. If not, create a new one.\n"
                                    "Enter the new course code: ")

            # Update the student information
            student.update(student_id, new_first_name, new_last_name, new_gender, new_year_level, new_course_code)
            print("Student information updated successfully!")
        else:
            print("Update canceled.")
    else:
        print("Student not found.")


def update_course():
    course_code = input("Enter course code: ")

    # Search for the course first
    course_data = course.read_update(course_code)

    if course_data:
        print("Course found:")
        print("Course Code:", course_data["CourseCode"])
        print("Course Name:", course_data["CourseName"])

        # Prompt user to confirm the update
        choice = input("Do you want to update this course? (Yes/No): ")
        if choice.lower() == "yes":
            new_course_code = input("Enter new course code (or press Enter to keep the current code): ")
            if not new_course_code:
                new_course_code = course_code
            new_course_name = input("Enter new course name: ")

            # Update the course information
            course.update(course_code, new_course_code, new_course_name)
            print("Course information updated successfully!")

            # Update references in other tables
            course.update_references(course_code, new_course_code)
            print("References in other tables updated successfully!\n")
        else:
            print("Course update canceled.")
    else:
        print("Course not found.")

    input("Press Enter to Continue")


def delete_course():
    course_code = input("Enter course code: ")

    # Check if the course exists
    if not course.course_exists(course_code):
        print("No course found with the given course code.")
        return

    choice = input("Are you sure you want to delete this course? (Yes/No): ")
    if choice.lower() == "yes":
        success = course.delete(course_code)

        if success:
            print("Course deleted successfully!")
        else:
            print("Failed to delete the course.")
    else:
        print("Course deletion canceled.")

    input("Press Enter to Continue")


def delete_student():
    student_id = input("Enter student ID: ")

    # Check if the student exists
    if not student.student_exists(student_id):
        print("No student found with the given ID.")
        return

    choice = input("Are you sure you want to delete this student? (Yes/No): ")
    if choice.lower() == "yes":
        student.delete(student_id)
        print("Student deleted successfully!")
    else:
        print("Student deletion canceled.")

    input("Press Enter to Continue")


def list_courses():
    course.list()
    input("Press Enter to Continue")


def list_students():
    student.list()
    input("Press Enter to Continue")


# Print out menu options
def student_info():
    print("1. Add Student Information")
    print("2. Search Student Information")
    print("3. Update Student Information")
    print("4. Delete Student Information")
    print("5. List of Students")
    print("6. Exit")


def student_course():
    print("1. Add Course")
    print("2. Search Course")
    print("3. Update Course")
    print("4. Delete Course")
    print("5. List of Courses")
    print("6. Exit")


def main():
    while True:
        print("---------------------------------")
        print("Simple Student Information System")
        print("---------------------------------")
        print("1. CRUDL for Student Information")
        print("2. CRUDL for Courses")
        print("3. Exit")

        option = input("Enter your choice: ")

        if option == '1':
            while True:
                student_info()

                option1 = input("Enter your choice: ")

                if option1 == '1':
                    add_student()
                elif option1 == '2':
                    search_student()
                elif option1 == '3':
                    update_student()
                elif option1 == '4':
                    delete_student()
                elif option1 == '5':
                    list_students()
                elif option1 == '6':
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif option == '2':
            while True:
                student_course()

                option2 = input("Enter your choice: ")

                if option2 == '1':
                    add_course()
                elif option2 == '2':
                    search_course()
                elif option2 == '3':
                    update_course()
                elif option2 == '4':
                    delete_course()
                elif option2 == '5':
                    list_courses()
                elif option2 == '6':
                    break
                else:
                    print("Invalid choice. Please try again.")

        elif option == '3':
            print("Thank You For Using This System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
