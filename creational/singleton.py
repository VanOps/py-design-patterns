#!/usr/bin/python3

# Singleton pattern is a creational pattern that ensures that a class has only one instance and provides a global point
# of access to that instance. It violates the Single Responsibility Principle because it controls the creation and
# access to the instance.

# The Singleton class is the class that has only one instance.
# The __instance attribute is a class attribute that stores the instance of the class.
# The __init__ method is the constructor that creates the instance of the class.
# The __new__ method is a static method that returns the instance of the class. It is called before the __init__ method.

class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

if __name__ == '__main__':
    singleton1 = Singleton()
    singleton1.set_value(1)
    print(singleton1.get_value())

    singleton2 = Singleton()
    print(singleton2.get_value())

    print(singleton1 == singleton2)
    print(singleton1 is singleton2)
    print(id(singleton1), id(singleton2))
    print(singleton1.__dict__)
    print(singleton2.__dict__)
    print(singleton1.__class__.__dict__)
    print(singleton2.__class__.__dict__)
    print(Singleton.__dict__)
    print(singleton1.__class__.__dict__ is singleton2.__class__.__dict__)
    print(singleton1.__class__.__dict__ is Singleton.__dict__)