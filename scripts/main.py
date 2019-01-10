from typing import *


def main() -> None:
    r = 2
    c = Circle(r)
    area = c.area()
    print(area)


class Circle:

    def __init__(self, radius: float) -> None:
        self.radius = radius
        self.pi = 3.14

    def area(self) -> float:
        return self.radius**2 * self.pi


if __name__ == '__main__':
    main()
