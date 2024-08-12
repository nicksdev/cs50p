import sqlite3
import streamlit as st
from sqlite3 import Error


def main():
#    create_connection("contacts.db")
    conn = sqlite3.connect('work_contacts.db')

    # Initialise Database
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS contacts 
                   (id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, company TEXT, position TEXT, email TEXT, phone REAL)''')
    conn.commit()




    if st.button("Add Test Data"):
        cursor.execute("INSERT INTO contacts (firstname, lastname, company, position, email, phone) VALUES (?, ?, ?, ?, ?, ?)", ('testfirst', 'testlast', 'testcompany', 'test CEO', 'test@test.com', '0403 123456)'))
        conn.commit()
 
    if st.button("List"):
        cursor.execute("SELECT * FROM contacts")
        rows = cursor.fetchall()
        for row in rows:
        #print(row)
            st.info(row)

    if st.button("Create"):
        st.info("Create Record")

    if st.button("Read"):
        st.info("Read Record")

    if st.button("Update"):
        st.info("Update Record")

    if st.button("Delete"):
        st.info("Delete Record")

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def create_contact():
    ...

def read_contact():
    ...

def update_contact():
    ...

def delete_contact():
    ...






if __name__ == "__main__":
    main()



