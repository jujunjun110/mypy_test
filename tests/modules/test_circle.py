import unittest

from scripts.modules.point import Point
from scripts.modules.circle import Circle


class Test_TestCircle(unittest.TestCase):
    def test_area(self):
        c = Circle(0, Point(0, 0))
        self.assertEqual(c.area(), 0)

        c = Circle(3, Point(0, 0))
        self.assertEqual(c.area(), 28.26)


if __name__ == "__main__":
    unittest.main()
