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
    mycursor.execute("SELECT * FROM leaverecords")
    result = mycursor.fetchall()
    if result:
        df = pd.DataFrame(result, columns=["LeaveID", "StudentID", "StartDate", "EndDate", "Status"])
        st.dataframe(df)
    else:
        st.write("No records found.")

def create_record():
    st.subheader("Create a Record")
    LeaveID = st.text_input("Enter LeaveID")
    StudentID = st.text_input("Enter StudentID")
    StartDate = st.date_input("Enter StartDate")
    EndDate = st.date_input("Enter EndDate")
    Status = st.text_input("Enter Status")

    if st.button("Create"):
        try:
            # Modify the SQL query and values to match your table and columns (leave table)
            sql = "INSERT INTO leaverecords (LeaveID, StudentID, StartDate, EndDate, Status) VALUES (%s, %s, %s, %s, %s)"
            val = (LeaveID, StudentID, StartDate, EndDate, Status)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def update_record():
    st.subheader("Update a Record")
    LeaveID = st.text_input("Enter LeaveID of the record to update")
    new_student_id = st.text_input("Enter the new StudentID")
    new_start_date = st.date_input("Enter the new StartDate")
    new_end_date = st.date_input("Enter the new EndDate")
    new_status = st.text_input("Enter the new Status")

    if st.button("Update"):
        try:
            # Modify the SQL query to update the record with the specified LeaveID
            sql = "UPDATE leaverecords SET StudentID = %s, StartDate = %s, EndDate = %s, Status = %s WHERE LeaveID = %s"
            val = (new_student_id, new_start_date, new_end_date, new_status, LeaveID)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def delete_record():
    st.subheader("Delete a Record")
    LeaveID = st.text_input("Enter LeaveID of the record to delete")

    if st.button("Delete"):
        try:
            # Modify the SQL query to delete the record with the specified LeaveID
            sql = "DELETE FROM leave WHERE LeaveID = %s"
            val = (LeaveID,)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def main():
    st.title("Leave Management")
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
