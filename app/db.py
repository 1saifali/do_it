# import psycopg2

# #Database connection function
# def get_connection():
#     return psycopg2.connect(
#         host="localhost",
#         database="user_auth",
#         user="postgres",
#         password="saif"


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

# Run this once to insert users with hashed passwords
# insert_user('testuser1', 'testpass1')
# insert_user('admin1', 'admin1231')
