import pygame
import engine
from engine.entity import Entity
from engine import game


class Player(Entity):

    def update(self):
        if game.get_key_down(pygame.K_w):
            print("input working")
