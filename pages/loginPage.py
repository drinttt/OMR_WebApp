import streamlit as st
import mysql.connector
import streamlit_authenticator as stauth

from passlib.hash import sha256_crypt

# from pages.register import register
from pages import register


# st.set_page_config(layout="wide")


def login():
    # st.set_page_config(layout="wide")

    # สร้าง session_state สำหรับเก็บข้อมูลของผู้ใช้
    if 'username' not in st.session_state:
        st.session_state.username = ''

    def func(username,password):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="omr"
            )
            cursor = conn.cursor()

            
            cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password))
            user = cursor.fetchone()

            # ปิดการเชื่อมต่อกับฐานข้อมูล
            cursor.close()
            conn.close()

            if user:
                return username  # รีเทิร์นชื่อผู้ใช้ที่พบ
            
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None
        
        return None

        # cursor.execute("SELECT * FROM account WHERE username = %s", (username,))
        # user = cursor.fetchone()

        # st.session_state.username = user.username
        # st.session_state.password = user.password
    
    with open('css/login.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
    # st.set_page_config(layout="wide")

    col1, col2 = st.columns(2)

    with col1:
        # st.image("https://static.streamlit.io/examples/cat.jpg")
        st.image("img/logo.png")

    with col2:
        st.markdown("\n\n\n")
        st.header("Sign in")
        st.markdown("\n\n")

        placeholder = st.empty()
        # actual_email = "email"
        # actual_password = "password"

        with placeholder.form("login"):
            # st.markdown("#### Enter your credentials")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            st.markdown("\n")

            # submit = st.form_submit_button("SIGN IN")
            # st.write("Don't have an account [Sign up](/register)")
            # st.form_submit_button("SIGN IN", on_click=func(username,password))


            if st.form_submit_button("Submit"):
                username = func(username, password)

                if username:
                    print(f"Login successful! Welcome, {username}")
                    st.write(f"Hello {username}")
                    st.session_state.username = username
                    new_page_url = f"/profile?username={username}"
                    st.write(f"[Go to Profile Page]({new_page_url})")
                else:
                    print("Login failed. Invalid username or password.")
                # conn = mysql.connector.connect(
                #     host="localhost",
                #     user="root",
                #     password="",
                #     database="omr_new"
                # )
                # cursor = conn.cursor()

                # cursor.execute("SELECT * FROM account WHERE username = %s", (username,))
                # user = cursor.fetchone()

                # if user:  # ถ้าพบข้อมูลผู้ใช้
                #     if sha256_crypt.verify(password, user[2]):  # ตรวจสอบรหัสผ่าน
                #         st.session_state.username = user[1]  # กำหนดชื่อผู้ใช้ใน session_state
                #         st.session_state.useremail = user[3]  # กำหนดอีเมล์ผู้ใช้ใน session_state
                #         st.success('Login successful!')
                #     else:
                #         st.warning('Incorrect password')
                # else:
                #     st.warning('User not found')

                # cursor.close()
                # conn.close()


            # st.markdown("Don't have an account? [Sign up](/register)", unsafe_allow_html=True)
            st.markdown("Don't have an account? <a href='/register' target='_self'>Sign up</a>", unsafe_allow_html=True)
            # st.markdown("Don't have an account? <a href='/register'>Sign up</a>", unsafe_allow_html=True)



            # if st.session_state:
            #     st.write('Logged in as:', st.session_state.username)
            
login()