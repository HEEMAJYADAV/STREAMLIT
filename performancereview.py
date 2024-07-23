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
    mycursor.execute("SELECT * FROM performancereview")
    result = mycursor.fetchall()
    if result:
        df = pd.DataFrame(result, columns=["ReviewID", "StudentID", "ReviewDate", "Details"])
        st.dataframe(df)
    else:
        st.write("No records found.")

def create_record():
    st.subheader("Create a Record")
    ReviewID = st.text_input("Enter ReviewID")
    StudentID = st.text_input("Enter StudentID")
    ReviewDate = st.date_input("Enter ReviewDate")
    Details = st.text_area("Enter Details")

    if st.button("Create"):
        try:
            # Modify the SQL query and values to match your table and columns (performancereview table)
            sql = "INSERT INTO performancereview (ReviewID, StudentID, ReviewDate, Details) VALUES (%s, %s, %s, %s)"
            val = (ReviewID, StudentID, ReviewDate, Details)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Created Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def update_record():
    st.subheader("Update a Record")
    ReviewID = st.text_input("Enter ReviewID of the record to update")
    new_student_id = st.text_input("Enter the new StudentID")
    new_review_date = st.date_input("Enter the new ReviewDate")
    new_details = st.text_area("Enter the new Details")

    if st.button("Update"):
        try:
            # Modify the SQL query to update the record with the specified ReviewID
            sql = "UPDATE performancereview SET StudentID = %s, ReviewDate = %s, Details = %s WHERE ReviewID = %s"
            val = (new_student_id, new_review_date, new_details, ReviewID)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Updated Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def delete_record():
    st.subheader("Delete a Record")
    ReviewID = st.text_input("Enter ReviewID of the record to delete")

    if st.button("Delete"):
        try:
            # Modify the SQL query to delete the record with the specified ReviewID
            sql = "DELETE FROM performancereview WHERE ReviewID = %s"
            val = (ReviewID,)

            mycursor.execute(sql, val)
            mydb.commit()
            st.success("Record Deleted Successfully!!!")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def main():
    st.title("Performance Review Management")
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
