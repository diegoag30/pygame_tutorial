from abc import ABC, abstractmethod


# Define an abstract base class
class State(ABC):

    # Define abstract methods that must be implemented by subclasses
    @abstractmethod
    def get_collision(self, player):
        pass

    # Define abstract methods that must be implemented by subclasses
    @abstractmethod
    def get_animation(self, player, sprite, pos_x, pos_y):
        pass
