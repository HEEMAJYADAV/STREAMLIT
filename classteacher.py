import streamlit as st
import mysql.connector
import pandas as pd

# Establish a database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kunnu@102",
    database="student13"
)
mycursor = mydb.cursor()

def read_records():
    st.subheader("Read Records")
    mycursor.execute("SELECT * FROM ClassTeacher")
    result = mycursor.fetchall()
    if result:
        df = pd.DataFrame(result, columns=["ClassTeacherID", "StudentID", "Email", "FirstName", "LastName"])
        st.dataframe(df)
    else:
        st.write("No records found.")

def create_record():
    st.subheader("Create a Record")
    ClassTeacherID = st.text_input("Enter ClassTeacherID")
    StudentID = st.text_input("Enter StudentID")
    Email = st.text_input("Enter Email")
    FirstName = st.text_input("Enter First Name")
    LastName = st.text_input("Enter Last Name")

    if st.button("Create"):
        try:
            # Modify the SQL query and values to match your table and columns (ClassTeacher table)
            sql = "INSERT INTO ClassTeacher (ClassTeacherID, StudentID, Email, FirstName, LastName) VALUES (%s, %s, %s, %s, %s)"
            val = (ClassTeacherID, StudentID, Email, FirstName, LastName)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def update_record():
    st.subheader("Update a Record")
    StudentID = st.text_input("Enter StudentID of the record to update")
    new_ClassTeacher_id = st.text_input("Enter the new ClassTeacherID")
    new_email = st.text_input("Enter the new Email")
    new_first_name = st.text_input("Enter the new First Name")
    new_last_name = st.text_input("Enter the new Last Name")

    if st.button("Update"):
        try:
            # Modify the SQL query to update the record with the specified StudentID
            sql = "UPDATE ClassTeacher SET ClassTeacherID = %s, Email = %s, FirstName = %s, LastName = %s WHERE StudentID = %s"
            val = (new_ClassTeacher_id, new_email, new_first_name, new_last_name, StudentID)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def delete_record():
    st.subheader("Delete a Record")
    ClassTeacherID = st.text_input("Enter ClassTeacherID of the record to delete")

    if st.button("Delete"):
        try:
            # Modify the SQL query to delete the record with the specified StudentID
            sql = "DELETE FROM ClassTeacher WHERE ClassTeacherID = %s"
            val = (ClassTeacherID,)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def main():
    st.title("ClassTeacher")
    option = st.sidebar.selectbox("Select an operation", ("Create", "Read", "Update", "Delete"))

    if option == "Create":
        create_record()
    elif option == "Read":
        read_records()
    elif option == "Update":
        update_record()
    elif option == "Delete":
        delete_record()

if __name__ == "__main__":
    main()
