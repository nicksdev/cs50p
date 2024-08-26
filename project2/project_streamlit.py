
import streamlit as st
import csv



class Contact:
    def __init__(self, firstname, lastname, company, phone, email):
        #self.userid = userid
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.phone = phone
        self.email = email



def initid():
    if "userid" in globals():
        print("found")
        userid = userid + 1
        return userid
    else:
        print("notfound")
        
        userid = 1
        return userid



def main():


    

    contact = get_contact()
    if st.button('Create'):
        #print(userid)
        #print(contact.firstname, contact.lastname, contact.company, contact.phone, contact.email)
        create_contact(contact)
        


def get_contact():
    firstname = st.text_input("Firstname", value="", max_chars=None, key=None)
    lastname = st.text_input("Lastname", value="", max_chars=None, key=None)
    company = st.text_input("Company", value="", max_chars=None, key=None)
    phone = st.text_input("Phone", value="", max_chars=None, key=None)
    email = st.text_input("Email", value="", max_chars=None, key=None)
    contact = Contact(firstname, lastname, company, phone, email)
    return contact


def create_contact(contact):
    with open('contacts.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([initid(), contact.firstname, contact.lastname, contact.company, contact.phone, contact.email])
        



def read_contact():
    ...

def update_contact():
    ...

def delete_contact():
    ...






if __name__ == "__main__":
    main()



