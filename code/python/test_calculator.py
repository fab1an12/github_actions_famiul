import unittest
from main import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
    
    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)
    
    def test_perform_operation(self):
        # Test using operation names
        self.assertEqual(self.calc.perform_operation('add', 5, 3), 8)
        self.assertEqual(self.calc.perform_operation('subtract', 5, 3), 2)
        self.assertEqual(self.calc.perform_operation('multiply', 5, 3), 15)
        self.assertEqual(self.calc.perform_operation('divide', 6, 3), 2)
        
        # Test using symbols
        self.assertEqual(self.calc.perform_operation('+', 5, 3), 8)
        self.assertEqual(self.calc.perform_operation('-', 5, 3), 2)
        self.assertEqual(self.calc.perform_operation('*', 5, 3), 15)
        self.assertEqual(self.calc.perform_operation('/', 6, 3), 2)
        
        # Test invalid operation
        with self.assertRaises(ValueError):
            self.calc.perform_operation('invalid', 5, 3)

if __name__ == "__main__":
    unittest.main()
