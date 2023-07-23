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
    
    def _scan_surrounding_tiles(self) -> list[tuple[int, int]]:
        """Get the tiles from surrounding the player (+ - xy coordinates)
        
        Return:
            list[tuple[int, int]
        """
        _x, _y = self.coordinates
        return [
            self.game.map.tiles[_y-1][_x],
            self.game.map.tiles[_y+1][_x],
            self.game.map.tiles[_y][_x-1],
            self.game.map.tiles[_y][_x+1],
        ]
    
    def handle_input(self, key: str):
        """Event handler for managing the events from user input."""
        _x, _y = self.coordinates
        surrounding = self._scan_surrounding_tiles()
        match key.upper():
            case 'W':
                if not self.game.map.tiles[_y-1][_x].passable:
                    return
                self.coordinates = _x, _y-1
                return
            case 'S':
                if not self.game.map.tiles[_y+1][_x].passable:
                    return
                self.coordinates = _x, _y+1
                return
            case 'A':
                if not self.game.map.tiles[_y][_x-1].passable:
                    return
                self.coordinates = _x-1, _y
                return
            case 'D':
                if not self.game.map.tiles[_y][_x+1].passable:
                    return
                self.coordinates = _x+1, _y
            case 'F':
                if surrounding[0].is_interactable:
                    return surrounding[0].object.interact()
                elif surrounding[1].is_interactable:
                    return surrounding[1].object.interact()
                elif surrounding[2].is_interactable:
                    return surrounding[2].object.interact()
                elif surrounding[3].is_interactable:
                    return surrounding[3].object.interact()
            case 'I':
                return self.open_inventory()
