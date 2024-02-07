from random import choice
from typing import Tuple


class Colors:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 0)
    MAGENTA = (255, 0, 255)
    CYAN = (0, 255, 255)

    @classmethod
    def random_color(cls) -> Tuple[int, int, int]:
        return choice([cls.RED, cls.GREEN, cls.WHITE, cls.BLACK, cls.YELLOW, cls.MAGENTA, cls.CYAN])

