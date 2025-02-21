# We are using dictionary to store the contact details

# empty dictionary
contact_book = {}

# add the contact details
def add_contact():
    name = input("Enter the Name: ")
    phone = input("Enter the Phone Number: ")
    contact_book[name] = phone
    print("Contact details added successfully in contact book")

# view the contact details
def view_contact():
    if not contact_book:
        print("Contact book is empty")
    else:
        print("Contact details are: ")
        for name, phone in contact_book.items():
            print(f"Name: {name}, Phone Number: {phone}")

# search the contact details
def search_contact():
    name =  input("Enter the name to search: ")
    if name in contact_book:
        print(f"Name: {name}, Phone Number: {contact_book[name]}")
    else:
        print("This name and Phone number is not available in contact book")

# Main function
def main():
    while True:
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. Exit")

        choice = int(input('Enter your choice:'))

        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contact()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            print("Thankyou! Have a nice day")
            break
        else:
            print("Invalid Command")

if __name__ == "__main__":
    main()