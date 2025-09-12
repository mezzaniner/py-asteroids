import pygame
import random
from circleshape import CircleShape
from constants import PLAYER_SPEED, ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # if the asteroid is larger than the smallest type, split it when destroyed
    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return

        angle = random.uniform(20, 50)
        vec_1 = self.velocity.rotate(angle)
        vec_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_one.velocity = vec_1 * 1.2
        new_asteroid_two.velocity = vec_2 * 1.2
        self.kill()

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt