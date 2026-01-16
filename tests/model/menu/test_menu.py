"""Module for Menu class testing."""

import random
from model.menu.menu import Menu
from controller.utils.game_state import GameState

class TestMenu():
    """Class for the Menu class testing."""
    def setup_method(self) -> "None":
        """Setup to be run before all test methods."""
        self._menus = {
            state: Menu(state) for state in GameState
        }

    def test_move_up(self) -> "None":
        """Test for the move_up method in the Menu class."""
        self._menus[GameState.MAIN_MENU].move_up()
        assert self._menus[GameState.MAIN_MENU].enter_selection() == GameState.QUITTING
        self._menus[GameState.MAIN_MENU].move_up()
        assert self._menus[GameState.MAIN_MENU].enter_selection() == GameState.LEVEL_TRANSITION

        for _ in range(99):
            self._menus[GameState.PAUSE_MENU].move_up()
        assert self._menus[GameState.PAUSE_MENU].enter_selection() == GameState.MAIN_MENU

        self._menus[GameState.PAUSE_MENU].move_up()
        assert self._menus[GameState.PAUSE_MENU].enter_selection() == GameState.GAME

        for state in GameState:
            if state not in [GameState.MAIN_MENU, GameState.PAUSE_MENU]:
                for _ in range(random.randint(15, 255)):
                    self._menus[state].move_up()
                assert self._menus[state].enter_selection() == state

    def test_move_down(self) -> "None":
        """Test for the move_down method in the Menu class."""
        self._menus[GameState.MAIN_MENU].move_down()
        assert self._menus[GameState.MAIN_MENU].enter_selection() == GameState.QUITTING
        self._menus[GameState.MAIN_MENU].move_down()
        assert self._menus[GameState.MAIN_MENU].enter_selection() == GameState.LEVEL_TRANSITION

        for _ in range(99):
            self._menus[GameState.PAUSE_MENU].move_down()
        assert self._menus[GameState.PAUSE_MENU].enter_selection() == GameState.MAIN_MENU

        self._menus[GameState.PAUSE_MENU].move_down()
        assert self._menus[GameState.PAUSE_MENU].enter_selection() == GameState.GAME

        for state in GameState:
            if state not in [GameState.MAIN_MENU, GameState.PAUSE_MENU]:
                for _ in range(random.randint(15, 255)):
                    self._menus[state].move_down()
                assert self._menus[state].enter_selection() == state
