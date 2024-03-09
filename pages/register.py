import streamlit as st
import mysql.connector
import random
import string
from pages import loginPage


def create_user(username, password):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="omr"
    )
    cursor = conn.cursor()

    id_user = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

    # เพิ่มผู้ใช้ลงในตารางของ MySQL
    cursor.execute("INSERT INTO user (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()

    # ปิดการเชื่อมต่อ
    cursor.close()
    conn.close()

def register():
    st.set_page_config(layout="wide")
    with open('css/login.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
    col1, col2 = st.columns(2)

    with col1:
        # st.image("https://static.streamlit.io/examples/cat.jpg")
        st.image("img/logo.png")

    with col2:
        st.markdown("\n\n\n")
        st.header("Register")
        st.markdown("\n\n")

        placeholder = st.empty()
        # actual_email = "email"
        # actual_password = "password"

        with placeholder.form("register"):
            # st.markdown("#### Enter your credentials")
            username = st.text_input("Username")
            password1 = st.text_input("Password", type="password", key="password1")
            password2 = st.text_input("Confirm Password", type="password", key="password2")

            st.markdown("\n")


            if st.form_submit_button("Sign Up"):
                 # เงื่อนไขตรวจสอบ username และ password
                if not username:
                    st.error("Please enter a username.")
                elif not password1 or not password2:
                    st.error("Please enter both password and confirm password.")
                elif password1 != password2:
                    st.error("Password and Confirm Password do not match.")
                else:
                    create_user(username, password1)

                    # แสดงข้อความ "สำเร็จ"
                    st.success("User created successfully!")

                    # ลิงก์ไปยังหน้า login
                    # st.write("Don't have an account [Sign up](/login)")

            # st.markdown("PLease login [Sign up](/loginPage)")
            st.markdown("Please login <a href='/main' target='_self'>Sign up</a>", unsafe_allow_html=True)

            
register()