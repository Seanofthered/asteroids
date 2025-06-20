import pygame
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from shot import Shot
import sys

def main():
    pygame.init()

    print("Starting Asteroids!")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    dt = 0
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (drawable, updateable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT/2), PLAYER_RADIUS)
    field = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.event.get()

        screen.fill((0,0,0))

        for item in drawable:
            item.draw(screen)

        updateable.update(dt)

        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game over!")
                sys.exit()
        

            for shot in shots:
                if asteroid.collision_check(shot):
                    shot.kill()
                    asteroid.split()


        pygame.display.flip()
        dt = clock.tick(60) / 1000

        
        

if __name__ == "__main__":
    main()