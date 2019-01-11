from .point import Point


class Circle:
    def __init__(self, radius: float, origin: Point) -> None:
        self.radius = radius
        self.point = origin
        self.pi = 3.14

    def area(self) -> float:
        return self.radius ** 2 * self.pi

    def xmax(self) -> float:
        return self.point.x + self.radius

    def origin(self) -> "Point":
        return self.point
