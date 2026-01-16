"""Module containing the generic menu implementation."""

from typing import List
from model.menu.selection import Selection
from model.menu import state_mappings
from controller.utils.game_state import GameState

class Menu():
    """Menu implementation."""

    def __init__(self, game_state: "GameState") -> "None":
        """Instantiates a menu.
        
        Positional arguments:  
         - `game_state`: the current game state."""
        self._selected_idx: "int" = 0
        self._options: "List[Selection]" = [
            Selection(option) for option in state_mappings.get_options_from_state(game_state)
        ]
        self._actions: "List[GameState]" = state_mappings.get_actions_from_state(game_state)
        self._option_num: "int" = len(self._options)
        self._options[self._selected_idx].select()

    def move_up(self) -> "None":
        """Moves up one selection in the menu."""
        self._options[self._selected_idx].deselect()
        self._selected_idx = (self._selected_idx + self._option_num - 1) % self._option_num
        self._options[self._selected_idx].select()

    def move_down(self) -> "None":
        """Moves down one selection in the menu."""
        self._options[self._selected_idx].deselect()
        self._selected_idx = (self._selected_idx + 1) % self._option_num
        self._options[self._selected_idx].select()

    def enter_selection(self) -> "GameState":
        """Enters the desired selection.
        
        Return:
         - the `GameState` to which the current selection leads."""
        return self._actions[self._selected_idx]

    def get_options(self) -> "List[str]":
        """Getter for all option labels.
        
        Return:
         - A `List` of string, each describing a choice option's label."""
        return [option.get_text() for option in self._options]

    def get_selected(self) -> "int":
        """Getter for the index of the currently selected option.
        
        Return:
         - The index of the currently selected option."""
        return self._selected_idx
