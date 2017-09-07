import unittest
from pkg1.code import Calculator
from nose_parameterized import parameterized

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """ Use this to do task at the beginning of test cases execution
            Eg. setting up environment or set global objects
        """
        self.calc = Calculator()

    def tearDown(self):
        """
        use this to clear data/objects created because of tests at end of the execution
        :return:
        """
        pass

    # Basic Test case
    def test_add_method_1(self):
        """ check addition for integer user inputs """
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)

    # test 2: check for possible use cases
    def test_add_method_2(self):
        """ check addition for integer user inpouts """
        result = self.calc.add(2,2)
        self.assertEqual(4, result)

        """ check addition for various user inputs """
        result = self.calc.add(2,'b')
        # self.assertEqual('2b', result)

    # test 3: based on code improvisation, improve test as well to not raise false alarms
    def test_add_method_3(self):
        """ check addition for various user inputs """
        # valid integer input
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)

        # string input
        result = self.calc.add(2, 'b')
        self.assertTrue(result.find('invalid parameters') != -1, "invalid checks are not working")

        # empty input
        result = self.calc.add('', '')
        self.assertTrue(result.find('invalid parameters') != -1, "invalid checks are not working")

        # unicode input
        result = self.calc.add(u'\u0bcd', u'\U0001F44D')
        self.assertTrue(result.find('invalid parameters') != -1, "invalid checks are not working")

    # test cover 4: lot of code repetition in last, let's bring more readability, more coverage with less writing
    @parameterized.expand([
        ("whole_numbers", 10, 9, 19),
        ("negative_numbers", 0, -1, -1),
        ("invalid_string", "a", "b", "invalid parameters, only integers are accepted"),
        ("invalid_empty", "", "", "invalid parameters, only integers are accepted"),
        ("invalid_unicode", u'\u0bcd', u'\U0001F44D', "invalid parameters, only integers are accepted"),
    ])
    def test_add_method(self, name, a,b, expected):
        calc = Calculator()
        """ check addition for various user inputs """
        result = calc.add(a, b)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
