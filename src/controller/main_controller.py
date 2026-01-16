"""Module containing the main game controller."""

from typing import List
from pygame import KEYDOWN
from pygame.key import ScancodeWrapper
from pygame.event import Event
from controller.utils.game_state import GameState
from controller.utils.action import Action
from model.menu.menu import Menu
from view.menu.menu_view import MenuView
from constant import KEY_MAPPINGS

class MainController():
    """Main game controller implementation."""

    def __init__(self) -> "None":
        """Instantiates a main game controller."""
        self._game_state: "GameState" = GameState.MAIN_MENU
        self._menu: "Menu" = Menu(self._game_state)
        self._world: "None" = None # TODO - instantiate game world.
        self._level_number: "int" = 0 # TODO - introduce level progression controller ?

    def update(self, events: "List[Event]", pressed_keys: "ScancodeWrapper", dt: "int") -> "bool":
        """Performs a single model update step.
        
        Positional arguments:  
         - `events`: a list of all events occurred since the last update step.
         - `pressed_keys`: all the keys that are currently being pressed.  
         - `dt`: the amount of time elapsed since last update step, in milliseconds.
        
        Return:  
         - `True` if the game should keep running, `False` otherwise."""
        for key, action in KEY_MAPPINGS.items():
            if pressed_keys[key]:
                match action:
                    case _:
                        # TODO - handle in-world movement
                        pass

        for event in events:
            if event.type == KEYDOWN:
                try:
                    match KEY_MAPPINGS[event.key]:
                        case Action.MOVE_UP:
                            self._menu.move_up()
                        case Action.MOVE_DOWN:
                            self._menu.move_down()
                        case Action.INTERACT:
                            self.change_state(self._menu.enter_selection())
                        case Action.QUIT:
                            self.change_state(
                                GameState.PAUSE_MENU if self._game_state == GameState.GAME
                                else GameState.GAME if self._game_state == GameState.PAUSE_MENU
                                else GameState.QUITTING if self._game_state == GameState.MAIN_MENU
                                else self._game_state
                            )
                except KeyError:
                    pass

        #TODO - handle update step.

        return self._game_state != GameState.QUITTING

    def render_world(self) -> "None":
        """Renders the next frame."""
        match self._game_state:
            case menu_state if menu_state in [GameState.MAIN_MENU, GameState.PAUSE_MENU]:
                MenuView().render_menu(self._menu.get_options(), self._menu.get_selected())

    def change_state(self, dest_state: GameState) -> "None":
        """Changes the game state.
        
        Positional arguments:  
         - `dest_state`: the state to which the game should switch."""
        if self._game_state != dest_state:
            self._game_state = dest_state
            self._menu = Menu(self._game_state)
