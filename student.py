import streamlit as st
import mysql.connector
import pandas as pd

# Establish a connection to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kunnu@102",
    database="student13"
)
mycursor = mydb.cursor()

# Create triggers
triggers_sql = """
-- Create a table to log changes
CREATE TABLE IF NOT EXISTS Student_Log (
    LogID INT AUTO_INCREMENT PRIMARY KEY,
    Action VARCHAR(10),
    StudentID INT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    Fees DECIMAL(10,2),
    Email VARCHAR(255),
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a trigger for INSERT operation
DELIMITER //
CREATE TRIGGER after_student_insert
AFTER INSERT ON Student
FOR EACH ROW
BEGIN
    INSERT INTO Student_Log (Action, StudentID, FirstName, LastName, Fees, Email)
    VALUES ('INSERT', NEW.StudentID, NEW.firstname, NEW.lastname, NEW.Fees, NEW.email);
END;
//

-- Create a trigger for UPDATE operation
DELIMITER //
CREATE TRIGGER after_student_update
AFTER UPDATE ON Student
FOR EACH ROW
BEGIN
    INSERT INTO Student_Log (Action, StudentID, FirstName, LastName, Fees, Email)
    VALUES ('UPDATE', NEW.StudentID, NEW.firstname, NEW.lastname, NEW.Fees, NEW.email);
END;
//

-- Create a trigger for DELETE operation
DELIMITER //
CREATE TRIGGER after_student_delete
AFTER DELETE ON Student
FOR EACH ROW
BEGIN
    INSERT INTO Student_Log (Action, StudentID, FirstName, LastName, Fees, Email)
    VALUES ('DELETE', OLD.StudentID, OLD.firstname, OLD.lastname, OLD.Fees, OLD.email);
END;
//
DELIMITER ;
"""

mycursor.execute(triggers_sql)
mydb.commit()

def create_record():
    st.subheader("Create a Record")
    StudentID = st.text_input("Enter Student ID")
    firstname = st.text_input("Enter the First Name")
    lastname = st.text_input("Enter the Last Name")
    Fees = st.text_input("Enter the Fees")
    email = st.text_input("Enter the Email")
    
    if st.button("Create"):
        try:
            sql = "INSERT INTO Student (StudentID, firstname, lastname, Fees, email) VALUES (%s, %s, %s, %s, %s)"
            val = (StudentID, firstname, lastname, Fees, email)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")
    else:
        st.warning("Record not created")

def read_records():
    st.subheader("Read Records")
    mycursor.execute("SELECT * FROM Student")
    result = mycursor.fetchall()
    if result:
        df = pd.DataFrame(result, columns=["StudentID", "FirstName", "LastName", "Fees", "Email"])
        st.dataframe(df)
    else:
        st.write("No records found.")

    mycursor.execute("SELECT count(StudentID) FROM Student")
    result_count = mycursor.fetchone()
    count = result_count[0] if result_count else 0
    st.subheader(f"Count the number of Student: {count}")

    student_id = st.text_input("Enter Student ID to search")

    if student_id:
        sql = "SELECT * FROM Student WHERE StudentID = %s"
        val = (student_id,)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()

        if result:
            df = pd.DataFrame(result, columns=["StudentID", "FirstName", "LastName", "Fees", "Email"])
            st.dataframe(df)
        else:
            st.write("No records found.")

def update_record():
    st.subheader("Update a Record")
    StudentID = st.text_input("Enter Student ID")
    new_firstname = st.text_input("Enter the New First Name")
    new_lastname = st.text_input("Enter the New Last Name")
    new_Fees = st.text_input("Enter the New Fees")
    new_email = st.text_input("Enter the New Email")
    
    if st.button("Update"):
        try:
            sql = "UPDATE Student SET firstname=%s, lastname=%s, Fees=%s, email=%s WHERE StudentID=%s"
            val = (new_firstname, new_lastname, new_Fees, new_email, StudentID)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def delete_record():
    st.subheader("Delete a Record")
    StudentID = st.text_input("Enter Student ID to delete")
    
    if st.button("Delete"):
        try:
            sql = "DELETE FROM Student WHERE StudentID=%s"
            val = (StudentID,)
            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def main():
    st.title("Student")
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
