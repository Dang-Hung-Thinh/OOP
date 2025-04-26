import os
import pygame
import random
from settings import SCREEN_WIDTH, PIPE_GAP

class Pipe:
    def __init__(self, x):
        self.x = x
        self.top_height = random.randint(100, 300)
        self.bottom_y = self.top_height + PIPE_GAP

        # Construct paths to the image files
        assets_dir = os.path.join(os.path.dirname(__file__), "assets")
        self.image_top = pygame.image.load(os.path.join(assets_dir, "pipe_top.png"))
        self.image_bottom = pygame.image.load(os.path.join(assets_dir, "pipe_bottom.png"))

    def update(self):
        self.x -= 3

    def draw(self, screen):
        screen.blit(self.image_top, (self.x, self.top_height - self.image_top.get_height()))
        screen.blit(self.image_bottom, (self.x, self.bottom_y))

    def get_rects(self):
        top_rect = self.image_top.get_rect(topleft=(self.x, self.top_height - self.image_top.get_height()))
        bottom_rect = self.image_bottom.get_rect(topleft=(self.x, self.bottom_y))
        return top_rect, bottom_rect