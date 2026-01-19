"""Module containing the state to menu options and actions mapping."""

from typing import List
from controller.utils.game_state import GameState

def get_options_from_state(state: "GameState") -> "List[str]":
    """Returns a list of button labels from the given state.
    
    Positional arguments:  
     - `state`: the current game state.
     
    Return:  
     - A list of text button labels."""
    return ["Start Game", "Quit"] if state == GameState.MAIN_MENU \
        else ["Resume Game", "Main Menu"] if state == GameState.PAUSE_MENU \
        else ["Game"] if state == GameState.LEVEL_TRANSITION \
        else [state.name]

def get_actions_from_state(state: "GameState") -> "List[GameState]":
    """Returns a list of destination game states from the given state.
    
    Positional arguments:  
     - `state`: the current game state.
     
    Return:  
     - A list of `GameState` directing all possible menu selections."""
    return [GameState.LEVEL_TRANSITION, GameState.QUITTING] if state == GameState.MAIN_MENU \
        else [GameState.GAME, GameState.MAIN_MENU] if state == GameState.PAUSE_MENU \
        else [GameState.GAME] if state == GameState.LEVEL_TRANSITION \
        else [state]
