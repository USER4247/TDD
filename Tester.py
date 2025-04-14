import unittest
from Calc import Calculator

class Tester(unittest.TestCase):
    
    def test_add_1(self):
        results = Calculator().add('')
        self.assertAlmostEqual(results, 0.0, places=1)

    def test_add_2(self):
        results = Calculator().add('1')
        self.assertAlmostEqual(results, 1.0, places=1)

    def test_add_3(self):
        results = Calculator().add('1,5')
        self.assertAlmostEqual(results, 6.0, places=1)
    
    def test_add_4(self):
        results = Calculator().add("1\n2,3")
        self.assertAlmostEqual(results, 6.0, places=1)

    def test_add_5(self):
        results = Calculator().add("//;\n1;2")
        self.assertAlmostEqual(results, 3.0, places=1)

    def test_negative_number_raises_exception(self):
        with self.assertRaisesRegex(Exception, "negative numbers not allowed -5.0, -7.0"):
            Calculator().add("1,-5,-7")

    def test_add_float(self):
        results = Calculator().add("//;\n1.0;2.4")
        self.assertAlmostEqual(results, 3.4, places=1)

    def test_add_invalid_characters(self):
        with self.assertRaises(ValueError):
            # input contains "1a" and "a4", which are invalid characters
            Calculator().add("//;\n1.0;2.4;1a;a4")

if __name__ == "__main__":
    unittest.main()
