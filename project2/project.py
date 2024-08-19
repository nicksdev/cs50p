#import sqlite3
import streamlit as st
import csv
#from sqlite3 import Error


def main():
    with open('contacts.csv', 'w', newline='') as file:
        firstname = "Nick"
        lastname = "Hughes"
        company = "Luvian Consulting"
        phone = "0403 553977"
        email = "nick@nickhughes.io"
        writer = csv.writer(file)
        field = ["firstname", "lastname", "company", "phone", "email"]
        
        writer.writerow(field)
        writer.writerow([firstname, lastname, company, phone, email])

#    create_connection("contacts.db")




# def create_connection(path):
#     connection = None
#     try:
#         connection = sqlite3.connect(path)
#         print("Connection to SQLite DB successful")
#     except Error as e:
#         print(f"The error '{e}' occurred")

#     return connection

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



