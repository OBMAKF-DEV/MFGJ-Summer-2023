from source.container import Container
from source.items import Item
from typing import Type

Game: object = Type['Game']


class Tile:
    """Contains the texture image and interactive properties for an area in the map.
    
    Args:
        passable (bool): Whether the player can pass over the tile.
        interactable (bool): Whether the player can interact with the tile.
        _object (object | None): Any object that is over the map tile.
        texture (str | bytes): The texture image to render over the map tile.
    """
    def __init__(self, passable: bool = True, interactable: bool = False, _object: object = None, texture=None):
        self.object = _object
        self.passable = passable
        self.is_interactable = interactable
        self.texture = texture


class Map:
    """Loads the environment from specified map file.
    
    Attributes:
        tiles_icons (list[list[str]): A nested list containing icons for each coordinate.
        tiles (list[list[Tile]): A nested list containing `Tile` instances for each coordinate.
    """
    PLAYER_ICON = "X"
    CONTAINER = "+"
    WALL = "#"
    FLOOR = "-"
    
    tile_icons: list[list[str]] = []
    tiles: list[list[Tile]] = []
    
    def __init__(self, game: Game, map_file: str | bytes):
        """Initializes a new `Map` instance.
        
        Loads the data from the `map_file` and stores it to `tile_icons`.
        
        Args:
            game (Game): The main game object.
            map_file (str | bytes): The map file to load the environment data from.
        """
        with open(map_file, 'r') as file:
            for y, line in enumerate(file.readlines()):
                row = []
                for x, marker in enumerate(line):
                    row.append(marker)
                self.tile_icons.append(row)
        self.game = game
    
    def render(self):
        """Renders the environment from `tile_icons`.
        
        Renders the players icon over the tile.
        """
        player_x, player_y = self.game.player.coordinates
        _tiles = []
        for y, row in enumerate(self.tile_icons):
            line = ""
            _row = []
            for x, tile in enumerate(row):
                if y == player_y and x == player_x:
                    line += f" {self.PLAYER_ICON} "
                    _row.append(Tile(_object=self.game.player))
                    continue
                match tile:
                    case self.CONTAINER:
                        line += f"[{self.CONTAINER}]"
                        _row.append(Tile(False, True, Container([Item("apple")])))
                        continue
                    case self.WALL:
                        line += f"[{self.WALL}]"
                        _row.append(Tile(False, False))
                        continue
                    case self.FLOOR:
                        line += f"   "
                        _row.append(Tile())
                        continue
            _tiles.append(_row)
            print(line)
        self.tiles = _tiles
