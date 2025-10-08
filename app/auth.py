from .db import get_connection
import bcrypt

def authenticate_user(username, password):
    conn = get_connection()
    cur = conn.cursor()

    query = "SELECT id, password FROM users WHERE username = %s"
    cur.execute(query, (username,))
    result = cur.fetchone()

    cur.close()
    conn.close()

    if result:
        user_id, hashed_password = result
        if bcrypt.checkpw(password.encode(), hashed_password.encode()):
            return user_id
    return None
