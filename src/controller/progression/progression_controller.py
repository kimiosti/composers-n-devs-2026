"""Module containing the game progression controller implementation."""

from os.path import exists
from typing import List
from model.world.world import World
from model.world.player import Player
from model.world.entity import Entity
from controller.progression.parsing_utils import parse_direction, parse_game_state

class ProgressionController():
    """Implementation for the game progression controller."""

    def __init__(self) -> "None":
        """Instantiates and sets up a game progression controller."""
        self._cur_level = 0
        self._world = World(
            (0,0),
            [],
            Player((0,0), (0,0), "", parse_direction(""), 0, parse_game_state("")),
            ""
        )

    def can_progress(self) -> "bool":
        """Checks if the game can progress or if it's over.
        
        Return:  
         - `True` if there are levels to be played yet, `False` otherwise."""
        return exists(f"src/resources/levels/{self._cur_level + 1}/")

    def get_level_intro(self) -> "List[str]":
        """Getter for the level introductory text.
        
        Return:  
         - A list of strings, the first of which is the level title. Each other \
            string is a row of the introductory text to be shown."""
        with open(f"src/resources/levels/{self._cur_level}/intro", encoding="utf-8") as f:
            return f.readlines()

    def get_current_world(self) -> "World":
        """Getter for the current game world.
        
        Return:  
         - The current game world."""
        return self._world

    def progress(self) -> "None":
        """Progresses to the following level."""
        self._cur_level += 1
        player: "Player"
        entities: "List[Entity]" = []

        with open(
            f"src/resources/levels/{self._cur_level}/player",
            encoding="utf-8"
        ) as player_file:
            lines = player_file.readlines()
        player = Player(
            (float(lines[0][:-1]), float(lines[1][:-1])),
            (float(lines[2][:-1]), float(lines[3][:-1])),
            lines[4][:-1],
            parse_direction(lines[5][:-1]),
            int(lines[6][:-1]),
            parse_game_state(lines[7][:-1])
        )

        i: "int" = 1
        while exists(f"src/resources/levels/{self._cur_level}/entities/{i}"):
            with open(
                f"src/resources/levels/{self._cur_level}/entities/{i}",
                encoding="utf-8"
            ) as entity_file:
                lines = entity_file.readlines()
            entities.append(Entity(
                (float(lines[0][:-1]), float(lines[1][:-1])),
                (float(lines[2][:-1]), float(lines[3][:-1])),
                lines[4][:-1],
                parse_direction(lines[5][:-1]),
                int(lines[6][:-1]),
                parse_game_state(lines[7][:-1])
            ))
            i += 1

        with open(
            f"src/resources/levels/{self._cur_level}/world",
            encoding="utf-8"
        ) as world_file:
            lines = world_file.readlines()
        self._world = World(
            (int(lines[0][:-1]), int(lines[1][:-1])),
            entities,
            player,
            lines[2][:-1]
        )
