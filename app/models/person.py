
from app.core.abc_interfaces import Person
from app.core.metaclasses import BaseModel


class PersonModel(Person, BaseModel):

    def __init__(self, name, age, email):
        BaseModel.__init__(self)
        self.name = name
        self.age = age
        self.email = email

    def display_details(self):
        raise NotImplementedError

    def to_dict(self):
        raise NotImplementedError

