import unittest

from scripts.modules.point import Point
from scripts.modules.circle import Circle


class Test_TestCircle(unittest.TestCase):
    def test_area(self) -> None:
        c = Circle(0, Point(0, 0))
        self.assertEqual(c.area(), 0)

        c = Circle(3, Point(0, 0))
        self.assertAlmostEqual(c.area(), 28.27433388230813)

    def test_xmax(self) -> None:
        c = Circle(3, Point(4, 2))
        self.assertEqual(c.xmax(), 7)


if __name__ == "__main__":
    unittest.main()
