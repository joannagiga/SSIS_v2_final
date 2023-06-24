import mysql.connector

connection = mysql.connector.connect(
    user='root',
    password='12345',
    host='127.0.0.1',
    database='student_information_db'
)