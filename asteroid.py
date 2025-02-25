import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  # Call parent's init


    def draw(self, surface):  # Need surface parameter
        pygame.draw.circle(surface, "white", self.position, self.radius, width=2)

    def update(self, dt):  # Need dt parameter
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt
