from models import Person

def generate_person():
    # create the objects
    p1 = Person(1, "Holger", "holtech94@gmail.com")
    p2 = Person(2, "Luis", "luis@gmail.com")
    p3 = Person(3, "Vasilisa", "vasilisa@gmail.com")

def main():
    # function to insert persons
    generate_person()    

    # print the list of contacts
    Person.print_persons()

if __name__ == "__main__":
    main()

