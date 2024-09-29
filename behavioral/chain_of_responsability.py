#!/bin/src/python3

# Chain of responsibility pattern is a behavioral pattern that allows an object to send a command without knowing what
# object will receive and handle it. It decouples the sender and receiver of a request based on type of request.
# It is used to pass the request along a chain of handlers. It is used to handle the request in a chain of handlers.
# It is used to define a chain of handlers for a request.

from abc import ABC, abstractmethod


# Handler interface that declares a method for handling the request
class Handler(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass


# Concrete handler classes that implement the Handler interface
class ConcreteHandler1(Handler):
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if request == 'R1':
            print('ConcreteHandler1 handles the request')
        elif self.successor:
            self.successor.handle_request(request)


class ConcreteHandler2(Handler):
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if request == 'R2':
            print('ConcreteHandler2 handles the request')
        elif self.successor:
            self.successor.handle_request(request)


class ConcreteHandler3(Handler):
    def __init__(self, successor=None):
        self.successor = successor

    def handle_request(self, request):
        if request == 'R3':
            print('ConcreteHandler3 handles the request')
        elif self.successor:
            self.successor.handle_request(request)


if __name__ == '__main__':
    handler1 = ConcreteHandler1(ConcreteHandler2(ConcreteHandler3()))
    handler1.handle_request('R1')
    handler1.handle_request('R2')
    handler1.handle_request('R3')
    handler1.handle_request('R4')
