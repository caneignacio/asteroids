from circleshape import *
from main import *

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

