#!/usr/bin/python3

# Observer pattern is a behavioral pattern that defines a one-to-many dependency between objects so that when one object
# changes state, all its dependents are notified and updated automatically.
# It is used to define a subscription mechanism to notify multiple objects about any events that happen to the object
# they are observing.
# It is used to define a one-to-many dependency between objects so that when one object changes state, all its
# dependents are notified and updated automatically.

from abc import ABC, abstractmethod


# Subject class that holds the list of observers and notifies them when the state
# of the object changes
class Subject(ABC):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def set_state(self, state):
        pass


# Concrete subject class that extends the Subject class and implements the get_state and set_state methods
class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
        self.notify()


# Observer interface that declares an update method
class Observer(ABC):
    @abstractmethod
    def update(self):
        pass


# Concrete observer class that implements the Observer interface
class ConcreteObserver(Observer):
    def __init__(self, subject):
        self.subject = subject
        self.subject.attach(self)

    def update(self):
        print(f'Observer state: {self.subject.get_state()}')

    def unsubscribe(self):
        self.subject.detach(self)


if __name__ == '__main__':
    # Example of the observer pattern
    subject = ConcreteSubject()
    observer1 = ConcreteObserver(subject)
    observer2 = ConcreteObserver(subject)

    subject.set_state('State 1')
    observer1.unsubscribe()
    subject.set_state('State 2')
    observer2.unsubscribe()
    subject.set_state('State 3')
    observer1 = ConcreteObserver(subject)
    subject.set_state('State 4')
    observer2 = ConcreteObserver(subject)
    subject.set_state('State 5')
    observer1.unsubscribe()
    observer2.unsubscribe()


