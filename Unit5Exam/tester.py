
import unittest
from student_solution import calculate_total_cost

class TestCalculateTotalCost(unittest.TestCase):
    def test_default_tip(self):
        self.assertAlmostEqual(calculate_total_cost(100), 115.00)
        self.assertAlmostEqual(calculate_total_cost(50), 57.50)

    def test_custom_tip(self):
        self.assertAlmostEqual(calculate_total_cost(100, 20), 120.00)
        self.assertAlmostEqual(calculate_total_cost(50, 10), 55.00)

    def test_zero_tip(self):
        self.assertAlmostEqual(calculate_total_cost(100, 0), 100.00)

    def test_negative_tip(self):
        # Ensure negative tip uses default of 15%
        self.assertAlmostEqual(calculate_total_cost(100, -5), 115.00)

    def test_rounding(self):
        # Test proper rounding
        self.assertAlmostEqual(round(calculate_total_cost(50.123, 10), 2), 55.14)

if __name__ == "__main__":
    unittest.main()
