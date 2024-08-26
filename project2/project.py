import sys
import csv

class Contact:
    def __init__(self, firstname, lastname, company, phone, email):
        #self.userid = userid
        self.firstname = firstname
        self.lastname = lastname
        self.company = company
        self.phone = phone
        self.email = email


def main():
    input = sys.argv
    contact = get_contact(input)
    crud_call(input,contact)
    #print(contact.firstname)
    

    # test data: python project.py create Nick Hughes "My Company" 0403111999 nick@email.com
    # get values from prompt
    # generate id
    # write to csv



# def create_contact(contact):
#     with open('contacts.csv', 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow([initid(), contact.firstname, contact.lastname, contact.company, contact.phone, contact.email])

def crud_call(input,contact):

    if input[1] == "create":
        create_contact(contact)
    else:
        print("Unrecognised Input")

def create_contact(contact):
    print(contact.email)
    with open('contacts.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([contact.firstname, contact.lastname, contact.company, contact.phone, contact.email])
    

def read_contact():
    ...

def update_contact():
    ...

def delete_contact():
    ...

def get_contact(input):
    firstname = input[2]
    lastname = input[3]
    company = input[4]
    phone = input[5]
    email = input[6]
    contact = Contact(firstname, lastname, company, phone, email)
    return contact

if __name__ == "__main__":
    main()