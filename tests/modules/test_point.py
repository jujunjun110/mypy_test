import unittest

from scripts.modules.point import Point


class Test_TestPoint(unittest.TestCase):
    def test_distance(self) -> None:
        cases = [
            (Point(0, 0), 0),
            (Point(3, 4), 5),
            (Point(-3, -4), 5),
            (Point(1, 1), 1.41421356),
        ]

        for p, expected in cases:
            self.assertAlmostEqual(p.distance_from_origin(), expected)


if __name__ == "__main__":
    unittest.main()
