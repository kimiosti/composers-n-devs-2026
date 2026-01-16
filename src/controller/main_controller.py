"""Module containing the main game controller."""

import pygame
from controller.utils.game_state import GameState
from controller.utils.action import Action
from constant import KEY_MAPPINGS

class MainController():
    """Main game controller implementation."""

    def __init__(self) -> "None":
        """Instantiates a main game controller."""
        self._game_state: "GameState" = GameState.MAIN_MENU
        self._world: "None" = None # TODO - instantiate game world.
        self._level_number: "int" = 0 # TODO - introduce level progression controller ?

    def update(self, pressed_keys: "pygame.key.ScancodeWrapper", dt: "int") -> "bool":
        """Performs a single model update step.
        
        Positional arguments:  
         - `pressed_keys`: all the keys that are currently being pressed.  
         - `dt`: the amount of time elapsed since last update step, in milliseconds.
        
        Return:  
         - `True` if the game should keep running, `False` otherwise."""
        for key, action in KEY_MAPPINGS.items():
            if pressed_keys[key]:
                if action == Action.QUIT:
                    return False

        #TODO - handle update step.

        return True

    def render_world(self) -> "None":
        """Renders the next frame."""
        #TODO - handle rendering.
