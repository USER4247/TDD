import unittest
from Calc import Calculator
class Tester(unittest.TestCase):
    
    def test_add_1(self):
        results = Calculator().add('')
        self.assertEqual(results , 0)



if __name__ == "__main__":
    unittest.main()