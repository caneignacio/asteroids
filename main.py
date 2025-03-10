import pygame

from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():

    pygame.init()

    clock = pygame.time.Clock()

    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(x, y)
    asteroid_field = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0,0,0))

        for thing in drawable:
            thing.draw(screen)
        
        updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collides(player):
                raise SystemExit("Game Over!")
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
