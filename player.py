import pygame
pygame.init()
infoObject = pygame.display.Info()
width = 1366
height = 768


class Player:

    def __init__(self, x, y, buttons, images=[]):
        self.x = x
        self.y = y
        self.images = images
        self.current_image = images[0]
        self.buttons = buttons
        self.direction = "right"
        self.speed = 10

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.buttons["up"]] and self.y > 0:
            self.y -= self.speed
            if self.y % 17 == 0:
                self.current_image = self.images[1]
            elif self.y % 13 == 0:
                self.current_image = self.images[0]
        elif keys[self.buttons["down"]] and self.y < height - 150:
            self.y += self.speed
            if self.y % 17 == 0:
                self.current_image = self.images[1]
            elif self.y % 13 == 0:
                self.current_image = self.images[0]
        elif keys[self.buttons["right"]] and self.x < width - 75:
            if self.direction == "left":
                self.current_image = self.images[1]
            self.x += self.speed
            if self.x % 17 == 0:
                self.current_image = self.images[1]
            elif self.x % 13 == 0:
                self.current_image = self.images[0]
            self.direction = "right"
        elif keys[self.buttons["left"]] and self.x > 0:
            self.x -= self.speed
            if self.direction == "right":
                self.current_image = self.images[1]
            if self.x % 17 == 0:
                self.current_image = pygame.transform.flip(self.images[1], True, False)
            elif self.x % 13 == 0:
                self.current_image = pygame.transform.flip(self.images[0], True, False)
            self.direction = "left"

    def draw(self, screen):
        screen.blit(self.current_image, (self.x, self.y))
