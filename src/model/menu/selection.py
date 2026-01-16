"""Module containing a single selection wrapper."""

class Selection():
    """Implementation for a single menu selection."""

    def __init__(self, text: "str") -> "None":
        """Instantiates a single menu selection.
        
        Positional arguments:  
         - `text`: the text description to be shown in the menu button."""
        self._text: "str" = text
        self._selected: "bool" = False

    def select(self) -> "None":
        """Selects the option."""
        self._selected = True

    def deselect(self) -> "None":
        """Deselects the option."""
        self._selected = False

    def is_selected(self) -> "bool":
        """Checks wether the option is selected.
        
        Return:
         - `True` if the option is currently selected, `False` otherwise."""
        return self._selected

    def get_text(self) -> "str":
        """Retrieves the selection text.
        
        Return:  
         - The selection's string label."""
        return self._text
