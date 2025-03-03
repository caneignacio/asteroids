from circleshape import *
from main import *
import random

wid = 2
col = "white"

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius
    
    def draw(self, screen):
        pygame.draw.circle(screen, col, self.position, self.radius, wid)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            vec1 = self.velocity.rotate(random_angle)
            vec2 = self.velocity.rotate(random_angle * (-1))
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = vec1 * 1.2
            asteroid2.velocity = vec2 * 2.2
