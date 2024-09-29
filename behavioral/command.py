#!/usr/bin/python3

# Command pattern is a behavioral pattern that encapsulates a request as an object, thereby allowing for
# parameterization of clients with different requests, queuing of requests, and logging of requests.
# It also supports undoable operations.
# It is a way to decouple the sender and receiver of a command. The sender just sends a command and the receiver
# executes it. The sender does not need to know how the command is executed.

from abc import ABC, abstractmethod


# Command interface that declares a method for executing a command
class CommandInterface(ABC):
    @abstractmethod
    def execute(self):
        pass


# Receiver class that knows how to perform the operation
class Light:
    def turn_on(self):
        print('Light is on')

    def turn_off(self):
        print('Light is off')


# Concrete command classes that implement the Command interface
class LightOnCommand(CommandInterface):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class LightOffCommand(CommandInterface):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


# Invoker class that holds the command and executes it when required.
class RemoteControl:
    def __init__(self):
        self.commands = {}

    def register(self, command_name, command):
        self.commands[command_name] = command

    def execute(self, command_name):
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print('Command not found')


if __name__ == '__main__':
    light = Light()
    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControl()
    remote.register('light_on', light_on)
    remote.register('light_off', light_off)

    remote.execute('light_on')
    remote.execute('light_off')
    remote.execute('light_on')
    remote.execute('light_off')
    remote.execute('fan_on')
