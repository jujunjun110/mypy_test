import unittest

from scripts.modules.cryptocurrency import Bitflyer, Side, Book, Order


class TestCryptoCurrency(unittest.TestCase):
    def seuUp(self) -> Bitflyer:
        self.client = Bitflyer()

    def test_somehow_moves(self):
        bf = Bitflyer()
        buy_rate = bf.fetch_book().dig(Side.BUY, 0.5)
        sell_rate = bf.fetch_book().dig(Side.SELL, 0.5)
        print("buy_rate: {}".format(buy_rate))
        print("sell_rate: {}".format(sell_rate))
        self.assertEqual(type(buy_rate), float)
        self.assertEqual(type(sell_rate), float)

    def test_book(self) -> None:
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
