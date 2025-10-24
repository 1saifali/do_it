import psycopg2
import bcrypt

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="user_auth",
        user="postgres",
        password="saif"
    )

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def insert_user(username, password):
    hashed_pw = hash_password(password)
    conn = get_connection()
    cur = conn.cursor()

    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    cur.execute(query, (username, hashed_pw))
    conn.commit()

    cur.close()
    conn.close()
    print(f"User '{username}' inserted successfully.")

def get_tasks(username):
    conn = get_connection()
    cur = conn.cursor()
    query = "SELECT id, title, task_date FROM tasks WHERE username = %s ORDER BY task_date"
    cur.execute(query, (username,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "title": r[1], "date": r[2]} for r in rows]

def update_task(task_id, new_title, new_date):
    """
    Update an existing task's title and date in the database.

    Args:
        task_id (int): The ID of the task to update.
        new_title (str): The updated title for the task.
        new_date (date): The updated date for the task.
    """
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = """
            UPDATE tasks
            SET title = %s, task_date = %s
            WHERE id = %s
        """
        cur.execute(query, (new_title, new_date, task_id))
        conn.commit()

    except Exception as e:
        print(f"❌ Error updating task {task_id}: {e}")
        raise e  # optional: re-raise to handle in Streamlit

    finally:
        cur.close()
        conn.close()





def insert_task(username, title, task_date):
    conn = get_connection()
    cur = conn.cursor()
    query = "INSERT INTO tasks (username, title, task_date) VALUES (%s, %s, %s)"
    cur.execute(query, (username, title, task_date))
    conn.commit()
    cur.close()
    conn.close()


def delete_task(task_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    cur.close()
    conn.close()
