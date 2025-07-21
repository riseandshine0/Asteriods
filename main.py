import pygame, sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
#    print("Starting Asteroids!")
#    print(f"Screen width: {SCREEN_WIDTH}")
#    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    asteroid_field = AsteroidField()
    player1 = Player((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updateable.update(dt)    
        for obj in asteroids:
            if obj.check_collision(player1):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.check_collision(obj):
                    obj.split()
                    shot.kill()

        screen.fill((0,0,0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        #limit Framerate to 60 FPS
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
