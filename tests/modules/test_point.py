import unittest

from scripts.modules.point import Point


class Test_TestPoint(unittest.TestCase):
    def test_distance(self):
        cases = [(Point(0, 0), 0), (Point(3, 4), 5), (Point(-3, -4), 5)]

        for p, expected in cases:
            self.assertEqual(p.distance_from_origin(), expected)


if __name__ == "__main__":
    unittest.main()
