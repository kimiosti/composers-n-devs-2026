"""Module enumerating all possible game actions."""

from enum import Enum

class Action(Enum):
    """Enumerative type listing all possible game actions."""
    QUIT = 0
    MOVE_UP = 1
    MOVE_DOWN = 2
    MOVE_RIGHT = 3
    MOVE_LEFT = 4
    INTERACT = 6
    # TODO - more actions for all dialogue options
