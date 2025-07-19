import pygame
import circleshape
from constants import *

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, SHOT_RADIUS, width=2)

    def update(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += self.velocity * dt