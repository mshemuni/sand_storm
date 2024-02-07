import sys
from random import randint
from typing import Tuple

from .world import World
from .colors import Colors
import pygame


class Window:
    def __init__(self, world: World, shape: Tuple[int, int] = (400, 400), tick: int = 24) -> None:
        self.world = world
        self.shape = shape
        self.tick = tick

        self.add = False
        pygame.init()
        self.screen = pygame.display.set_mode(self.shape)
        pygame.display.set_caption("Sand Storm")
        self.is_running = False
        self.clock = pygame.time.Clock()
        self.size = self.shape[0] // self.world.grid[0], self.shape[1] // self.world.grid[1]

    def start(self) -> None:
        self.is_running = True
        self.run()

    def run(self) -> None:
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.add = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.add = False

            if self.add:
                x, y = pygame.mouse.get_pos()

                self.world.add_sand(
                    int(x // self.size[0]) + randint(-2, 2),
                    int(y // self.size[1]) + randint(-2, 2)
                )

            self.screen.fill(Colors.WHITE)

            for it in range(len(self.world.sands) - 1, -1, -1):
                self.world.check_falling(it)
                self.world.check_drift(it)
                if self.world.sands[it].is_falling:
                    self.world.sands[it].apply_acceleration(self.world.G)
                    self.world.sands[it].move()

                pygame.draw.rect(
                    self.screen,
                    self.world.sands[it].color,
                    (
                        self.world.sands[it].pos.point.x * self.size[0],
                        self.world.sands[it].pos.point.y * self.size[1],
                        self.size[0],
                        self.size[1]
                    )
                )

                if self.world.sands[it].is_dead(self.world.grid):
                    del self.world.sands[it]
                    continue

            pygame.display.flip()
            self.clock.tick(self.tick)
        pygame.quit()
        sys.exit()
