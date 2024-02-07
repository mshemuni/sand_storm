from typing import Tuple

from v3d import Vector, Point


class Sand:
    def __init__(self, pos: Vector, color: Tuple) -> None:
        self.pos = pos
        self.vel = Vector()
        self.acc = Vector()
        self.color = color
        self.is_falling = True

    def move(self) -> None:
        self.vel += self.acc
        self.pos += self.vel
        self.pos = Vector(Point(int(self.pos.point.x), int(self.pos.point.y)))

    def apply_acceleration(self, acc: Vector) -> None:
        self.acc = acc

    def reset_acceleration(self) -> None:
        self.acc = Vector()

    def is_dead(self, shape: Tuple[int, int]) -> bool:
        width, height = shape
        horizontal = self.pos.point.x < 0 or self.pos.point.x > width
        vertical = self.pos.point.y < 0 or self.pos.point.y > height
        return horizontal or vertical
