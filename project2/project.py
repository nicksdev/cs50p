import sys
import os
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
    init_csv()
    contactid = init_id()
    input = sys.argv
    contact = get_contact(input)
    crud_call(input,contact,contactid)
    #print(contact.firstname)
    

    # test data: python project.py create Nick Hughes "My Company" 0403111999 nick@email.com
    # get values from prompt
    # generate id
    # write to csv



def crud_call(input,contact,contactid):

    if input[1] == "create":
        create_contact(contact,contactid)
    else:
        print("Unrecognised Input")

def create_contact(contact,contactid):
    print(contact.email)
    print(contactid)
    id = int(contactid) + 1
    with open('contacts.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, contact.firstname, contact.lastname, contact.company, contact.phone, contact.email])
    

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




if __name__ == "__main__":
    main()