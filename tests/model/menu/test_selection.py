"""Module for Selection implementation testing."""

from model.menu.selection import Selection

SAMPLE_TEXT: "str" = "Sample"

class TestSelection():
    """Class for Selection implementation testing."""
    def setup_method(self) -> "None":
        """General setup to run before all test methods."""
        self._selection = Selection(SAMPLE_TEXT)

    def test_select(self) -> "None":
        """Tests the select method of the Selection class."""
        self._selection.select()
        assert self._selection.is_selected()

    def test_deselect(self) -> "None":
        """Tests the deselect method of the Selection class."""
        self._selection.select()
        self._selection.deselect()
        assert not self._selection.is_selected()

    def test_get_text(self) -> "None":
        """Tests the get_text method of the selection class."""
        assert self._selection.get_text() == SAMPLE_TEXT
