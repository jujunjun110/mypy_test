from modules.point import Point
from modules.circle import Circle


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
