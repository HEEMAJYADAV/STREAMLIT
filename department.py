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
    mycursor.execute("SELECT * FROM department")
    result = mycursor.fetchall()
    if result:
        df = pd.DataFrame(result, columns=["DepartmentID", "DepartmentName", "Description", "StudentID"])
        st.dataframe(df)
    else:
        st.write("No records found.")

def create_record():
    st.subheader("Create a Record")
    DepartmentID = st.text_input("Enter DepartmentID")
    DepartmentName = st.text_input("Enter DepartmentName")
    Description = st.text_input("Enter Description")
    StudentID = st.text_input("Enter StudentID")

    if st.button("Create"):
        try:
            # Modify the SQL query and values to match your table and columns (department table)
            sql = "INSERT INTO department (DepartmentID, DepartmentName, Description, StudentID) VALUES (%s, %s, %s, %s)"
            val = (DepartmentID, DepartmentName, Description, StudentID)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def update_record():
    st.subheader("Update a Record")
    DepartmentID = st.text_input("Enter DepartmentID of the record to update")
    new_department_name = st.text_input("Enter the new DepartmentName")
    new_description = st.text_input("Enter the new Description")
    new_student_id = st.text_input("Enter the new StudentID")

    if st.button("Update"):
        try:
            # Modify the SQL query to update the record with the specified DepartmentID
            sql = "UPDATE department SET DepartmentName = %s, Description = %s, EmployeeID = %s WHERE DepartmentID = %s"
            val = (new_department_name, new_description, new_student_id, DepartmentID)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def delete_record():
    st.subheader("Delete a Record")
    DepartmentID = st.text_input("Enter DepartmentID of the record to delete")

    if st.button("Delete"):
        try:
            # Modify the SQL query to delete the record with the specified DepartmentID
            sql = "DELETE FROM department WHERE DepartmentID = %s"
            val = (DepartmentID,)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def main():
    st.title("Department")
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
