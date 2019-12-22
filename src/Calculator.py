import math


def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b


def subtraction(a, b):
    a = int(a)
    b = int(b)
    return a - b


def multiplication(a, b):
    a = int(a)
    b = int(b)
    return a * b


def division(a, b):
    a = int(a)
    b = int(b)
    if a != 0:
        return round(b / a, 7)
    else:
        return "Dividend cannot be zero."


def square(a):
    a = int(a)
    return a * a


def squareroot(a):
    a = int(a)
    return round(math.sqrt(a), 8)


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def sqr(self, a):
        self.result = square(a)
        return self.result

    def sqrrt(self, a):
        self.result = squareroot(a)
        return self.result
