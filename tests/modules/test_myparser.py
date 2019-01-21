import unittest

from scripts.modules.myparser import MyParser


class Test_TestMyParser(unittest.TestCase):
    def test_extract_number(self) -> None:
        cases = [
            ("", None),
            ("abc", None),
            ("0123", 123),
            ("-0123", -123),
            ("1a2b3c", 123),
            ("-1a2b3c", -123),
            ("12.3", 12.3),
            ("-12.3", -12.3),
        ]

        p = MyParser()
        for case, expected in cases:
            self.assertEqual(p.extract_number(case), expected)


if __name__ == "__main__":
    unittest.main()
