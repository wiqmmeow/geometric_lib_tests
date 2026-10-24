import unittest
import math
import circle
import rectangle
import square
import triangle
class TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle.area(2), math.pi * 4)
         
    def test_perimeter(self):
        self.assertAlmostEqual(circle.perimeter(2), math.pi * 4)

class TestRectangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle.area(3, 4), 12)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(3, 4), 14)

class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square.area(5), 25)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)

class TestTriangle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(triangle.area(6, 4), 12)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(3, 4, 5), 12)
if __name__ == "__main__":
    unittest.main()