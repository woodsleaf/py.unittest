import unittest
from squares import square_area


class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when radius >= 0
        self.assertAlmostEqual(square_area(1), 1)
        self.assertAlmostEqual(square_area(0), 0)
        self.assertAlmostEqual(square_area(2.1), 2.1 * 2.1)

    def test_values(self):
        # Make sure values errors are raised when necessary
        self.assertRaises(ValueError, square_area, -2)
