import ccxt
import json
from typing import List, Any, Optional
from enum import Enum


class Side(Enum):
    BUY = 1
    SELL = 2


class Order:
    rate: float
    amount: float

    def __init__(self, order: List[float]):
        self.rate = order[0]
        self.amount = order[1]


class Book:
    asks: List[Order]
    bids: List[Order]

    def __init__(self, book: dict):
        self.asks = [Order(o) for o in book["asks"]]
        self.bids = [Order(o) for o in book["bids"]]

    def dig(self, side: Side, amount: float) -> Optional[float]:
        target_books = self.asks if side == Side.BUY else self.bids
        total = 0.0

        for order in target_books:
            total += order.amount
            if total >= amount:
                return order.rate

        return None


class MarketClient:
    def __init__(self) -> None:
        self.client: ccxt.base.exchange
        self.pair: str

    def fetch_ticker(self) -> str:
        return self.client.fetch_ticker(self.pair)

    def fetch_book(self) -> Optional[Book]:
        try:
            book = self.client.fetch_order_book(self.pair)
            return Book(book)

        except Exception:
            return None


class Bitflyer(MarketClient):
    def __init__(self) -> None:
        super().__init__()
        self.client = ccxt.bitflyer()
        self.pair = "BTC/JPY"
