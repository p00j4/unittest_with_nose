import unittest

class Calculator(object):

    def add(self, x, y):
        if type(x) != int or type(y) != int:
            return "invalid parameters, only integers are accepted"
        return x+y



