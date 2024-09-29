#!/usr/bin/python3

# Interpreter pattern is a behavioral pattern that provides a way to evaluate language grammar or expression.
# It is used to define a grammar for simple languages and provides an interpreter to interpret the grammar.
# It is used to create a simple language interpreter.

from abc import ABC, abstractmethod


# Abstract expression class that declares an interpret method. It is used to interpret the expression.
# It is used to define the interface for the expression.
class AbstractExpression(ABC):
    @abstractmethod
    def interpret(self):
        raise "It is needed to implement this method"


# Terminal expression class that implements the interpret method. It holds the number and returns it.
# It is used to represent the number in the expression. It is a leaf node in the expression tree. It does not have
# any sub-expression.
class NumberExpression(AbstractExpression):
    def interpret(self, context):
        num = ''
        while context.current() and context.current().isdigit():
            num += context.current()
            context.next()
        return int(num)


# Non-terminal expression class that implements the interpret method. It holds the left and right expressions.
# It interprets the left and right expressions and returns the result.
class OperatorExpression(AbstractExpression):
    def interpret(self, context):
        operator = context.current()
        context.next()
        return operator


# Add expression class that extends the OperatorExpression class. It interprets the left and right expressions and
# returns the sum of them.
class ParenthesesExpression(AbstractExpression):
    def interpret(self, context):
        context.next()  # Skip the opening parenthesis
        value = Expression().interpret(context)
        context.next()  # Skip the closing parenthesis
        return value


# Add expression class that extends the OperatorExpression class. It interprets the left and right expressions and
# returns the sum of them.
class Expression(AbstractExpression):
    def interpret(self, context):
        expressions = []
        while context.current():
            if context.current().isdigit():
                expressions.append(NumberExpression().interpret(context))
            elif context.current() in '+-*/':
                expressions.append(OperatorExpression().interpret(context))
            elif context.current() == '(':
                expressions.append(ParenthesesExpression().interpret(context))
            else:
                context.next()

        while len(expressions) > 1:
            left = expressions.pop(0)
            operator = expressions.pop(0)
            right = expressions.pop(0)

            if operator == '+':
                expressions.insert(0, left + right)
            elif operator == '-':
                expressions.insert(0, left - right)
            elif operator == '*':
                expressions.insert(0, left * right)
            elif operator == '/':
                expressions.insert(0, left / right)

        return expressions[0]


# Context class that holds the expression. It is used to interpret the expression.
class Context:
    def __init__(self, expression):
        self.expression = expression
        self.position = 0

    def next(self):
        self.position += 1

    def current(self):
        return self.expression[self.position] if self.position < len(self.expression) else None


if __name__ == '__main__':
    context = Context('(1+2)*3')
    print(Expression().interpret(context))