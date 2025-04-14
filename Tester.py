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

if __name__ == "__main__":
    unittest.main()
