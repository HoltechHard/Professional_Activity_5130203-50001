from models import Person

def menu():
    print("""
        ========= PERSON MANAGER =========
        1. Insert person
        2. Edit person
        3. Delete person
        4. List persons
        5. Exit
        ==================================
        """)

# show insert option
def insert_person_view():
    id = int(input("Enter ID: "))
    name = input("Enter name: ")
    email = input("Enter email: ")

    try:
        Person.insert_person(id, name, email)
        print("Person inserted successfully!\n")
    except ValueError as e:
        print(e)

# show edit option
def edit_person_view():
    id = int(input("Enter ID to edit: "))
    name = input("Enter NEW name: ")
    email = input("Enter NEW email: ")

    if Person.edit_person(id, name, email):
        print("Person updated successfully!\n")
    else:
        print("Person not found.\n")

# show delete option
def delete_person_view():
    id = int(input("Enter ID to delete: "))

    if Person.delete_person(id):
        print("Person deleted successfully!\n")
    else:
        print("Person not found.\n")


def main():
    while True:
        menu()
        option = input("Choose an option: ")

        if option == "1":
            insert_person_view()
        elif option == "2":
            edit_person_view()
        elif option == "3":
            delete_person_view()
        elif option == "4":
            Person.print_persons()
        elif option == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
