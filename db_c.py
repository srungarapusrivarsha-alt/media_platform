import mysql.connector 
import streamlit as st 

def get_connection():
    conn = mysql.connector.connect(
        host=st.secrets["host"],
        port=int(st.secrets["port"]),
        user=st.secrets["user"],
        password=st.secrets["password"],
        database=st.secrets["db"],
        ssl_disabled=False
    )
    cursor = conn.cursor(dictionary=True)
    return conn, cursor

def create_tables():                          
    conn, cursor = get_connection()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        password VARCHAR(100)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS files(
        id INT PRIMARY KEY AUTO_INCREMENT,
        user_id INT,
        file_name VARCHAR(255),
        file_type VARCHAR(100),
        file_url TEXT,
        upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    """)

    conn.commit()
    conn.close()
print("Tables Created Successfully")