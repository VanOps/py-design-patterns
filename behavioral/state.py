#!/bin/src/python3

# State pattern is a behavioral pattern that allows an object to change its behavior when its internal state changes.
# It is used to define a state machine for an object. It is used to represent the state of an object.
# It is used to define the state of an object and the actions that can be performed on the object.

from abc import ABC, abstractmethod


# State interface that declares a method for performing an action
class StateInterface(ABC):
    @abstractmethod
    def do_action(self):
        pass


# Concrete state classes that implement the State interface
class StartState(StateInterface):
    def do_action(self):
        print('Player is in start state')
        context.set_state('start')


class StopState(StateInterface):
    def do_action(self):
        print('Player is in stop state')
        context.set_state('stop')


# Context class that holds the state of the object
class Context:
    def __init__(self):
        self.state = None

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return f'Current state is: {self.state}'


if __name__ == '__main__':
    context = Context()
    start_state = StartState()
    start_state.do_action()
    print(context.get_state())
    stop_state = StopState()
    stop_state.do_action()
    print(context.get_state())
