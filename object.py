import pygame

pygame.init()
infoObject = pygame.display.Info()
width = infoObject.current_w
height = infoObject.current_h
background_image = pygame.transform.scale(pygame.image.load("images/background.jpg"), (width, height))
normal1 = pygame.transform.scale(pygame.image.load('images/normal1.png'), (75, 150))
normal2 = pygame.transform.scale(pygame.image.load('images/normal2.png'), (75, 150))
uni1 = pygame.transform.scale(pygame.image.load('images/uni1.png'), (75, 150))
uni2 = pygame.transform.scale(pygame.image.load('images/uni2.png'), (75, 150))
codecool1 = pygame.transform.scale(pygame.image.load('images/codecool1.png'), (75, 150))
codecool2 = pygame.transform.scale(pygame.image.load('images/codecool2.png'), (75, 150))
mcdo1 = pygame.transform.scale(pygame.image.load('images/mcdo1.png'), (75, 150))
mcdo2 = pygame.transform.scale(pygame.image.load('images/mcdo2.png'), (75, 150))
IT = pygame.transform.scale(pygame.image.load('images/IT.png'), (75, 150))
normal = [normal1, normal2]
codecool = [codecool1, codecool2]
uni = [uni1, uni2]
mcdo = [mcdo1, mcdo2]
IT = [IT, IT]


class Location:

    def __init__(self, name, rect):
        self.name = name
        self.rect = rect

    def action(self, player):
        if self.name == 'codecool':
            player.images = codecool
        elif self.name == 'uni':
            player.images = uni
        elif self.name == 'mcdo':
            player.images = mcdo
        elif self.name == 'IT':
            player.images = IT
        else:
            pass



