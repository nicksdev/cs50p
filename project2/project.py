import sqlite3
import streamlit as st
from sqlite3 import Error


def main():
#    create_connection("contacts.db")
    conn = sqlite3.connect('work_contacts.db')

    # Initialise Database
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees 
                   (id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, company TEXT, position TEXT, email TEXT, phone REAL)''')
    conn.commit()






    if st.button("List"):
        st.info("Display List")

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



