class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "Point ({}, {})".format(self.x, self.y)


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


def main() -> None:
    r = 2
    o = Point(3, 3)
    c = Circle(r, o)

    area = c.area()
    origin = c.origin()
    xmax = c.xmax()

    print(area)
    print(origin)
    print(xmax)


if __name__ == "__main__":
    main()
