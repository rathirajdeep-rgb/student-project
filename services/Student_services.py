from db.db import get_db_connection
#Addition of student
def add_student(first_name, last_name, dob, email):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO students (first_name, last_name, dob, email)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (first_name, last_name, dob, email))
    conn.commit()

    print("Student added successfully")
    cursor.close()
    conn.close()

# Search of student by email
def get_student_by_email(email):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    select first_name, last_name, dob, email
    from students where email = %s
    """

    cursor.execute( query, (email,))
    student = cursor.fetchone()

    cursor.close()
    conn.close()
    return student

# Search of student by email
def get_student_by_first_name(first_name):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    select first_name, last_name, dob, email
    from students where first_name = %s
    """

    cursor.execute(query, (first_name,))
    student = cursor.fetchone()

    cursor.close()
    conn.close()
    return student