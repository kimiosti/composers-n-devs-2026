"""Module containing the main game controller."""

import pygame
from controller.utils.game_state import GameState
from controller.utils.action import Action
from model.menu.menu import Menu
from constant import KEY_MAPPINGS

class MainController():
    """Main game controller implementation."""

    def __init__(self) -> "None":
        """Instantiates a main game controller."""
        self._game_state: "GameState" = GameState.MAIN_MENU
        self._menu: "Menu" = Menu(self._game_state)
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
                match action:
                    case Action.MOVE_UP:
                        self._menu.move_up()
                        # TODO - move inside game world
                    case Action.MOVE_DOWN:
                        self._menu.move_down()
                        # TODO - move inside game world
                    case Action.MOVE_RIGHT:
                        # TODO - move inside game world
                        pass
                    case Action.MOVE_LEFT:
                        # TODO - move inside game world
                        pass
                    case Action.INTERACT:
                        self.change_state(self._menu.enter_selection())
                        # TODO - handle interactions in the game world
                    case Action.QUIT:
                        match self._game_state:
                            case GameState.GAME:
                                self.change_state(GameState.PAUSE_MENU)
                            case GameState.PAUSE_MENU:
                                self.change_state(GameState.GAME)
                            case GameState.MAIN_MENU:
                                self.change_state(GameState.QUITTING)

        #TODO - handle update step.

        return self._game_state != GameState.QUITTING

    def render_world(self) -> "None":
        """Renders the next frame."""
        #TODO - handle rendering.

    def change_state(self, dest_state: GameState) -> "None":
        """Changes the game state.
        
        Positional arguments:  
         - `dest_state`: the state to which the game should switch."""
        if self._game_state != dest_state:
            self._game_state = dest_state
            self._menu = Menu(self._game_state)
