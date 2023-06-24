import database as db


def create(student_id, first_name, middle_initial, last_name, gender, year_level, course_code):
    cursor = db.connection.cursor()

    query = "INSERT INTO student" \
            "(studentID, FirstName, MiddleInitial, LastName, Gender, YearLevel, CourseCode)" \
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"

    value = (student_id, first_name, middle_initial, last_name, gender, year_level, course_code)
    cursor.execute(query, value)
    db.connection.commit()


def read_by_student_id(student_id):
    cursor = db.connection.cursor()

    query = "SELECT * FROM student WHERE StudentID = %s"

    cursor.execute(query, (student_id,))
    records = cursor.fetchall()

    if len(records) > 0:
        print("STUDENT FOUND")
        for row in records:
            print(row)


def read_by_first_name(first_name):
    cursor = db.connection.cursor()

    query = "SELECT * FROM student WHERE FirstName LIKE %s"

    cursor.execute(query, (f"%{first_name}%",))
    records = cursor.fetchall()

    if len(records) > 0:
        print("STUDENT FOUND")
        for row in records:
            print(row)


def read_by_last_name(last_name):
    cursor = db.connection.cursor()

    query = "SELECT * FROM student WHERE LastName LIKE %s"

    cursor.execute(query, (f"%{last_name}%",))
    records = cursor.fetchall()

    if len(records) > 0:
        print("STUDENT FOUND")
        for row in records:
            print(row)


def read_by_field(field_name, search_query):
    cursor = db.connection.cursor()

    query = f"SELECT * FROM student WHERE {field_name} LIKE %s"

    cursor.execute(query, (f"%{search_query}%",))
    records = cursor.fetchall()

    if len(records) > 0:
        print("STUDENT FOUND")
        for row in records:
            print(row)


def update(student_id, first_name, last_name, gender, year_level, course_code):
    cursor = db.connection.cursor()
    query = """
    UPDATE student
    SET FirstName = %s, LastName = %s, Gender = %s, YearLevel = %s, CourseCode = %s
    WHERE studentID = %s
    """
    values = (first_name, last_name, gender, year_level, course_code, student_id)

    # Execute the query
    cursor.execute(query, values)
    db.connection.commit()


def delete(student_id):
    cursor = db.connection.cursor()

    query = "DELETE FROM student WHERE studentID = %s"

    cursor.execute(query, (student_id,))
    db.connection.commit()


def student_exists(student_id):
    cursor = db.connection.cursor()

    query = "SELECT COUNT(*) FROM student WHERE StudentID = %s"
    cursor.execute(query, (student_id,))

    count = cursor.fetchone()[0]
    return count > 0


def list():
    cursor = db.connection.cursor()

    query = "SELECT * FROM student"

    cursor.execute(query)
    records = cursor.fetchall()

    print("List of Student Information")
    for row in records:
        print(row)


def find_student(student_id, first_name, last_name):
    cursor = db.connection.cursor()

    query = "SELECT * FROM student WHERE studentID = %s AND FirstName = %s AND LastName = %s"

    cursor.execute(query, (student_id, first_name, last_name))
    # Get the first record
    record = cursor.fetchone()

    if record is None:
        return None
    else:
        student_data = {
            "StudentID": record[0],
            "FirstName": record[1],
            "MiddleInitial": record[2],
            "LastName": record[3],
            "Gender": record[4],
            "YearLevel": record[5],
            "CourseCode": record[6]
        }
        return student_data
