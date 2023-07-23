# Run from this file.
from source.config.game_state import GameState
from source import *
import pygame

if __name__ == '__main__':
    game = Game()
    game.set_up()
    while game.state != GameState.ENDED:
        game.clock.tick(50)
        if game.state == GameState.NONE:
            ...
        elif game.state == GameState.RUNNING:
            game.update()
        pygame.display.flip()
