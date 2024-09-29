#!/usr/bin/python3

# Borg pattern is a creational pattern that allows sharing the state of the objects between them. It is similar to the
# Singleton pattern, but it allows creating multiple instances of the class that share the same state. It is useful when
# we want to share the state of the objects between them, but we want to keep the object creation independent.
# It violates the Single Responsibility Principle because it controls the creation and access to the instance.

# The Borg class is the class that has the shared state.
# The __shared_state attribute is a class attribute that stores the shared state of the objects.
# The __init__ method is the constructor that initializes the object.
# The __new__ method is a static method that returns the instance of the class. It is called before the __init__ method.
class Borg:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj

    def __init__(self):
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value


if __name__ == '__main__':
    borg1 = Borg()
    borg1.set_value(1)
    print(borg1.get_value())

    borg2 = Borg()
    print(borg2.get_value())

    print(borg1 == borg2)
    print(borg1 is borg2)
    print(id(borg1), id(borg2))
    print(borg1.__dict__)
    print(borg2.__dict__)
    print(borg1.__class__.__dict__)
    print(borg2.__class__.__dict__)
    print(Borg.__dict__)
    print(borg1.__class__.__dict__ is borg2.__class__.__dict__)
    print(borg1.__class__.__dict__ is Borg.__dict__)