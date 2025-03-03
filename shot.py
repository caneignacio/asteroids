from circleshape import *
from main import *

col = "white"
wid = 2
SHOT_RADIUS = 5

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = SHOT_RADIUS

    def draw(self, screen):
        pygame.draw.circle(screen, col, self.position, self.radius, wid)

    def update(self, dt):
        self.position += self.velocity * dt
