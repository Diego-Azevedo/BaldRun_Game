import pygame
class Door(pygame.sprite.Sprite):
    def __init__(self, pos, *groups):
        super().__init__(*groups)
        try:
            self.image = pygame.image.load('versao_final\game\image\Object\door.png').convert_alpha()
        except FileNotFoundError:
            self.image = pygame.image.load('versao_final/game/image/Object/door.png').convert_alpha()

        self.rect = self.image.get_rect(topleft = pos)