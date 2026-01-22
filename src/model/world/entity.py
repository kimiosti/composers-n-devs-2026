"""Module containing the non-playing entity implementation."""

from typing import Tuple
from pygame import Rect
from controller.utils.game_state import GameState
from model.world.direction import Direction
from constant import VISUAL_ASSETS_FOLDER, CHARACTER_ASSETS_FOLDER, ANIMATION_DEPTH, \
    VISUAL_ASSETS_EXTENSION, get_direction_asset_postfix

class Entity():
    """Implementation for all non-playing game entities."""

    def __init__(self, pos: "Tuple[float, float]", size: "Tuple[float, float]",
                 name: "str", direction: "Direction", game_id: "int",
                 destination_state: "GameState") -> "None":
        """Instantiates a non-playing game entity.
        
        Positional arguments:  
         - `pos`: the coordinates of the top-left corner of the entity's hitbox \
            when spawned.  
         - `size`: the dimension of the entity's hitbox.  
         - `name`: the entity's name, useful for retrieving the proper visual asset.
         - `direction`: the direction towards which the entity is facing.
         - `game_id`: the entity's in-game identifier.
         - `destination_state`: the game state to which a successful player \
            interaction should lead."""
        self._hitbox: "Rect" = Rect(pos, size)
        self._name: "str" = name
        self._frame_num: "int" = 0
        self._direction = direction
        self._game_id = game_id
        self._destination_state = destination_state

    def is_colliding(self, hitbox: "Rect") -> "bool":
        """Checks for collision with a given hitbox.
        
        Positional arguments:  
         - `hitbox`: the hitbox to be checked for collision.
        
        Return:  
         - `True` if the two hitboxes collide, `False` otherwise."""
        return self._hitbox.colliderect(hitbox)

    def progress_animation(self) -> "None":
        """Progresses the animation, referring to the next frame's resource."""
        self._frame_num = (self._frame_num + 1) % ANIMATION_DEPTH

    def get_resource_name(self) -> "str":
        """Getter for the proper visual asset name.
        
        Return:  
         - A string identifier for the next proper resource to be shown on screen."""
        return VISUAL_ASSETS_FOLDER + CHARACTER_ASSETS_FOLDER + self._name \
            + get_direction_asset_postfix(self._direction) + str(self._frame_num) \
            + VISUAL_ASSETS_EXTENSION

    def get_hitbox(self) -> "Rect":
        """Getter for the entity's hitbox.
        
        Return:
         - The entity's hitbox, describing its position and size."""
        return Rect(self._hitbox)

    def get_game_id(self) -> "int":
        """Getter for the entity's in-game identifier.
        
        Return:  
         - An integer that uniquely represents the entity in the game."""
        return self._game_id

    def get_destination_state(self) -> "GameState":
        """Getter for the interaction destination state.
        
        Return:  
         - The state to which the game goes on a successful interaction with the entity."""
        return self._destination_state
