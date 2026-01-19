"""Module containing the implementation for the player-controlled game entities."""

from typing import Tuple
from pygame import Rect
from constant import PLAYER_SPEED
from model.world.direction import Direction
from model.world.entity import Entity

class Player(Entity):
    """Implementation for the player-controlled game entities."""

    def move(self, direction: "Direction", dt: "int") -> "Rect":
        """Computes the player's movement in the desired direction.
        
        Positional arguments:  
         - `direction`: the direction towards where the player should move.  
         - `dt`: the amount of time elapsed since the last world update step, in milliseconds.
        
        Return:  
         - The position the hitbox would occupy after its movement.
         
        Note that the game world coordinate system is left-handed. The origin is the top-left \
        corner of the map, with x increasing towards the right and y increasing towards the \
        bottom."""
        self._direction = direction
        return self._hitbox.move(
            PLAYER_SPEED * dt / 1000 if direction == Direction.RIGHT else
            - PLAYER_SPEED * dt / 1000 if direction == Direction.LEFT else 0,
            PLAYER_SPEED * dt / 1000 if direction == Direction.DOWN else
            - PLAYER_SPEED * dt / 1000 if direction == Direction.UP else 0
        )

    def move_to(self, pos: "Tuple[float, float]") -> "None":
        """Moves the player to a given position.
        
        Positional arguments:  
         - `pos`: the position where the player should be moved."""
        self._hitbox = Rect(pos, self._hitbox.size)
