from typing import List

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

    # function to print list of objects
    def print_persons() -> None:
        print("--- List of persons ---")
        for person in Person.lst_persons:            
            print("id: ", person.id, " | name: ", person.name, " | email: ", person.email)
