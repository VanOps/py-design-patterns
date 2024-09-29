#!/usr/bin/python3

# Template pattern is a behavioral pattern that defines the skeleton of an algorithm in the superclass but lets
# subclasses override specific steps of the algorithm without changing its structure.
# It is used to define the steps of an algorithm in the superclass but allow subclasses to override specific steps
# of the algorithm without changing its structure.

from abc import ABC, abstractmethod


# Abstract class that defines the template method
class AbstractClass(ABC):
    def template_method(self):
        self.base_operation1()
        self.required_operation1()
        self.base_operation2()
        self.hook1()
        self.required_operation2()
        self.base_operation3()
        self.hook2()

    def base_operation1(self):
        print('AbstractClass base_operation1')

    def base_operation2(self):
        print('AbstractClass base_operation2')

    def base_operation3(self):
        print('AbstractClass base_operation3')

    @abstractmethod
    def required_operation1(self):
        pass

    @abstractmethod
    def required_operation2(self):
        pass

    def hook1(self):
        pass

    def hook2(self):
        pass


# Concrete class that implements the template method
class ConcreteClass(AbstractClass):
    def required_operation1(self):
        print('ConcreteClass required_operation1')

    def required_operation2(self):
        print('ConcreteClass required_operation2')

    def hook1(self):
        print('ConcreteClass hook1')

    def hook2(self):
        print('ConcreteClass hook2')


if __name__ == '__main__':
    print('### AbstractClass template method:')
    concrete_class = ConcreteClass()
    print('### ConcreteClass template method:')
    concrete_class.template_method()
