"""Module containing the non-playing entity implementation."""

from typing import Tuple
from pygame import Rect
from constant import VISUAL_ASSETS_FOLDER, CHARACTER_ASSETS_FOLDER, ANIMATION_DEPTH, \
    VISUAL_ASSETS_EXTENSION

class Entity():
    """Implementation for all non-playing game entities."""
    
    def __init__(self, pos: "Tuple[float, float]", size: "Tuple[float, float]",
                 name: "str") -> "None":
        """Instantiates a non-playing game entity.
        
        Positional arguments:  
         - `pos`: the coordinates of the top-left corner of the entity's hitbox \
            when spawned.  
         - `size`: the dimension of the entity's hitbox.  
         - `name`: the entity's name, useful for retrieving the proper texture."""
        self._hitbox: "Rect" = Rect(pos, size)
        self._asset_base_name: "str" = VISUAL_ASSETS_FOLDER + CHARACTER_ASSETS_FOLDER + name
        self._frame_num: "int" = 0

    def is_colliding(self, hitbox: "Rect") -> "bool":
        """Checks for collision with a given hitbox.
        
        Positional arguments:  
         - `hitbox`: the hitbox to be checked for collision.
        
        Return:  
         - `True` if the two hitboxes collide, `False` otherwise."""
        return self._hitbox.colliderect(hitbox)

    def get_resource_name(self) -> "str":
        """Getter for the proper texture name.
        
        Return:  
         - A string identifier for the next proper resource to be shown on screen."""
        self._frame_num = self._frame_num + 1 % ANIMATION_DEPTH
        return self._asset_base_name + str(self._frame_num) + VISUAL_ASSETS_EXTENSION
