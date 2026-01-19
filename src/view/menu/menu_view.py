"""Module containing the menu view's implementation."""

from math import floor
from typing import List, Tuple
from pygame import Surface
from pygame.font import Font
from pygame import display as pg_display

def render_menu(options: "List[str]", selected: "int") -> "None":
    """Renders and display the current menu selection.
    
    Positional arguments:  
     - `options`: the button labels for all menu options.  
     - `selected`: the index of the currently selected option."""
    menu_font: "Font" = Font("src/resources/font/game-font.ttf", size=36)

    display: "Surface" = pg_display.get_surface()
    if display is None:
        display = pg_display.set_mode()

    display.fill((0,0,0))

    display_width, display_height = display.get_size()

    max_size: "Tuple[int, int]" = (-1, -1)
    for option in options:
        max_size = (max(max_size[0], menu_font.size(option)[0]), max_size[1])
        max_size = (max_size[0], max(max_size[1], menu_font.size(option)[1]))

    max_size = (floor(max_size[0] * 1.3), floor(max_size[1] * 1.3))

    menu_width = max_size[0]
    menu_height = max_size[1] * len(options) + max_size[1] / 2 * (len(options) - 1)

    menu_surf = Surface((menu_width, menu_height))

    for i, option in enumerate(options):
        outer_surf = Surface(max_size)
        text_surf = menu_font.render(
            option,
            False,
            (255,255,0) if selected == i else (255,255,255)
        )

        outer_surf.blit(
            text_surf,
            (
                (outer_surf.get_width() - text_surf.get_width()) / 2,
                (outer_surf.get_height() - text_surf.get_height()) / 2
            )
        )

        menu_surf.blit(
            outer_surf,
            (0, i * (max_size[1] * 1.5))
        )

    display.blit(
        menu_surf,
        (
            (display_width - menu_surf.get_width()) / 2,
            (display_height - menu_surf.get_height()) / 2
        )
    )

    pg_display.flip()
