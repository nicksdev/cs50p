import sqlite3
from sqlite3 import Error


def main():
    create_connection("contacts.db")




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



