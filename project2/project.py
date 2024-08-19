
import streamlit as st
import csv



def main():
    firstname = st.text_input("Firstname", value="", max_chars=None, key=None)
    lastname = st.text_input("Lastname", value="", max_chars=None, key=None)
    company = st.text_input("Company", value="", max_chars=None, key=None)
    phone = st.text_input("Phone", value="", max_chars=None, key=None)
    email = st.text_input("Email", value="", max_chars=None, key=None)
    
    with open('contacts.csv', 'w', newline='') as file:
        # firstname = "Nick"
        # lastname = "Hughes"
        # company = "Luvian Consulting"
        # phone = "0403 553977"
        # email = "nick@nickhughes.io"
        writer = csv.writer(file)
        field = ["firstname", "lastname", "company", "phone", "email"]
        
        writer.writerow(field)
        writer.writerow([firstname, lastname, company, phone, email])


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



