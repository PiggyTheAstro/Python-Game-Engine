import pygame
import engine
from engine.component import Component
from engine.physics_manager import PhysicsManager
from engine.entity import Entity


class Rigidbody(Component):

    def __init__(self, parent, gravity=False, gravity_amount=2):
        self.parent = parent
        self.gravity = gravity
        self.gravity_amount = gravity_amount
        PhysicsManager.rb_list.append(self.parent)

    def update(self):
        if self.gravity:
            self.parent.rect[1] += self.gravity_amount
            self.gravity_amount += 0.05
            other = PhysicsManager.check_collisions(self.parent)
            if other is not None:
                self.parent.rect[1] = other[1] - self.parent.rect[3]
                # User can't set base gravity, will change later
                self.gravity_amount = 2
