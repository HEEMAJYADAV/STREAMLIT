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

def join_tables():
    st.title("Join Tables")
    
    # Let the user choose the tables to join
    table1_name = st.selectbox("Select the first table", ["Student", "attendance", "leaverecords"])
    table2_name = st.selectbox("Select the second table", ["Student", "attendance", "leaverecords"])

    if st.button("Join Tables"):
        try:
            # Modify the SQL query to join the selected tables based on StudentID
            sql = f"SELECT {table1_name}.*, {table2_name}.StartDate AS {table2_name}_StartDate, {table2_name}.EndDate AS {table2_name}_EndDate, {table2_name}.Status AS {table2_name}_Status FROM {table1_name} INNER JOIN {table2_name} ON {table1_name}.StudentID = {table2_name}.StudentID"
            
            mycursor.execute(sql)
            result = mycursor.fetchall()

            if result:
                columns = [desc[0] for desc in mycursor.description]
                df = pd.DataFrame(result, columns=columns)
                st.dataframe(df)
            else:
                st.write("No records found.")
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")

def main():
    join_tables()

if __name__ == "__main__":
    main()
