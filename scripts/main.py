def main() -> None:
    r = 2
    c = Circle(r)

    area = c.area()
    origin = c.origin()

    print(area)
    print(origin)


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius
        self.pi = 3.14

    def area(self) -> float:
        return self.radius ** 2 * self.pi

    def origin(self) -> "Point":
        return Point(0, 0)


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "Point ({}, {})".format(self.x, self.y)


if __name__ == "__main__":
    main()
