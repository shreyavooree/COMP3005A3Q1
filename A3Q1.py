from psycopg import connect, DatabaseError, OperationalError

# to read and output all the students
def getAllStudents():
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=school user=postgres password=postgres host=localhost")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM students")

        conn.commit()
        print(cursor.fetchall())
        cursor.close()
        conn.close()
#exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

# to add a student
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=school user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO students (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s);
        """,
        (first_name, last_name, email, enrollment_date))
        
        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()
    
# to update a student's email where the student_id is specified
def updateStudent(student_id, new_email):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=school user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""
        UPDATE students SET email = %s WHERE student_id = %s
        """,
        (new_email, student_id))
    
        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()

# to delete a student from the table
def deleteStudent(student_id):
    try:
        # code to connect to the database and perform the CRUD operations
        conn = connect("dbname=school user=postgres password=postgres host=localhost")
        cursor = conn.cursor()

        cursor.execute("""DELETE FROM students WHERE student_id = %s""",
        (student_id,))

        conn.commit()
        cursor.close()
        conn.close()
    #exception handling
    except (Exception, DatabaseError, OperationalError) as e:
        print(f"Error: {e}")
        exit()
