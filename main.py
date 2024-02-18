import streamlit as st
from pages.login import login
from pages.about import show_about_page

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox("Go to", ["Home", "About"])

    if page == "Home":
        login()
    elif page == "About":
        show_about_page()

if __name__ == "__main__":
    main()

