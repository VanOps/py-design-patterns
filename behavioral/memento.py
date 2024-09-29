#!/usr/bin/python3

# Memento pattern is a behavioral pattern that allows an object to capture its internal state without exposing its
# internal structure and to restore the object to that state later.
# It is used to capture the internal state of an object without exposing its internal structure.
# It is used to save and restore the state of an object.
# It is used to save the state of an object and restore it later.

from abc import ABC, abstractmethod


# Memento class that holds the state of the object
class Memento:
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state


# Originator class that creates a memento and restores the state of the object
class Originator:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def save_state_to_memento(self):
        return Memento(self.state)

    def get_state_from_memento(self, memento):
        self.state = memento.get_state()


# Caretaker class that holds the memento
class Caretaker:
    def __init__(self):
        self.memento = None

    def set_memento(self, memento):
        self.memento = memento

    def get_memento(self):
        return self.memento


if __name__ == '__main__':
    originator = Originator()
    caretaker = Caretaker()

    originator.set_state('State 1')
    originator.set_state('State 2')
    caretaker.set_memento(originator.save_state_to_memento())
    memento = caretaker.get_memento()
    print(memento.get_state())

    originator.set_state('State 3')
    print(f'Current state: {originator.state}')
    # caretaker.set_memento(originator.save_state_to_memento())
    memento = caretaker.get_memento()
    print(memento.get_state())

    originator.get_state_from_memento(caretaker.get_memento())
    print(f'Restored state: {originator.state}')
    memento = caretaker.get_memento()
    print(memento.get_state())
