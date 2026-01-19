"""Module containing the game world implementation."""

from typing import Tuple, List
from pygame import Rect
from constant import VISUAL_ASSETS_FOLDER, BACKGROUND_ASSETS_FOLDER, VISUAL_ASSETS_EXTENSION
from controller.utils.action import Action
from model.world.direction import Direction
from model.world.entity import Entity
from model.world.player import Player

class World():
    """Implementation for the game world."""

    def __init__(self, size: "Tuple[int, int]", entities: "List[Entity]",
                 player: "Player", name: "str") -> "None":
        """Instantiates a game world.
        
        Positional arguments:  
         - `size`: the world's dimensions along the two axes.  
         - `entities`: a list of all world entities.  
         - `player`: the player-controlled entity.  
         - `name`: the world's name, useful for retrieving visual assets."""
        self._map: "Rect" = Rect((0,0), size)
        self._entities: "List[Entity]" = entities
        self._player: "Player" = player
        self._name: "str" = name

    def update(self, action: "Action", dt: "int") -> "None":
        """Performs a single world update step.
        
        Positional arguments:  
         - `action`: the action demanded by the player.
         - `dt`: the amount of time elapsed since the last world update, \
            in milliseconds."""
        if action not in [Action.QUIT, Action.INTERACT]:
            moved_hitbox: "Rect" = self._player.move(
                Direction.RIGHT if action == Action.MOVE_RIGHT \
                    else Direction.LEFT if action == Action.MOVE_LEFT \
                    else Direction.DOWN if action == Action.MOVE_DOWN \
                    else Direction.UP,
                dt
            )

            can_move: "bool" = True
            for entity in self._entities:
                if entity.is_colliding(moved_hitbox):
                    can_move = False

            if can_move and self._map.contains(moved_hitbox):
                self._player.move_to((moved_hitbox.left, moved_hitbox.top))

    def interact(self) -> "None":
        """Performs an interaction, if possible."""
        #TODO - implement interaction

    def get_background(self) -> "Tuple[str, Tuple[float, float]]":
        """Getter for the background resource.
        
        Return:  
         - A tuple that associates the name of the resource as a string to a tuple \
            representing the map dimension in game coordinates."""
        return (
            VISUAL_ASSETS_FOLDER + BACKGROUND_ASSETS_FOLDER
                + self._name + VISUAL_ASSETS_EXTENSION,
            self._map.size
        )

    def get_sprites(self) -> "List[Tuple[str, Rect]]":
        """Getter for all the game sprites to be shown in the current frame.
        
        Return:  
         - A list of tuples that associates to each resource name its position \
            and size in game coordinates."""
        res: "List[Tuple[str, Rect]]" = []
        for entity in self._entities:
            res.append((
                entity.get_resource_name(),
                entity.get_hitbox()
            ))
        res.append((
            self._player.get_resource_name(),
            self._player.get_hitbox()
        ))
        return res
