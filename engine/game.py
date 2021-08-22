import sys
import pygame
import engine
from engine.entity import Entity
from engine.component import Component


BLACK = (0, 0, 0)
entity_list = []
watched_key = -1


def create_window(size):
    window = pygame.display.set_mode(size)


def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def render():
    screen = pygame.display.get_surface()
    screen.fill(BLACK)
    for ent in entity_list:
        pygame.draw.rect(screen, ent.color, ent.rect)
    pygame.display.flip()


def update_entities():
    for ent in entity_list:
        ent.base_update()


def get_key_down(key):
    watched_key = key
    keys = pygame.key.get_pressed()
    if keys[watched_key]:
        return True
    else:
        return False
