#!/usr/bin/python3

# Factory pattern is a creational pattern that uses factory methods to create objects.


# Include and interface to obligate the classes to implement the method speak
class PetInterface:
    def speak(self): pass


# Every class that implements the PetInterface must implement the method speak
class Dog(PetInterface):
    def speak(self):
        print("Woof!")


class Cat(PetInterface):
    def speak(self):
        print("Meow!")


# Factory class that returns the object based on the type
class PetFactory:
    # Static method to create the object based on the type.
    # It is static because it does not need to access any instance variable of the class.
    # It is a utility method that does not need to refer to the class or instance.
    # @staticmethod is a decorator that defines a static method
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
