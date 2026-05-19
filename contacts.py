import json
import os

def load_contacts():
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as file:
            return json.load(file)
    return []

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(name:str, contact_num : int, email:str):
    contacts = load_contacts()
    name = input("Enter your name: ").strip()
    if name == " ":
        print("your name cannot be null try again.")
    else:
        contact_num = input("Enter your contact number: ").strip()
        if contact_num == " ":
            print("your contact cannot be null try again.")
        elif not contact_num.isdigit():
            print("Contact Number can only be numbers.")
        else:
            email = input("Enter your email address = ").strip()
            if email == " ":
                print("your email cannot be null try again.")
        
        for contact in contacts:
            if contact["contact_num"] == contact:
                print(f'this contact already exists!')
            return

    new_contact = {
        "name" : name,
        "contact" : contact_num,
        "email"  : email
    }
    contacts.append(new_contact)

    save_contacts(contacts)
    
    print("Success!! Your contact has been saved")
def add_contact():
    contacts = load_contacts()

    print("\n--- Add New Contact ---")

    # get name
    while True:
        name = input("Enter your name: ").strip()
        if name == "":
            print("Name cannot be empty, try again.")
        else:
            break

    # get phone
    while True:
        contact_num = input("Enter your contact number: ").strip()
        if contact_num == "":
            print("Contact cannot be empty, try again.")
        elif not contact_num.isdigit():
            print("Contact number can only be numbers.")
        else:
            break

    # check duplicate
    for contact in contacts:
        if contact["contact"] == contact_num:
            print("This contact already exists!")
            return add_contact()

    # get email
    while True:
        email = input("Enter your email address: ").strip()
        if email == "":
            print("Email cannot be empty, try again.")
        elif "@" not in email:
            print("Please enter a valid email.")
        else:
            break

    # save
    new_contact = {
        "name": name,
        "contact": contact_num,
        "email": email
    }
    contacts.append(new_contact)
    save_contacts(contacts)

    print("Success!! Your contact has been saved.")

def view_contact():
    contacts = load_contacts()
    if contacts == []:
        print("The list is empty!")
        return
    else:
        print("___Your_Contacts___")
        for i, contact in enumerate(contacts, 1):
            print(f'{i}, Name: {contact["name"]}')
            print(f'Contact: {contact["contact"]}')
            print(f'Email: {contact["email"]}')
            print('-----------')

def search_contact(contacts):
    searchMethod = input("Choose an option\n 1. Search by name\n 2. Search by contact\n 3. Search by Email\n >" )
    if searchMethod == "1":
        searchName = input("Enter the name: ")
        found = False
        for i, contact in enumerate(contacts, 1):
            if searchName.lower() == contact["name"].lower():
                print(f'{i}\n Found: {contact["name"]}\n {contact["contact"]}\n {contact["email"]}')
                found = True
                return contact

        if found != True:
            print(f"Your name: {searchName} was not found")
    elif searchMethod == "2":
        searchContact = input("Enter the contact: ")
        found = False
        for i, contact in enumerate(contacts, 1):
            if searchContact == contact["contact"]:
                print(f'{i}\n Found: {contact["name"]}\n {contact["contact"]}\n {contact["email"]}')
                found = True
                return contact

        if found != True:
            print(f"Your contact: {searchContact} was not found")

    elif searchMethod == "3":
        searchEmail = input("Enter the email: ")
        found = False
        for i, contact in enumerate(contacts, 1):
            if searchEmail.lower() == contact["email"].lower():
                print(f'{i}\n Found: {contact["name"]}\n {contact["contact"]}\n {contact["email"]}')
                found = True
                return contact

        if found != True:
            print(f"Your email: {searchEmail} was not found")
    
def update_contact():
    contacts = load_contacts()
    updateContacts = search_contact(contacts)
    if updateContacts:
        print("Write the new data or Press enter to keep it unchanged.")
        new_name = input(f"Enter the new name {updateContacts['name']}: ")
        if new_name != "":
            updateContacts["name"] = new_name
        while True:
            new_contact = input(f"Enter the new contact {updateContacts['name']}: ")
            if new_contact.isdigit():
                updateContacts["contact"] = new_contact
                break
            elif new_contact == "":
                break
            else:
                print("Please Enter a valid input.")
                pass

        new_email = input(f"Enter the new email {updateContacts['name']}: ")
        if "@" not in new_email and new_email != "":
            print("Please Enter a Valid Email.")
        elif new_email != "" and "@" in new_email:
            updateContacts["email"] = new_email

        save_contacts(contacts)

def delete_contact():
    contacts = load_contacts()
    deleteContact = search_contact(contacts)
    if deleteContact:
        choice = input("Are you sure you want to delete this contact? Y/N").lower()
        if choice == "y":
            contacts.remove(deleteContact)
            save_contacts(contacts)
            print("Your contact has been deleted.")
        else:
            print("Deletion Cancelled!")

def main_menu():
    print("<----------MAIN_MENU---------->")
    while True:
        choice = input("<-----CHOOSE AN OPTION----->\n 1. ADD CONTACTS\n 2. VIEW CONTACTS\n 3. SEARCH CONTACTS\n 4. UPDATE CONTACTS\n 5. DELETE CONTACTS\n >"  )
        if choice == "1":
            add_contact()
            break
        elif choice == "2":
            view_contact()
            break
        elif choice == "3":
            search_contact
            break
        elif choice == "4":
            update_contact()
            break
        elif choice == "5":
            delete_contact()
            break
        else:
            print("Enter a valid input.")
            pass
main_menu()


            

                
            




    