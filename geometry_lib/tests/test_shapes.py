from unittest import TestCase

from geometry_lib.shapes import Circle, Triangle



class TestShapes(TestCase):
    def test_circle_area(self):
        c = Circle(5)
        self.assertAlmostEqual(c.area(), 78.538, 2)

    def test_triangle_radius(self):
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(t.area(), 6.0, 2)
        self.assertTrue(t.is_right())

    def test_triangle_not_right(self):
        t = Triangle(2, 3, 4)
        self.assertFalse(t.is_right())

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(-1, 2, 3)

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(-1)

    def test_invalid_circle_string(self):
        with self.assertRaises(ValueError):
            Circle('a')

    def test_calculate_area(self):
        from geometry_lib.utils import calculate_area
        c = Circle(5)
        t = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(c), 78.538, 2)
        self.assertAlmostEqual(calculate_area(t), 6.0, 2)

