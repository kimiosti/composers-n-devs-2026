"""Module containing all game constants."""

from typing import Dict
import pygame
from controller.utils.action import Action
from model.world.direction import Direction

KEY_MAPPINGS: "Dict[int, Action]" = {
    pygame.K_ESCAPE: Action.QUIT,
    pygame.K_UP: Action.MOVE_UP,
    pygame.K_DOWN: Action.MOVE_DOWN,
    pygame.K_RIGHT: Action.MOVE_RIGHT,
    pygame.K_LEFT: Action.MOVE_LEFT,
    pygame.K_x: Action.INTERACT
}

PLAYER_SPEED: "float" = 100

VISIBLE_WIDTH: "int" = 1000

VISIBLE_HEIGHT: "int" = 650

VISUAL_ASSETS_FOLDER: "str" = "src/resources/assets/"

VISUAL_ASSETS_EXTENSION: "str" = ".png"

CHARACTER_ASSETS_FOLDER: "str" = "characters/"

BACKGROUND_ASSETS_FOLDER: "str" = "backgrounds/"

ANIMATION_DEPTH: "int" = 2

def get_direction_asset_postfix(direction: "Direction") -> "str":
    """Computes the asset postfix given the entity's movement direction.
    
    Positional arguments:  
     - `direction`: the direction of the entity's movement.
    
    Return:  
     - A string postfix to be added to the asset name."""
    return f"_{direction.name.lower()}_"
