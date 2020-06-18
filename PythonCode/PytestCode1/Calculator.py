from decimal import Decimal, getcontext


class Calc:
    c = 0

    def add(self, a, b):
        c = ("%.2f" % (a + b))
        return c

    def sub(self, a, b):
        c = ("%.2f" % (a - b))
        return c

    def multiply(self, a, b):
        c = ("%.2f" % (a * b))
        return c

    def div(self, a, b):
        c = ("%.2f" % (a / b))
        return c
