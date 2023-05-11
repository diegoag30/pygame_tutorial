from .state import State


class CeillingState(State):

    def get_collision(self, player, sprite):
        player.rect.top = sprite.rect.bottom
        player.direction.y = 0
        player.on_ceiling = True

    def get_animation(self, player, sprite, pos_x, pos_y):
        pass
