"""Module containing the game view implementation."""

from typing import Tuple, List
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.transform import smoothscale
from pygame.image import load as load_img
from view.utils import get_clear_display
from constant import VISIBLE_WIDTH, VISIBLE_HEIGHT

def render_game_map(background: "Tuple[str, Rect]", player: "Tuple[str, Rect]",
                    sprites: "List[str, Rect]") -> "None":
    """Renders the game world for a single frame.
    
    Positional arguments:  
     - `background`: a tuple representing the background's resource name and its \
        size and position in game coordinates.
     - `player`: a tuple representing the player's resource name and its size and \
        position in game coordinates.
     - `sprites`: a list of tuples, each representing an entity's resource name and \
        its size and position in game coordinates."""
    display: "Surface" = get_clear_display()
    display_width, display_height = display.get_size()

    map_surf_width = display_width / 9 * 7
    map_surf_height = display_height / 9 * 7
    map_surf: "Surface" = Surface((map_surf_width, map_surf_height))

    background_surf = smoothscale(
        load_img(background[0]),
        (
            background[1].width / VISIBLE_WIDTH * map_surf_width,
            background[1].height / VISIBLE_HEIGHT * map_surf_height
        )
    ).convert()

    background_width, background_height = background_surf.get_size()

    blittable_sprites: "List[Tuple[str, Rect]]" = sprites + [player]
    for res_name, hitbox in blittable_sprites:
        background_surf.blit(
            smoothscale(
                load_img(res_name),
                (
                    hitbox.width / background[1].width * background_width,
                    hitbox.height / background[1].height * background_height
                )
            ).convert_alpha(),
            (
                hitbox.left / background[1].width * background_width,
                hitbox.top / background[1].height * background_height
            )
        )
    
    visible_left_edge = 0 if player[1].centerx < VISIBLE_WIDTH / 2 \
        else background[1].width - VISIBLE_WIDTH \
        if player[1].centerx > background[1].width - (VISIBLE_WIDTH / 2) \
        else player[1].centerx - (VISIBLE_WIDTH / 2)
    
    visible_top_edge = 0 if player[1].centery < VISIBLE_HEIGHT / 2 \
        else background[1].height - VISIBLE_HEIGHT \
        if player[1].centery > background[1].height - (VISIBLE_HEIGHT / 2) \
        else player[1].centery - (VISIBLE_HEIGHT / 2)
    
    map_surf.blit(
        background_surf,
        (
            - visible_left_edge / background[1].width * background_width,
            - visible_top_edge / background[1].height * background_height
        )
    )

    display.blit(
        map_surf,
        (
            (display_width - map_surf_width) / 2,
            (display_height - map_surf_height) / 2
        )
    )
