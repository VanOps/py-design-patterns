#!/usr/bin/python3

from copy import deepcopy


# Prototype pattern is a creational pattern that allows cloning objects, even complex ones, without coupling to their
# specific classes. It is useful when the object creation is expensive or complex.
# It is useful when we want to create a new object from an existing object, and we want to keep the existing object
# unchanged.

# The Prototype class is the interface that defines the method to clone the object.
# The clone method is an abstract method that must be implemented by the concrete classes. This method does not always
# do only a copy of the object. It can make a deep copy, depending on the requirements, or make some changes
# to the object before returning it.
class Prototype:
    def clone(self): pass


# The ConcretePrototype class implements the Prototype interface and defines the method to clone the object.
class ConcretePrototype(Prototype):
    def __init__(self, attribute):
        self.attribute = attribute
        self.serial_number = 1000000000

    def clone(self):
        obj = deepcopy(self)
        obj.serial_number += 1
        return obj

    def show(self):
        print("Attribute: ", self.attribute)
        print("Serial number: ", self.serial_number)
        print("ID: ", id(self))


if __name__ == '__main__':
    prototype = ConcretePrototype("Original object")
    prototype.show()

    clone = prototype.clone()
    clone.show()
