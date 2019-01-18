import unittest

from scripts.modules.cryptocurrency import Bitflyer, Side, Book, Order


class TestCryptoCurrency(unittest.TestCase):
    def test_book(self) -> None:
        b = Bitflyer()
        book = b.fetch_book()

        print(book.dig(Side.BUY, 1))

        book_dict = {
            "asks": [[200, 0.2], [210, 0.2], [220, 0.2], [230, 0.2], [240, 0.2]],
            "bids": [[190, 0.2], [180, 0.2], [170, 0.2], [160, 0.2], [150, 0.2]],
        }

        book = Book(book_dict)

        self.assertEqual(book.dig(Side.BUY, 0), 200)
        self.assertEqual(book.dig(Side.BUY, 0.1), 200)
        self.assertEqual(book.dig(Side.BUY, 0.3), 210)
        self.assertEqual(book.dig(Side.BUY, 1.0), 240)
        self.assertEqual(book.dig(Side.BUY, 1.1), None)


if __name__ == "__main__":
    unittest.main()
