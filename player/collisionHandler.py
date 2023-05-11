from .ceillingState import CeillingState
from .groundState import GroundState


class CollisionHandler:

    def __init__(self, player):
        self.state = GroundState()
        self.player = player

    def collide(self, sprite):
        if self.player.direction.y > 0:
            self.state = GroundState()
            self.state.get_collision(self.player, sprite)
        elif self.player.direction.y < 0:
            self.state = CeillingState()
            self.state.get_collision(self.player, sprite)

    def animate(self, player):
        self.state.get_animation(player)
