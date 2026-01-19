"""Module containing the main game controller."""

from typing import List
from pygame import KEYDOWN
from pygame.key import ScancodeWrapper
from pygame.event import Event
from controller.progression.progression_controller import ProgressionController
from controller.utils.game_state import GameState
from controller.utils.action import Action
from model.world.world import World
from model.menu.menu import Menu
from view.menu.menu_view import render_menu
from constant import KEY_MAPPINGS

class MainController():
    """Main game controller implementation."""

    def __init__(self) -> "None":
        """Instantiates a main game controller."""
        self._game_state: "GameState" = GameState.MAIN_MENU
        self._menu: "Menu" = Menu(self._game_state)
        self._progression_controller: "ProgressionController" = ProgressionController()
        self._world: "World" = self._progression_controller.get_current_world()

    def update(self, events: "List[Event]", pressed_keys: "ScancodeWrapper", dt: "int") -> "bool":
        """Performs a single model update step.
        
        Positional arguments:  
         - `events`: a list of all events occurred since the last update step.
         - `pressed_keys`: all the keys that are currently being pressed.  
         - `dt`: the amount of time elapsed since last update step, in milliseconds.
        
        Return:  
         - `True` if the game should keep running, `False` otherwise."""
        updated: "bool" = False
        for key, action in KEY_MAPPINGS.items():
            if pressed_keys[key] and not updated:
                self._world.update(action, dt)
                updated = True

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
                            # TODO - handle interaction
                        case Action.QUIT:
                            self.change_state(
                                GameState.PAUSE_MENU if self._game_state == GameState.GAME
                                else GameState.GAME if self._game_state == GameState.PAUSE_MENU
                                else GameState.QUITTING if self._game_state == GameState.MAIN_MENU
                                else self._game_state
                            )
                except KeyError:
                    pass

        return self._game_state != GameState.QUITTING

    def render_world(self) -> "None":
        """Renders the next frame."""
        match self._game_state:
            case menu_state if menu_state in [GameState.MAIN_MENU, GameState.PAUSE_MENU]:
                render_menu(self._menu.get_options(), self._menu.get_selected())

    def change_state(self, dest_state: GameState) -> "None":
        """Changes the game state.
        
        Positional arguments:  
         - `dest_state`: the state to which the game should switch."""
        print(f"Going to state {dest_state}")
        if self._game_state != dest_state:
            self._game_state = dest_state
            self._menu = Menu(self._game_state)
        if self._game_state == GameState.LEVEL_TRANSITION:
            if self._progression_controller.can_progress():
                self._progression_controller.progress()
                self._world = self._progression_controller.get_current_world()
            else:
                print("Cannot progress")
                self.change_state(GameState.ENDING)
