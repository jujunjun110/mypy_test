class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** (1 / 2)

    def __str__(self) -> str:
        return f"Point ({self.x}, {self.y})"
