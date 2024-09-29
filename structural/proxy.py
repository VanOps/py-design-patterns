#|/usr/bin/python3

# Proxy pattern is a structural pattern that provides a surrogate or placeholder for another object to control
# access to it. It is useful when we want to control access to an object, add extra functionality to an object,
# or delay the creation of an object.


# The Subject class is an interface that defines the methods that the RealSubject and Proxy classes must implement.
class SubjectInterface:
    def request(self): pass


# The RealSubject class implements the Subject interface and defines the methods to be implemented.
class RealSubject(SubjectInterface):
    def request(self):
        print("RealSubject request")
        print("Success")


# The Proxy class implements the Subject interface and defines the methods to be implemented.
# The constructor initializes the RealSubject object.
# The request method calls the request method of the RealSubject object.
class Proxy(SubjectInterface):
    def __init__(self):
        self.real_subject = RealSubject()

    def request(self, user):
        if user.user_id > 10000:
            print("Proxy request")
            print("Access granted")
            self.real_subject.request()
        else:
            print("Proxy request")
            print("Access denied")



class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def request(self):
        self.proxy.request()


if __name__ == '__main__':
    # Use case
    user1 = User(15323)
    proxy = Proxy()
    proxy.request(user1)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    ## Another use case
    user2 = User(1)
    proxy.request(user2)
