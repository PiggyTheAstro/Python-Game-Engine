from abc import abstractmethod


class Component:
    @abstractmethod
    def __init__(self, parent):
        self.parent = parent

    @abstractmethod
    def update(self):
        pass
