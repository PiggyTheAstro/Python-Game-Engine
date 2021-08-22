import sys
import pygame
import engine
from engine import game
from engine.entity import Entity
from project import usercode


pygame.init()
WINDOW_SIZE = (640, 480)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CLOCK = pygame.time.Clock()
game.create_window(WINDOW_SIZE)

while True:
    game.process_events()
    game.update_entities()
    game.render()
    CLOCK.tick(60)
