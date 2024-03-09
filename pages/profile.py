import streamlit as st
import mysql.connector
import pandas as pd

def profile():
    # ดึงค่า username จาก query parameters ใน URL
    username = st.experimental_get_query_params().get("username", [""])[0]

    # เชื่อมต่อกับฐานข้อมูล MySQL
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="omr"
    )
    
    cursor = conn.cursor()

    # ค้นหาข้อมูลจากฐานข้อมูลโดยใช้ username
    # cursor.execute("SELECT name FROM user WHERE username = %s", (username,))
    cursor.execute("SELECT user.name, user.surname, user.email, user.password, subject.code_subject, subject.id_subject, subject.name_subject, subject.year, subject.term FROM user JOIN subject ON user.username = subject.username WHERE user.username = %s", (username,))
    user_data = cursor.fetchall()

    if user_data:
        name = user_data[0][0]  # ดึงค่า "name" จากผลลัพธ์ที่ได้จากการ query
        st.write(f"Welcome back, {name}!")
        # สร้าง DataFrame จากข้อมูลที่ได้รับ
        df = pd.DataFrame(user_data, columns=["Name", "Surname", "Email", "Password", "Code Subject", "ID Subject", "Name Subject", "Year", "Term"])
        st.write(df)
    else:
        st.write("Please log in first!")

    # ปิดการเชื่อมต่อกับฐานข้อมูล
    cursor.close()
    conn.close()

# เรียกใช้ฟังก์ชันเพื่อแสดงโปรไฟล์ผู้ใช้
profile()
