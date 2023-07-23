from source.player import Player
from source.map_renderer import MapRenderer
from source.config.properties import get_window_size
from source.config.game_state import GameState, CurrentGameState
from source.constants.colors import *
import pygame


class Game:
    """The main game object that encapsulates all the game items and methods.
    
    Attributes:
        player (Player): The main player for the game.
        map (Map): The map for loading and rending the environment.
    """
    state = GameState.NONE
    current_state = CurrentGameState.MAP
    player_has_moved: bool = False
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("MFGJ-Summer-2023")
        self.clock = pygame.time.Clock()
        self.player = Player(self)
        self.maps = ['../MFGJ-Summer-2023/resources/map_files/map1.txt',]
        self.map = MapRenderer(self, self.maps[0])
    
    def set_up(self):
        self.screen.fill(color=BLACK)
        self.state = GameState.RUNNING
        self.map.load()
        self.map.render()
        #self.map = Map(self, self.maps[0])
    
    def update(self):
        
        if self.current_state == CurrentGameState.MAP:
            self.player_has_moved = False
            self.handle_events()
            
            if self.player_has_moved:
                self.determine_game_events()
    
    def determine_game_events(self):
        map_title = self.map.tiles[self.player.coordinates[1]][self.player.coordinates[0]]
        ...
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.state = GameState.NONE
                surrounding = self.player.scan_surrounding_tiles()
                _x, _y = self.player.coordinates
                match event.key:
                    case pygame.K_w:
                        if not self.map.tiles[_y - 1][_x].passable:
                            return
                        self.player.coordinates = _x, _y - 1
                        return #self.map.render()
                    
                    case pygame.K_s:
                        if not self.map.tiles[_y + 1][_x].passable:
                            return self.map.render()
                        self.player.coordinates = _x, _y + 1
                        return #self.map.render()
                    
                    case pygame.K_a:
                        if not self.map.tiles[_y][_x - 1].passable:
                            return
                        self.player.coordinates = _x - 1, _y
                        return #self.map.render()
                    
                    case pygame.K_d:
                        if not self.map.tiles[_y][_x + 1].passable:
                            return
                        self.player.coordinates = _x + 1, _y
                    
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
                self.map.load()
                self.update()
    
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
