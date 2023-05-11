from .state import State


class GroundState(State):

    def get_collision(self, player, sprite):
        player.rect.bottom = sprite.rect.top
        player.direction.y = 0
        player.on_ground = True

    def get_animation(self, player, sprite, pos_x, pos_y):
        pass
