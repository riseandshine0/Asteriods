import pygame
import circleshape
from constants import *


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=2)
    
    def update(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += self.velocity * dt