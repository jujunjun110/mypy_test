from .point import Point
import math


class Circle:
    def __init__(self, radius: float, origin: Point) -> None:
        self.radius = radius
        self.point = origin

    def area(self) -> float:
        return self.radius ** 2 * math.pi

    def xmax(self) -> float:
        return self.point.x + self.radius

    def origin(self) -> "Point":
        return self.point
