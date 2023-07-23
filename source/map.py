from source.config.load_config import load_config
from source.config.properties import get_window_size
from source.container import Container
from source.constants.map_icons import MapIcons
from source.items import Item
from typing import Type
import math

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
        self.size = (load_config('scale'))


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
    
    objects = []
    tile_icons: list[list[str]] = []
    tiles: list[list[Tile]] = []
    
    def __init__(self, game: Game, map_file: str | bytes):
        """Initializes a new `Map` instance.
        
        Loads the data from the `map_file` and stores it to `tile_icons`.
        
        Args:
            game (Game): The main game object.
            map_file (str | bytes): The map file to load the environment data from.
        """
        self.camera: list[int] = [0, 0]
        self.file_name = map_file
        self.player_exit_position = None
        
        with open(self.file_name, 'r') as file:
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
        self.determine_camera()
        player_x, player_y = self.game.player.coordinates
        _tiles = []
        for y, row in enumerate(self.tile_icons):
            line = ""
            _row = []
            for x, tile in enumerate(row):
                if y == player_y and x == player_x:
                    line += f" {self.PLAYER_ICON} "
                    image = '../MFGJ-Summer-2023/resources/player_icon.png'
                    _row.append(Tile(_object=self.game.player, texture=image))
                    rect = pygame.Rect(
                        x * load_config('scale'),
                        y * load_config('scale') - (self.camera[1] * load_config('scale')),
                        load_config('scale'),
                        load_config('scale'))
                    self.game.screen.blit(image, rect)
                    continue
                
                match tile:
                    case self.CONTAINER:
                        line += f"[{self.CONTAINER}]"
                        image = '../MFGJ-Summer-2023/resources/container.png'
                        _row.append(Tile(False, True, Container([Item("apple")]), texture=image))
                        rect = pygame.Rect(
                            x * load_config('scale'),
                            y * load_config('scale') - (self.camera[1] * load_config('scale')),
                            load_config('scale'),
                            load_config('scale'))
                        self.game.screen.blit(image, rect)
                        continue
                    
                    case self.WALL:
                        line += f"[{self.WALL}]"
                        image = '../MFGJ-Summer-2023/resources/wall.jpg'
                        _row.append(Tile(False, False, texture=image))
                        rect = pygame.Rect(
                            x * load_config('scale'),
                            y * load_config('scale') - (self.camera[1] * load_config('scale')),
                            load_config('scale'),
                            load_config('scale'))
                        self.game.screen.blit(image, rect)
                        continue
                    
                    case self.FLOOR:
                        line += f"   "
                        image = '../MFGJ-Summer-2023/resources/floor.jpg'
                        _row.append(Tile(texture=image))
                        rect = pygame.Rect(
                            x * load_config('scale'),
                            y * load_config('scale') - (self.camera[1] * load_config('scale')),
                            load_config('scale'),
                            load_config('scale'))
                        self.game.screen.blit(image, rect)
            
            _tiles.append(_row)
            print(line)
        
        self.tiles = _tiles
    
    def determine_camera(self):
        _screen_width, _screen_height = get_window_size()
        max_y_position = int(len(self.tile_icons) - _screen_height / load_config('scale'))
        y_position = self.game.player.coordinates[1] - math.ceil(
            round(_screen_height / load_config('scale') / 2))
        
        if max_y_position >= y_position >= 0:
            self.camera[1] = y_position
        elif y_position < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = max_y_position
