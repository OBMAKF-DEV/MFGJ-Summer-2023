import pygame.event

from source.items import Item
from typing import Type

Game: object = Type['Game']


class Player:
    """The main player class.
    
    Attributes:
        game (Game): The main game class.
        coordinates (tuple[int, int]): The players location coordinates `(x, y)`
        inventory (list[Item]): The players inventory -- A list containing `Item`s.
    """
    inventory: list[Item] = []
    
    def __init__(self, game: Game, coordinates: tuple[int, int] = (1, 1)):
        self.game = game
        self.coordinates = coordinates
    
    def open_inventory(self):
        """Opens the players inventory."""
        print("Inventory:")
        if len(self.inventory) == 0:
            print("\t- Empty")
        else:
            for item in self.inventory:
                print(f"\t- {item.name}")
        _ = input()
        # Todo. create functionality for picking up / dropping items.
    
    def scan_surrounding_tiles(self) -> list:
        """Get the tiles from surrounding the player (+ - xy coordinates)
        
        Return:
            list[tuple[int, int]
        """
        _x, _y = self.coordinates
        print(_x, _y)
        try:
            north = self.game.map.tiles[_y-1][_x],
        except IndexError as exc:
            return
        try:
            south = self.game.map.tiles[_y+1][_x],
        except IndexError as exc:
            return
        try:
            west = self.game.map.tiles[_y][_x-1],
        except IndexError as exc:
            return
        try:
            east = self.game.map.tiles[_y][_x+1],
        except IndexError as exc:
            return
        return [north, south, west, east]
    
    def handle_input(self, key: str = None):
        """Event handler for managing the events from user input."""
        _x, _y = self.coordinates
        surrounding = self.scan_surrounding_tiles()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_w:
                        if not self.game.map.tiles[_y-1][_x].passable:
                            return
                        self.coordinates = _x, _y-1
                        return
                    
                    case pygame.K_s:
                        if not self.game.map.tiles[_y+1][_x].passable:
                            return
                        self.coordinates = _x, _y+1
                        return
                    
                    case pygame.K_a:
                        if not self.game.map.tiles[_y][_x-1].passable:
                            return
                        self.coordinates = _x-1, _y
                        return
                    
                    case pygame.K_d:
                        if not self.game.map.tiles[_y][_x+1].passable:
                            return
                        self.coordinates = _x+1, _y
                    
                    case pygame.K_f:
                        if surrounding[0].is_interactable:
                            return surrounding[0].object.interact()
                        
                        elif surrounding[1].is_interactable:
                            return surrounding[1].object.interact()
                        
                        elif surrounding[2].is_interactable:
                            return surrounding[2].object.interact()
                        
                        elif surrounding[3].is_interactable:
                            return surrounding[3].object.interact()
                    
                    case pygame.K_i:
                        return self.open_inventory()
