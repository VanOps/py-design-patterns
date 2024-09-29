#!/usr/bin/python3

# Facade pattern is a structural pattern that provides a simplified interface to a complex system of classes,
# library, or framework. It is useful when we want to provide a simple interface to a complex subsystem.
# It hides the complexity of the subsystem and provides an interface to the client to access the system.

# The Facade class is the class that provides a simple interface to the complex subsystem.
# The __init__ method is the constructor that initializes the subsystem objects.
# The operation method is the method that provides a simple interface to the complex subsystem.
class Facade:
    def __init__(self):
        self.subsystem1 = Subsystem1()
        self.subsystem2 = Subsystem2()
        self.subsystem3 = Subsystem3()

    def operation(self):
        self.subsystem1.operation1()
        self.subsystem2.operation2()
        self.subsystem3.operation3()

    def operation1(self):
        self.subsystem1.operation1()


# The Subsystem1 class is a class of the complex subsystem.
# The operation1 method is a method of the complex subsystem.
class Subsystem1:
    def operation1(self):
        print("Subsystem1 operation")


# The Subsystem2 class is a class of the complex subsystem.
# The operation2 method is a method of the complex subsystem.
class Subsystem2:
    def operation2(self):
        print("Subsystem2 operation")


# The Subsystem3 class is a class of the complex subsystem.
# The operation3 method is a method of the complex subsystem.
class Subsystem3:
    def operation3(self):
        print("Subsystem3 operation")


if __name__ == '__main__':
    facade = Facade()
    facade.operation()
    facade.operation1()
