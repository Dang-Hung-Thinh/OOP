import os
import pygame
from settings import GRAVITY, JUMP_STRENGTH

class Bird:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__velocity = 0
        assets_path = os.path.join(os.path.dirname(__file__), "assets", "bird.png")
        self.image = pygame.image.load(assets_path)

    def update(self):
        self.__velocity += GRAVITY
        self.__y += self.__velocity

    def jump(self):
        self.__velocity = JUMP_STRENGTH

    def get_position(self):
        return self.__x, self.__y

    def draw(self, screen):
        screen.blit(self.image, (self.__x, self.__y))