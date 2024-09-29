#!/usr/bin/python3

# Abstract Factory pattern is a creational pattern that provides an interface to create families of related or
# dependent objects without specifying their concrete classes.
# It is similar to the Factory pattern, but it is used get one more level of abstraction and flexibility.

# The AbstractFactory class is the interface that defines the methods to create the objects.
# The create_product_a and create_product_b methods are abstract methods that must be implemented by the concrete
# classes.
# These methods do not always create the object. They can return an instance of the object that is already
# created, depending on the requirements.
class AbstractFactory:
    def create_product_a(self): pass

    def create_product_b(self): pass


# The ConcreteFactory1 class implements the AbstractFactory interface and defines the methods to create the objects.
class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ProductA1()

    def create_product_b(self):
        return ProductB1()


# The ConcreteFactory2 class implements the AbstractFactory interface and defines the methods to create the objects.
class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ProductA2()

    def create_product_b(self):
        return ProductB2()

    # The AbstractProductA class is the interface that defines the method to show the product.


# The show method is an abstract method that must be implemented by the concrete classes.
class AbstractProductA:
    def show(self): pass


# The AbstractProductB class is the interface that defines the method to show the product.
# The show method is an abstract method that must be implemented by the concrete classes.
class AbstractProductB:
    def show(self): pass


# The ProductA1 class implements the AbstractProductA interface and defines the method to show the product.
class ProductA1(AbstractProductA):
    def show(self):
        print("Product A1")


# The ProductB1 class implements the AbstractProductB interface and defines the method to show the product.
class ProductB1(AbstractProductB):
    def show(self):
        print("Product B1")


# The ProductA2 class implements the AbstractProductA interface and defines the method to show the product.
class ProductA2(AbstractProductA):
    def show(self):
        print("Product A2")


# The ProductB2 class implements the AbstractProductB interface and defines the method to show the product.
class ProductB2(AbstractProductB):
    def show(self):
        print("Product B2")


if __name__ == '__main__':
    factory = ConcreteFactory1()
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    product_a.show()
    product_b.show()

    factory = ConcreteFactory2()
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    product_a.show()
    product_b.show()
