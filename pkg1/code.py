import unittest

class Calculator(object):
    # 1st commit
    def add(self, x, y):
        pass

    # Improvisation 1
    def add(self, x, y):
        return x+y

    # Improvisation 2
    def add(self, x, y):
        if not (isinstance(x, int)) or not(isinstance(y, int)):
            return "invalid parameters, only integers are accepted"
        return x+y



