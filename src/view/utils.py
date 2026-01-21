"""Module containing generic view utilities."""

from pygame import display as pg_display
from pygame.surface import Surface
from pygame.display import flip

def get_clear_display() -> "Surface":
    """Initializes the screen (if necessary), cleans up the previous frame \
        and returns the current display surface.
        
    Return:  
     - A surface representing the current display."""
    display: "Surface" = pg_display.get_surface()
    if display is None:
        display = pg_display.set_mode()

    display.fill((0,0,0))

    return display

def flip_screen() -> "None":
    """Flips the screen, showing the next frame."""
    flip()
