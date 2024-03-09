import streamlit as st
import mysql.connector
import pandas as pd
# from streamlit_option_menu import option_menu

from pages.loginPage import login
# from pages.aboutPage import about
from pages.register import register
from pages.profile import profile

# from pages import home
# from pages import loginPage
# from pages import register
# from pages import aboutPage
# from pages import profile

# st.set_page_config(layout="wide")


# connection db
# connection = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='omr'
# )

# cursor = connection.cursor()

# cursor.execute("Select * from account")
# data = cursor.fetchall()



# st.title("Yo man It's all account")

# df = pd.DataFrame(data, columns=cursor.column_names)
# st.dataframe(df)

def main():
    st.set_page_config(layout="wide")
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Login", "About", "Register", "Profile"])

    if page == "Login":
        login()
    # if page == "About":
    #     about()
    if page == "Register":
        register()
    if page == "Profile":
        profile()

if __name__ == "__main__":
    main()



# class MultiApp:
#     def __init__(self):
#         self.apps = []

#     def add_app(self, title, func):
#         self.apps.append({
#             "title": title,
#             "function": func
#         })
    
#     def run():
#         st.set_page_config(layout="wide")
#         st.sidebar.title("Navigation")
#         app = st.sidebar.selectbox("Go to", ["Home", "Login", "Register"])
            
#         if app == "Home":
#             home.app()
#         if app == "Login":
#             loginPage.app()
#         if app == "Register":
#             register.app()
#         if app == 'About':
#             aboutPage.app()    
             
          
             
#     run()

