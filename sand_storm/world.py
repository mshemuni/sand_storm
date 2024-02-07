from random import randint
from typing import List, Tuple

from v3d import Vector, Point
from sand_storm.sand import Sand
from sand_storm.colors import Colors


class World:
    def __init__(self, grid: Tuple[int, int], sands: List[Sand], friction: int = 2) -> None:
        self.grid = grid
        self.sands = sands
        self.friction = friction

        self.G: Vector = Vector(Point(0, 0.1, 0))

    def add_sand(self, x: int, y: int) -> None:
        self.sands.append(
            Sand(Vector(Point(int(x), int(y), 0)), Colors.random_color())
        )

    def check_drift(self, index: int) -> None:
        if not self.sands[index].is_falling:
            if self.sands[index].pos.point.y == self.grid[1] - 1:
                return

            y = self.sands[index].pos.point.y
            left = self.sands[index].pos.point.x - 1
            right = self.sands[index].pos.point.x + 1

            can_move: List[bool] = [True, True]
            for other in self.sands:
                if other is not self.sands[index]:
                    if y < other.pos.point.y < y + self.friction:
                        if other.pos.point.x == left:
                            can_move[0] = False
                        if other.pos.point.x == right:
                            can_move[1] = False

            if all(can_move):
                self.sands[index].pos.point.x += pow(-1, randint(0, 1))
            elif can_move[0]:
                self.sands[index].pos.point.x += -1
            elif can_move[1]:
                self.sands[index].pos.point.x += 1

    def check_falling(self, index: int) -> None:
        next_vel = self.sands[index].vel + self.sands[index].acc
        next_pos = self.sands[index].pos + next_vel
        next_pos = Vector(Point(int(next_pos.point.x), int(next_pos.point.y)))

        is_between: List[Sand] = []
        for other in self.sands:
            if self.sands[index] is not other:
                if (self.sands[index].pos.point.y < other.pos.point.y <= next_pos.point.y and
                        self.sands[index].pos.point.x == other.pos.point.x):
                    is_between.append(other)

        if len(is_between) > 0:
            lowest_y = self.grid[1]
            for each in is_between:
                if lowest_y > each.pos.point.y:
                    lowest_y = each.pos.point.y

            self.sands[index].is_falling = False
            self.sands[index].pos.point.y = int(lowest_y - 1)
            return

        if next_pos.point.y >= self.grid[1]:
            self.sands[index].is_falling = False
            self.sands[index].pos.point.y = int(self.grid[1]) - 1
            return

        self.sands[index].is_falling = True
