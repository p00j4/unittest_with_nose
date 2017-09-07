import unittest
from pkg1.code import Calculator

class TestCalculator(unittest.TestCase):

    def test_add_method(self):
        calc = Calculator()
        """ check addition for integer user inpouts """
        result = calc.add(2,2)
        self.assertEqual(4, result)

        """ check addition for varied user inputs """
        result = calc.add(2,'b')
        self.assertEqual('2b', result)

if __name__ == '__main__':
    unittest.main()
