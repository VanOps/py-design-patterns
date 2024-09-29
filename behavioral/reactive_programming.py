#!/usr/bin/python3
from rx3.core import Observer
from rx3.subject import Subject


# Reactive programming pattern is a behavioral pattern that is used to define a one-to-many dependency between objects
# so that when one object changes state, all its dependents are notified and updated automatically.
# It is used to define a subscription mechanism to notify multiple objects about any events that happen to the object
# they are observing.


# Subject class that holds the list of observers and notifies them when the state
# of the object changes
class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self.state = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
        self.on_next(state)



# Observer class that implements the Observer interface
class ConcreteObserver(Observer):
    def __init__(self, name: str):
        self.name = name

    def on_next(self, value):
        print(f'{self.name} received: {value}')

    def on_error(self, error):
        print(f'{self.name} received error: {error}')

    def on_completed(self):
        print(f'{self.name} received completed')


if __name__ == '__main__':
    subject = ConcreteSubject()
    observer1 = ConcreteObserver('Observer 1')
    observer2 = ConcreteObserver('Observer 2')
    observer3 = ConcreteObserver('Observer 3')

    subject.subscribe(observer1)
    subject.subscribe(observer2)
    subject.subscribe(observer3)

    subject.set_state('State 1')
    subject.set_state('State 2')
    subject.set_state('State 3')
    subject.set_state('State 4')
    subject.set_state('State 5')
    subject.set_state('State 6')
    subject.set_state('State 7')
    subject.set_state('State 8')
    subject.set_state('State 9')