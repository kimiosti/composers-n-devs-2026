"""Module containing the non-playing entity implementation."""

from typing import Tuple
from pygame import Rect
from model.world.direction import Direction
from constant import VISUAL_ASSETS_FOLDER, CHARACTER_ASSETS_FOLDER, ANIMATION_DEPTH, \
    VISUAL_ASSETS_EXTENSION, get_direction_asset_postfix

class Entity():
    """Implementation for all non-playing game entities."""

    def __init__(self, pos: "Tuple[float, float]", size: "Tuple[float, float]",
                 name: "str", direction: "Direction") -> "None":
        """Instantiates a non-playing game entity.
        
        Positional arguments:  
         - `pos`: the coordinates of the top-left corner of the entity's hitbox \
            when spawned.  
         - `size`: the dimension of the entity's hitbox.  
         - `name`: the entity's name, useful for retrieving the proper visual asset.
         - `direction`: the direction towards which the entity is facing."""
        self._hitbox: "Rect" = Rect(pos, size)
        self._name: "str" = name
        self._frame_num: "int" = 0
        self._direction = direction

    def is_colliding(self, hitbox: "Rect") -> "bool":
        """Checks for collision with a given hitbox.
        
        Positional arguments:  
         - `hitbox`: the hitbox to be checked for collision.
        
        Return:  
         - `True` if the two hitboxes collide, `False` otherwise."""
        return self._hitbox.colliderect(hitbox)

    def get_resource_name(self) -> "str":
        """Getter for the proper visual asset name.
        
        Return:  
         - A string identifier for the next proper resource to be shown on screen."""
        self._frame_num = self._frame_num + 1 % ANIMATION_DEPTH
        return VISUAL_ASSETS_FOLDER + CHARACTER_ASSETS_FOLDER + self._name \
            + get_direction_asset_postfix(self._direction) + str(self._frame_num) \
            + VISUAL_ASSETS_EXTENSION

    def get_hitbox(self) -> "Rect":
        """Getter for the entity's hitbox.
        
        Return:
         - The entity's hitbox, describing its position and size."""
        return Rect(self._hitbox)
