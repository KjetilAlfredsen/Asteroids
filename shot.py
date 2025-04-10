from circleshape import *
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.shot_radius = SHOT_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position , self.radius, width = 2)

    def update(self, dt):
        self.position += (self.velocity * dt)
