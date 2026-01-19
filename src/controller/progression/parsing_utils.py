"""Module containing level design files parsing utilities."""

from model.world.direction import Direction
from controller.utils.game_state import GameState

def parse_game_state(text: "str") -> "GameState":
    """Parses a game state from a given text.
    
    Positional arguments:  
     - `text`: a string describing the desired game state.
     
    Return:  
     - The `GameState` described by the given string, or `GameState.GAME` \
        as a default value."""
    for state in GameState:
        if state.name == text:
            return state
    return GameState.GAME

def parse_direction(text: "str") -> "Direction":
    """Parses a direction from a given text.
    
    Positional arguments:  
     - `text`: a string describing the desired direction.
    
    Return:  
     - The `Direction` described by the given string, or `Direction.RIGHT` \
        as a default value."""
    for direction in Direction:
        if direction.name == text:
            return direction
    return Direction.RIGHT
