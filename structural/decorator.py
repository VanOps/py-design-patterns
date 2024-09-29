#!/usr/bin/python3

# Decorator pattern is a structural pattern that allows adding new behaviors to objects dynamically by placing them
# inside special wrapper objects called decorators. It is useful when we want to add new functionalities to objects
# without changing their structure.
# It is useful when we want to add new functionalities to objects without changing their structure.


# The Component class is the interface that defines the method to be decorated.
class Component:
    def operation(self): pass


# The ConcreteComponent class implements the Component interface and defines the method to be decorated.
class ConcreteComponent(Component):
    def operation(self):
        print("ConcreteComponent operation")


# The Decorator is used as parent class for the ConcreteDecorator classes. It is an optional class.
class Decorator(Component):
    def __init__(self, component):
        self.component = component

    def operation(self):
        self.component.operation()


# The ConcreteDecorator class implements the Decorator interface and defines the method to add new functionalities to
# the object.
class ConcreteDecoratorA(Decorator):
    def operation(self):
        print("ConcreteDecoratorA operation")
        self.component.operation()


# The ConcreteDecorator class implements the Decorator interface and defines the method to add new functionalities to
# the object.
class ConcreteDecoratorB(Decorator):
    def operation(self):
        print("ConcreteDecoratorB operation")
        self.component.operation()


if __name__ == '__main__':
    # Use case
    component = ConcreteComponent()
    component.operation()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # Another use case
    component = ConcreteDecoratorA(ConcreteComponent())
    component.operation()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # Another use case
    component = ConcreteDecoratorB(ConcreteComponent())
    component.operation()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # Another use case
    component = ConcreteDecoratorA(ConcreteDecoratorB(ConcreteComponent()))
    component.operation()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # Another use case
    component = ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent()))
    component.operation()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # Another use case
    component = ConcreteDecoratorA(ConcreteDecoratorB(ConcreteDecoratorA(ConcreteComponent())))
    component.operation()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")