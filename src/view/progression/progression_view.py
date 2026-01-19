"""Module containing the progression view implementation."""

from typing import List
from pygame.font import Font
from pygame.surface import Surface
from pygame import display as pg_display

def render_level_intro(text: "List[str]") -> "None":
    """Renders the level's introductory text.
    
    Positional arguments:  
     - `text`: a list of all lines of the level's introductory text."""
    title_font: "Font" = Font("src/resources/font/game-font.ttf", size=36)
    lines_font: "Font" = Font("src/resources/font/game-font.ttf", size=24)

    display: "Surface" = pg_display.get_surface()
    if display is None:
        display = pg_display.set_mode()

    display.fill((0,0,0))

    display_width, display_height = display.get_size()

    title: "str" = text[0]
    lines: "List[str]" = text[1:]

    title_surf: "Surface" = title_font.render(title[:-1], False, (255,255,255))

    display.blit(
        title_surf,
        (
            display_width / 4,
            display_height / 3 - title_surf.get_height()
        )
    )

    interline_space: "float" = 0.5
    for i in range(len(lines) - 1):
        line_surf: "Surface" = lines_font.render(lines[i][:-1], True, (255,255,255))
        display.blit(
            line_surf,
            (
                display_width / 4,
                display_height / 2 + (i * line_surf.get_height() * (1 + interline_space))
            )
        )
    
    line_surf: "Surface" = lines_font.render(lines[len(lines) - 1][:-1], True, (255,255,255))
    display.blit(
        line_surf,
        (
            display_width / 4 * 3 - line_surf.get_width(),
            display_height / 2 + (len(lines) - 1) * line_surf.get_height() * (1 + interline_space)
        )
    )

    pg_display.flip()
