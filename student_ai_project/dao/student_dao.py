from db.db import get_db_connection

def save_prediction(data, marks, result):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    insert into student_predictions (age, study_hours, attendance, sleep_hours, marks, result)
    
    values (%s, %s, %s, %s, %s, %s)"""

    values = (
        data['age'],
        data['study_hours'],
        data['attendance'],
        data['sleep_hours'],
        marks,
        result
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

def get_all_predictions(limit):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    select * from student_predictions order by id desc limit %s"""

    cursor.execute(query, (limit,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

