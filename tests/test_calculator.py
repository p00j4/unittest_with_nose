import unittest
from pkg1.code import Calculator

class TestCalculator(unittest.TestCase):

    # 1st commit
    def test_add_method_1(self):
        calc = Calculator()
        """ check addition for integer user inputs """
        result = calc.add(2, 2)
        self.assertEqual(4, result)

    # test cover 2
    def test_add_method_2(self):
        calc = Calculator()
        """ check addition for integer user inpouts """
        result = calc.add(2,2)
        self.assertEqual(4, result)

        """ check addition for various user inputs """
        result = calc.add(2,'b')
        self.assertEqual('2b', result)

    # test cover 3
    def test_add_method_2(self):
        calc = Calculator()
        """ check addition for various user inputs """
        result = calc.add(2, 'b')
        self.assertEqual('invalid parameters, only integers are accepted', result)


if __name__ == '__main__':
    unittest.main()
