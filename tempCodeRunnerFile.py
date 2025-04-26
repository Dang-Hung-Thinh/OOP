import pygame
from bird import Bird
from pipe import Pipe
from utils.collision import check_collision
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Flappy Bird")
        self.clock = pygame.time.Clock()
        self.bird = Bird(34, 24)
        self.pipes = [Pipe(320)]
        self.running = True

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.screen.fill((135, 206, 235))  # sky blue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.bird.jump()

            self.bird.update()
            self.bird.draw(self.screen)

            if self.pipes[-1].x < 200:
                self.pipes.append(Pipe(400))

            for pipe in self.pipes:
                pipe.update()
                pipe.draw(self.screen)

            # collision detection
            bird_x, bird_y = self.bird.get_position()
            bird_rect = pygame.Rect(bird_x, bird_y, 34, 24)
            if check_collision(bird_rect, self.pipes):
                print("Game Over!")
                self.running = False

            pygame.display.update()

        pygame.quit()