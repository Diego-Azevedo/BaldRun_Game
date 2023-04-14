import pygame

from game.UI.interface import Interface

class Menu(Interface):
    def __init__(self, *groups):
        super().__init__( *groups)
        try:
            self.image = pygame.image.load('versao_final/game/image/menu/menu_iniciar.jpg')

        except FileNotFoundError:
            self.image = pygame.image.load("versao_final\game\image\menu\menu_iniciar.jgp")
     

        
        