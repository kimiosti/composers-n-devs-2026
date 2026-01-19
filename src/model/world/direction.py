"""Module for implementing an enumerative type listing all possible movement directions."""

from enum import Enum

class Direction(Enum):
    """Enumerative type listing all possible directions."""
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3
