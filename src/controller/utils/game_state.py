"""Module for enumerating all possible game states."""

from enum import Enum

class GameState(Enum):
    """Enumerative type listing all possible game states."""
    MAIN_MENU = 0
    GAME = 1
    LEVEL_TRANSITION = 2
    DIALOGUE = 3
    PAUSE_MENU = 4
    ENDING = 5
    QUITTING = 6
