import pygame
import project
from project.player import Player
from engine.entity import Entity
from engine.rigidbody import Rigidbody


WHITE = (255, 255, 255)
RED = (255, 0, 0)

player = Player(RED, pygame.Rect(20, 20, 20, 20))
floor = Entity(WHITE, pygame.Rect(20, 440, 640, 40))

player.add_component(Rigidbody)
floor.add_component(Rigidbody)
player.get_component(Rigidbody).gravity = True
player.get_component(Rigidbody).gravity_amount = 3
