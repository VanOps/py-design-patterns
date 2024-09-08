#!/usr/bin/python3

from termcolor import colored


# Decorator is a design pattern in Python that allows a user to add new functionality to an existing object without
# modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

# Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or
# class. Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without
# permanently modifying it.

# Example of using a decorator:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_hello():
    print("Hello!")


if __name__ == '__main__':
    print(colored("msg: Execution of the function without the decorator", 'red'))
    say_hello()
    print("\n")
    print(colored("msg: execution of the function with the decorator", 'blue'))
    say_hello = my_decorator(say_hello)
    say_hello()
