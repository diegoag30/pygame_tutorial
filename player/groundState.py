from .state import State


class GroundState(State):

    def get_collision(self, player, sprite):
        player.rect.bottom = sprite.rect.top
        player.direction.y = 0
        player.on_ground = True

    def get_animation(self, player):
        player.rect = player.image.get_rect(midbottom=player.rect.midbottom)
