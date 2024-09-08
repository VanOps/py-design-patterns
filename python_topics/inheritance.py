
class Furniture(object):
    """Base class for all furniture"""
    def __init__(self, color, material):
        self.color = color
        self.material = material

    def get_color(self):
        return self.color

    def get_material(self):
        return self.material

    def __str__(self):
        return f"The color of the furniture is {self.color}, {self.material} is the material"


class Chair(Furniture):
    """Class for chairs"""

    # Use of overriding
    # It is the ability of a class to change the implementation of a method provided by one of its ancestors.
    def __init__(self, color, material, legs):
        # Use of super() method to call the parent class constructor and pass the parameters
        super().__init__(color, material)
        # Adding a new attribute to the child class
        self.legs = legs

    def get_legs(self):
        return self.legs

    # Use of Overloading
    # It is the ability of a function or an operator to behave in different ways based on the parameters that
    # are passed to the function, or the operands that the operator acts on. Could be marked as Overriding by using a
    # decorator @overload
    def get_color(self, show):
        message = f"The color of the chair is {self.color}, {self.material} is the material"
        return message

    def __str__(self):
        message = f"The color of the chair is {self.color}, {self.material} is the material, and it has {self.legs} legs"

        # Use of __bases__ method
        # The __bases__ attribute of a class object is a tuple of the base classes of the class.

        # Use of __subclasses__ method
        # The __subclasses__ method of a class object returns a list of all the subclasses of the class.

        # Use of __mro__ method
        # As a class could inherit from multiple classes, the method resolution order (MRO) is the order in which
        # base classes are searched when looking up a method in a class hierarchy.
        # __mro__ attribute of a class object is a ordered tuple of classes that are considered when looking up the
        # method

        extra = (f"\nIt is a {self.__class__.__name__}, base class is {self.__class__.__bases__} "
                 f"and subclasses are {self.__class__.__subclasses__()}")
        return message + extra


class BabyChair(Chair):
    """Class for baby chairs"""
    def __init__(self, color, material, legs, size):
        super().__init__(color, material, legs)
        self.size = size

    def get_size(self):
        return self.size

    def __str__(self):
        message = f"The color of the baby chair is {self.color}, {self.material} is the material, " \
                          f"it has {self.legs} legs and the size is {self.size}"
        # Use of __mro__ method
        # As a class could inherit from multiple classes, the method resolution order (MRO) is the order in which
        # base classes are searched when looking up a method in a class hierarchy.
        # __mro__ attribute of a class object is a ordered tuple of classes that are considered when looking up the
        # method

        extra = (f"\nIt is a {self.__class__.__name__}, base class is {self.__class__.__bases__} and order is {self.__class__.__mro__}")
        return message + extra


# Use of multiple inheritance
class BabyChairDeLuxe(BabyChair,Chair):
    """Class for baby chairs"""
    def __init__(self, color, material, legs, size, brand):
        super().__init__(color, material, legs, size)
        self.brand = brand

    def get_brand(self):
        return self.brand

if __name__ == '__main__':

    print("\n ----------------- \n")
    print("Creating an instance of the Chair class")
    chair = Chair("Red", "Wood", 4)
    print(chair.get_color(True))
    print(chair.get_legs())
    print(chair.__str__())
    print("\n ----------------- \n")
    print("Creating an instance of the BabyChair class")
    baby_chair = BabyChair("Blue", "Plastic", 3, "Small")
    print(baby_chair.get_color(True))
    print(baby_chair.get_legs())
    print(baby_chair.get_size())
    print(baby_chair.__str__())
    print("\n ----------------- \n")
    print("Creating an instance of the BabyChairDeLuxe class")
    baby_chair_deluxe = BabyChairDeLuxe("Green", "Plastic", 3, "Small", "IKEA")
    print(baby_chair_deluxe.get_color(True))
    print(baby_chair_deluxe.get_legs())
    print(baby_chair_deluxe.get_size())
    print(baby_chair_deluxe.get_brand())
    print("msg shows as the BabyChairDeLuxe class is inheriting from BabyChair __str__ msg")
    print(baby_chair_deluxe.__str__())
