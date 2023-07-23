from source.player import Player
from source.map import Map


class Game:
    """The main game object that encapsulates all the game items and methods.
    
    Attributes:
        player (Player): The main player for the game.
        map (Map): The map for loading and rending the environment.
    """
    def __init__(self):
        self.player = Player(self)
        self.map = Map(self, '../MFGJ-Summer-2023/test_map.txt')
    
    def play(self):
        """Starts the main game loop."""
        while True:
            print(" ___________________________________________\n"
                  "|Controls:      |            |              |\n"
                  "| (W,A,S,D)Move |(F)Interact |(I)Inventory  |")
            self.map.render()
            _input = input()
            if _input.upper() == 'Q':
                break
            self.player.handle_input(_input)
