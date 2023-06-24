import database as db


def create(course_code, course_name):
    cursor = db.connection.cursor()

    query = "INSERT INTO course"\
            "(CourseCode, CourseName)"\
            "VALUES (%s, %s)"

    value = (course_code, course_name)

    cursor.execute(query, value)
    db.connection.commit()



def update(old_course_code, new_course_code, new_course_name):
    cursor = db.connection.cursor()

    query = "UPDATE course SET CourseCode = %s, CourseName = %s WHERE CourseCode = %s"
    values = (new_course_code, new_course_name, old_course_code)

    cursor.execute(query, values)
    db.connection.commit()


def update_references(old_course_code, new_course_code):
    cursor = db.connection.cursor()

    query = "UPDATE student SET CourseCode = %s WHERE CourseCode = %s"
    values = (new_course_code, old_course_code)

    cursor.execute(query, values)
    db.connection.commit()


def delete(course_code):
    cursor = db.connection.cursor()

    query = "DELETE FROM course WHERE CourseCode = %s"

    cursor.execute(query, (course_code,))
    deleted_rows = cursor.rowcount
    db.connection.commit()

    return deleted_rows > 0


def list():
    cursor = db.connection.cursor()

    query = "SELECT * FROM course"

    cursor.execute(query)
    records = cursor.fetchall()

    print("List of Courses")
    for row in records:
        print(row)


def read_update(course_code):
    cursor = db.connection.cursor()

    query = "SELECT CourseCode, CourseName FROM course WHERE CourseCode = %s"
    values = (course_code,)

    cursor.execute(query, values)
    result = cursor.fetchone()

    if result:
        course_data = {
            "CourseCode": result[0],
            "CourseName": result[1]
        }
        return course_data
    else:
        return None
