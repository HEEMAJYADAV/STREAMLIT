import streamlit as st
import mysql.connector
import pandas as pd

# Establish a database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kunnu@102",
    database="student13"  # Make sure this is the correct database name
)
mycursor = mydb.cursor()
# st.write("Connection Established")

def create_record():
    st.subheader("Create a Record")
    AttendanceID = st.text_input("Enter AttendanceId")
    StudentID = st.text_input("Enter the StudentId")
    Status = st.text_input("Enter the Status")
    StartDate = st.date_input("Enter the StartDate")
    EndDate = st.date_input("Enter the EndDate")

    if st.button("Create"):
        try:
            # Modify the SQL query and values to match your table and columns (attendance table)
            sql = "INSERT INTO attendance (AttendanceID, StudentID, Status, StartDate, EndDate) VALUES (%s, %s, %s, %s, %s)"
            val = (AttendanceID, StudentID, Status, StartDate, EndDate)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def read_records():
    st.subheader("Read Records")
    mycursor.execute("SELECT * FROM attendance")  # Modify to select from the attendance table
    result = mycursor.fetchall()
    if result:
        df = pd.DataFrame(result, columns=["AttendanceID", "StudentID", "Status", "StartDate", "EndDate"])
        st.dataframe(df)
    else:
        st.write("No records found.")

def update_record():
    st.subheader("Update a Record")
    AttendanceID = st.text_input("Enter AttendanceID of the record to update")
    new_status = st.text_input("Enter the new Status")

    if st.button("Update"):
        try:
            # Modify the SQL query to update the status of the specified record
            sql = "UPDATE attendance SET Status = %s WHERE AttendanceID = %s"
            val = (new_status, AttendanceID)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def delete_record():
    st.subheader("Delete a Record")
    AttendanceID = st.text_input("Enter AttendanceID of the record to delete")

    if st.button("Delete"):
        try:
            # Modify the SQL query to delete the record with the specified AttendanceID
            sql = "DELETE FROM attendance WHERE AttendanceID = %s"
            val = (AttendanceID,)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def main():
    st.title("Attendance")
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
