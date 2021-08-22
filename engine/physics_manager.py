import engine
from engine.entity import Entity


class PhysicsManager:
    rb_list = []

    def check_collisions(rb):
        try:
            physics_manager.rb_list.remove(rb)
        except:
            pass
        for rigid in physics_manager.rb_list:
            if physics_manager.colliding(rb, rigid):
                return rigid.rect

    def colliding(self, rb_one, rb_two):
        if rb_one.rect[1] + rb_one.rect[3] > rb_two.rect[1]\
        and rb_one.rect[0] + rb_one.rect[2] > rb_two.rect[0]:
            if rb_one.rect[1] + rb_one.rect[3] < rb_two.rect[1] + rb_two.rect[3]\
            and rb_one.rect[0] + rb_one.rect[2] < rb_two.rect[0] + rb_two.rect[2]:
                return rb_two.rect

physics_manager = PhysicsManager()

