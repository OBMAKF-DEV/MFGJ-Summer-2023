import pygame
from source.config.game_state import GameState
from constants import *


class Menu:
    def __init__(self, game):
        self.game = game
    
    def set_up(self):
        # menu design goes here
        ...
    
    def update(self):
        self.game.screen.fill(BLACK)
        rect = pygame.Rect(1, 1, 2, 2)
        # blit image
        
        for event in pygame.event.get():
            if event == pygame.QUIT:
                self.game.state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.state = GameState.ENDED
                elif event.key == pygame.K_RETURN:
                    self.game.set_up()
                    self.game.state = GameState.RUNNING
