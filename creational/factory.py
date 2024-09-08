#!/usr/bin/python
# Factory pattern is a creational pattern that uses factory methods to create objects.


# Include and interface to obligate the classes to implement the method speak
class PetInterface:
    def speak(self): pass


# Every class that implements the PetInterface must implement the method speak
class Dog(PetInterface):
    def __init__(self):
        self.name = "Dog"

    def speak(self):
        print("Woof!")


class Cat(PetInterface):
    def __init__(self):
        self.name = "Cat"

    def speak(self):
        print("Meow!")


# Factory class that returns the object based on the type
class PetFactory:
    @staticmethod
    def get_pet(type):
        if type == "dog":
            return Dog()
        if type == "cat":
            return Cat()
        else:
            assert 0, "Invalid pet type:" + type


if __name__ == '__main__':
    pet = PetFactory.get_pet("dog")
    pet.speak()

    pet = PetFactory.get_pet("cat")
    pet.speak()

    pet = PetFactory.get_pet("parrot")
    pet.speak()