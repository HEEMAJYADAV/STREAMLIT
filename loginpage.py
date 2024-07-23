import streamlit as st
import mysql.connector
import pandas as pd
import admin

# Establish a database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kunnu@102",
    database="student13"
)
mycursor = mydb.cursor()

def admin_page():
    admin.main()
    

def employee_page():
    st.write("Welcome to the Employee Page")

def main():
    st.markdown("""
        <h1 style='text-align: center;'>WELCOME TO EMPLOYEE MANAGEMENT SYSTEM</h1>
    """, unsafe_allow_html=True)

    # Center the buttons
    button_container = st.container()
    with button_container:
        if st.button("ADMIN"):
            admin_page()
        if st.button("EMPLOYEE"):
            employee_page()

if __name__ == "__main__":
    main()


