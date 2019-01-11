import unittest

from scripts.modules.point import Point


class Test_TestPoint(unittest.TestCase):
    def test_distance(self):
        p = Point(3, 4)
        self.assertEqual(p.distance_from_origin(), 5)


if __name__ == "__main__":
    unittest.main()
