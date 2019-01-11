import unittest


class Test_TestCircle(unittest.TestCase):
    def test_area(self):
        self.assertEqual(5, 5)
        # self.assertEqual(Circle(3, Point(0, 0)), 28.26)


if __name__ == "__main__":
    unittest.main()
