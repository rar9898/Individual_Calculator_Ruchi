def addition(a, b):
    return a + b


def subraction(a, b):
    return a - b


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subract(self, a, b):
        self.result = subraction(a, b)
        return self.result