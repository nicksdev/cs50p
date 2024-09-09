import sys
import os
import csv
import pandas as pd



class Contact:
    def __init__(self, firstname, lastname, company, phone, email):
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.phone = phone
        self.email = email


def main():
    init_csv()
    contactid = init_id()
    input = sys.argv
    contact = get_contact(input)
    crud_call(input,contact,contactid)
    

    # test data: python project.py create Nick Hughes "My Company" 0403111999 nick@email.com
    # get values from prompt
    # generate id
    # Create Contact
    # Display Contact
    # Update Contact
    # Delete Contact



def crud_call(input,contact,contactid):

    if input[1] == "create":
        create_contact(contact,contactid)
    elif input[1] == "delete":
        delete_contact(contact.email)
    elif input[1] == "update":
        update_contact(contact)
    elif input[1] == "read":
        read_contact(contact)

    else:
        print("Unrecognised CRUD Operation")

def create_contact(contact,contactid):
    if duplicate_check(contact.email) == True:
        return
    id = int(contactid) + 1
    with open('contacts.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, contact.firstname, contact.lastname, contact.company, str(contact.phone), contact.email])
    

def read_contact():
    ...

def update_contact(contact):
    if duplicate_check(contact.email) == False:
        print("Contact not found")
    else:
        df = pd.read_csv('contacts.csv', delimiter=',', dtype = str)
        df.loc[df['Email'] == contact.email, ['Firstname', 'Lastname', 'Company', 'Phone']] = contact.firstname, contact.lastname, contact.company, str(contact.phone)
        df.to_csv('contacts.csv', index=False)

            
def delete_contact(email):
    if duplicate_check(email) == False:
        print("Contact not found")
    else:
        df = pd.read_csv('contacts.csv', delimiter=',')
        df = df.loc[df['Email'] != email]
        df.to_csv('contacts.csv', index=False)
        print("Contact Deleted")

def get_contact(input):
    firstname = input[2]
    lastname = input[3]
    company = input[4]
    phone = input[5]
    email = input[6]
    contact = Contact(firstname, lastname, company, phone, email)
    return contact

def init_id():
    try:   
        z = open("contacts.csv", "r")
        last_line = z.readlines()[-1]
        obj = last_line.split(",")
        z.close()
        return int(obj[0])
    except IndexError:
        return 0
    except ValueError:
        return 0

def init_csv():
    if os.path.isfile("contacts.csv") == False:
        print("NOT FOUND")
        file = open("contacts.csv", "w")
        writer = csv.writer(file)
        writer.writerow(["ID", "Firstname", "Lastname", "Company", "Phone", "Email"])
    else:
        with open('contacts.csv', 'r') as file:
            file = file.readlines()
            if len(file) < 1:
                w_file = open("contacts.csv", "w")
                writer = csv.writer(w_file)
                writer.writerow(["ID", "Firstname", "Lastname", "Company", "Phone", "Email"])

def duplicate_check(email):
    #print("Checking if email exists: " + email)
    with open('contacts.csv', 'r') as file:
        for row in file:
            data = row.strip().split(',')
            #print(data[5])
            if email == data[5]:
                #print("Email Exists")
                return True
        #print("Email Not Found")
        return False



if __name__ == "__main__":
    main()