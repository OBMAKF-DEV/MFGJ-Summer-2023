from source.map import Tile, Item, Container
from source.constants.map_icons import MapIcons, TILE_DATA
from source.config.load_config import load_config
import pygame


class MapRenderer:
    def __init__(self, game, map_file):
        self.game = game
        self.map_file = map_file
        self.camera = [1, 1]
        self.tiles = []
        self.load()
    
    def load(self):
        with open(self.map_file, 'r', encoding='utf-8') as file:
            for y, row in enumerate(file.readlines()):
                _list = []
                for x, icon in enumerate(row.strip()):
                    _icon = MapIcons.items[icon]
                    _format = TILE_DATA[_icon]['format']
                    passable = TILE_DATA[_icon]['passable']
                    interactive = TILE_DATA[_icon]['interactable']
                    _list.append(Tile(
                        passable=passable,
                        interactable=interactive,
                        texture=f"resources/images/map_tiles/{_icon}.{TILE_DATA[_icon]['format']}")
                    )
                self.tiles.append(_list)
    
    def render(self):
        for y, row in enumerate(self.tiles):
            for x, tile in enumerate(row):
                SCALE = load_config("scale") * 2
                if self.game.player.coordinates == (x, y):
                    image = pygame.transform.scale(
                    pygame.image.load(f"resources/images/map_tiles/player_icon.png"),
                    (SCALE, SCALE))
                else:
                    image = pygame.transform.scale(
                        pygame.image.load(tile.texture),
                        (SCALE, SCALE))
                rect = pygame.Rect(
                    x * int(SCALE),
                    y * int(SCALE) - (self.camera[1] * int(SCALE)),
                    SCALE, SCALE)
                self.game.screen.blit(image, rect)
