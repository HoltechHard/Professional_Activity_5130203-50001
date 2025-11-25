from typing import List, Optional

# python class person
class Person:

    lst_persons: List["Person"] = []

    # constructor
    def __init__(self, id:int, name: str, email: str) -> None:
        self.id = id
        self.name = name
        self.email = email
        Person.lst_persons.append(self)
    
    # definition of objects
    def __repr__(self) -> str:
        return(
            f"{self.__class__.__name__}("
            f"{self.name}, {self.email}"
            f")"
        )

    # function to search person object by id
    @staticmethod
    def find_person_by_id(id: int) -> Optional["Person"]:
        for person in Person.lst_persons:
            if person.id == id:
                return person
        return None
    
    # function to insert person
    @staticmethod
    def insert_person(id: int, name: str, email: str) -> "Person":
        # check if person already exists        
        if Person.find_person_by_id(id):
            raise ValueError(f"Person with ID {id} already exists!")
        return Person(id, name, email)

    # function to edit person
    @staticmethod
    def edit_person(id: int, new_name: str, new_email: str) -> bool:
        person = Person.find_person_by_id(id)
        if person:
            person.name = new_name
            person.email = new_email
            return True
        return False
    
    # function to delete person
    @staticmethod
    def delete_person(id: int) -> bool:
        person = Person.find_person_by_id(id)
        if person:
            Person.lst_persons.remove(person)
            return True
        return False

    # function to print list of objects
    @staticmethod
    def print_persons() -> None:
        print("--- List of persons ---")
        for person in Person.lst_persons:            
            print("id: ", person.id, " | name: ", person.name, " | email: ", person.email)
