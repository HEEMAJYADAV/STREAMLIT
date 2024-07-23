import streamlit as st
import student
import document
import attendance
import classteacher
import department
import leaverecord
import performancereview# Import the manager script
import join

def main():
    st.title("Student Management System")
    page = st.sidebar.selectbox("Select a Page", ["Home", "Student", "Document", "Attendance", "ClassTeacher","Department","Leave","Performance","Join"])

    if page == "Home":
        st.write("Welcome to the CRUD App. Select a page from the sidebar to get started.")
    elif page == "Student":
        student.main()
    elif page == "Document":
        document.main()
    elif page == "Attendance":
        attendance.main()
    elif page == "ClassTeacher":
        classteacher.main() 
    elif page == "Department":
        department.main() 
    elif page == "Leave":
        leaverecord.main() 
    elif page == "Performance":
        performancereview.main() 
    elif page == "Join":
        join.main() 
    # Call the main function from the manager script

if __name__ == "__main__":
    main()


