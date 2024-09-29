#!/usr/bin/python3

# Strategy pattern is a behavioral pattern that defines a family of algorithms, encapsulates each algorithm, and makes
# them interchangeable at runtime. It lets the algorithm vary independently of the clients that use it.

from abc import ABC, abstractmethod


# Strategy interface that declares a method for performing an algorithm
class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self):
        pass


# Concrete strategy classes that implement the Strategy interface
class ConcreteStrategyA(Strategy):
    def do_algorithm(self):
        print('ConcreteStrategyA algorithm')


class ConcreteStrategyB(Strategy):
    def do_algorithm(self):
        print('ConcreteStrategyB algorithm')


class ConcreteStrategyC(Strategy):
    def do_algorithm(self):
        print('ConcreteStrategyC algorithm')


# Context class that holds the strategy and executes the algorithm
class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_algorithm(self):
        self.strategy.do_algorithm()


if __name__ == '__main__':
    strategy_a = ConcreteStrategyA()
    context = Context(strategy_a)
    context.execute_algorithm()

    strategy_b = ConcreteStrategyB()
    context = Context(strategy_b)
    context.execute_algorithm()

    strategy_c = ConcreteStrategyC()
    context = Context(strategy_c)
    context.execute_algorithm()
