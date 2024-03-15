from psycopg import connect, DatabaseError, OperationalError

# to read and output all the students
def getAllStudents():
    cursor.execute("SELECT * FROM students")

# to add a student
def addStudent(first_name, last_name, email, enrollment_date):
    cursor.execute("""
    INSERT INTO students (first_name, last_name, email, enrollment_date)
    VALUES (%s, %s, %s, %s);
    """,
    (first_name, last_name, email, enrollment_date))
    
# to update a student's email where the student_id is specified
def updateStudent(student_id, new_email):
    cursor.execute("""
    UPDATE students SET email = %s WHERE student_id = %s
    """,
    (new_email, student_id))

# to delete a student from the table
def deleteStudent(student_id):
    cursor.execute("""DELETE FROM students WHERE student_id = %s""",
    (student_id,))



# code to connect to the database and perform the CRUD operations
try:
    conn = connect("dbname=school user=postgres password=postgres host=localhost")
    cursor = conn.cursor()

# READ
    # getAllStudents()
    # print(cursor.fetchall())

# WRITE
    # addStudent("Shreya", "Voore", "shreyavore@cmail.carleton.ca", datetime.date(2023, 3, 21).strftime('%Y-%m-%d'))

# UPDATE
    # updateStudent(5, "shreyavoore@cmail.carleton.ca")

# DELETE
    # deleteStudent(5)

    conn.commit()
    cursor.close()
    conn.close()
#exception handling
except (Exception, DatabaseError, OperationalError) as e:
    print(f"Error: {e}")
    exit()




