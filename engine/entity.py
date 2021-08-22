import pygame
from abc import abstractmethod
from engine import game


class Entity:
    def __init__(self, color, rect, components=[]):
        self.color = color
        self.rect = rect
        self.components = list(components)
        game.entity_list.append(self)

    def base_update(self):
        for com in self.components:
            com.update()
        self.update()

    def add_component(self, comp):
        self.comp = comp(self)
        self.components.append(self.comp)

    def get_component(self, objType):
        self.objType = objType
        for component in self.components:
            if type(component) == self.objType:
                return component

    def update(self):
        pass
