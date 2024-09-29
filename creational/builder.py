#!/usr/bin/python3

# Builder pattern is a creational pattern that allows constructing complex objects step by step. This construction
# process can create different representations of the object.
# It is useful when the object has a lot of parameters and we want to keep the construction process independent of the
# main object.


# The Director class is responsible for the construction of the object. It receives the builder object and calls the
# methods to build the object.
class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()


# The Builder class is an **interface** that defines the methods to build the object.
class Builder:
    def build_part_a(self): pass
    def build_part_b(self): pass
    def build_part_c(self): pass


# The ConcreteBuilder class implements the Builder interface and defines the methods to build the object.
class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add("Part A")

    def build_part_b(self):
        self.product.add("Part B")

    def build_part_c(self):
        self.product.add("Part C")

    def get_product(self):
        return self.product


# The Product class is the object that is being built.
class Product:
    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        print("Product parts: ", self.parts)


if __name__ == '__main__':
    builder = ConcreteBuilder()
    director = Director(builder)
    director.construct()
    product = builder.get_product()
    product.show()
