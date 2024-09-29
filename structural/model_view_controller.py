#!/usr/bin/python3

# Model-View-Controller (MVC) pattern is a design pattern that separates the application into three main components:
#   -Model: Model is the data layer, the View is the presentation layer, and the Controller is the logic layer.
#   -View: View is the presentation layer that displays the data to the user.
#   -Controller: Controller is the logic layer that processes the data and sends it to the view.

# The Model class is the data layer that stores the data.
# The __data attribute is a private attribute that stores the data.
# The __init__ method is the constructor that initializes the data.
# The get_data method returns the data.
# The set_data method sets the data.
class Model:
    def __init__(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data


# The View class is the presentation layer that displays the data to the user.
# The show_data method displays the data.
class View:
    def show_data(self, data):
        print("Data: ", data)


# The Controller class is the logic layer that processes the data and sends it to the view.
# The __model attribute is a private attribute that stores the model object.
# The __view attribute is a private attribute that stores the view object.
# The __init__ method is the constructor that initializes the model and view objects.
# The process_data method processes the data and sends it to the view.
class Controller:
    def __init__(self, model, view):
        self.__model = model
        self.__view = view

    def process_data(self):
        data = self.__model.get_data()
        self.__view.show_data(data)


if __name__ == '__main__':
    model = Model("Hello, World!")
    view = View()
    controller = Controller(model, view)
    controller.process_data()
