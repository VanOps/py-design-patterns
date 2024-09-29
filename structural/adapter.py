#!/usr/bin/python3

# Adapter pattern is a structural pattern that allows objects with incompatible interfaces to collaborate. It is useful
# when we want to use an existing class, and its interface does not match the one we need.
# The Adapter pattern allows us to create a new class that will adapt the existing class to the interface we need.

# The Adapter class is the class that adapts the existing class to the interface we need.
# The __init__ method is the constructor that initializes the existing class.
# The operation method is the method that adapts the existing class to the interface we need.
class Adapter:
    def __init__(self):
        self.adaptee = Adaptee()

    def operation(self):
        operation = self.adaptee.specific_operation()
        # Adapt the existing class to the interface we need
        # replace eachletter with ascii value
        operation_adapted = []
        for letter in operation:
            operation_adapted.append(ord(letter))
        return operation_adapted


class Translator:
    def translate(self, list):
        # Replace each ascii value in the list with letter in string
        translated_text = ""
        for ascii_value in list:
            translated_text += chr(ascii_value)
        return translated_text


# The Adaptee class is the existing class that we want to adapt to the interface we need.
# The specific_operation method is the method of the existing class.
class Adaptee:
    def specific_operation(self):
        return "Adaptee specific operation"


if __name__ == '__main__':
    # Use case
    adapter = Adapter()
    recovered_list = adapter.operation()
    print("Adapter operation:", recovered_list)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # Another use case
    adaptee = Adaptee()
    print("Adaptee operation:", adaptee.specific_operation())
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # Translate the recovered text
    translator = Translator()
    translated_text = translator.translate(recovered_list)
    print("Translated text:", translated_text)