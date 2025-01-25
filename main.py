import random

import pygame

from config.constants import *
from units.asteroid import Asteroid
from units.player import Player
from units.asteroidfield import AsteroidField

def spawn_asteroid():
    # spawn a new asteroid at a random edge
    edge = random.choice(AsteroidField.edges)
    speed = random.randint(40, 100)
    velocity = edge[0] * speed
    velocity = velocity.rotate(random.randint(-30, 30))
    position = edge[1](random.uniform(0, 1))
    kind = random.randint(1, ASTEROID_KINDS)
    asteroid = Asteroid(position.x, position.y, ASTEROID_MIN_RADIUS * kind)
    asteroid.velocity = velocity
    return asteroid

def main():
    print("Starting Asteroids... Good luck Astronaut!")
    print(f"Screen size: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")

    # initialize pygame
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    # clock
    clock = pygame.time.Clock()
    dt = 0

    # game objects
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # sprite groups
    updatable_objects = pygame.sprite.Group()
    drawable_objects = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # add objects to sprite groups
    updatable_objects.add(player)
    drawable_objects.add(player)

    # asteroid field
    asteroid_field = AsteroidField(updatable_objects)
    updatable_objects.add(asteroid_field)

    # game loop
    running = True

    last_time = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # render_time_running(screen, dt)
        # player.update(dt)
        # player.draw(screen)

        # spawn a new asteroid every second
        current_time = pygame.time.get_ticks()
        if current_time - last_time > 1000:
            last_time = current_time
            asteroid = spawn_asteroid()
            asteroids.add(asteroid)
            updatable_objects.add(asteroid)
            drawable_objects.add(asteroid)

        for obj in updatable_objects:
            obj.update(dt)
        for obj in drawable_objects:
            obj.draw(screen)

        updatable_objects.add(player.bullets)
        drawable_objects.add(player.bullets)

        # check for collisions
        for asteroid in asteroids:
            if player.is_colliding_with(asteroid):
                print("Player has been hit by an asteroid!")
                running = False

            for bullet in player.bullets:
                if bullet.is_colliding_with(asteroid):
                    print("Bullet has hit an asteroid!")
                    bullet.kill()
                    asteroid.kill()
                    for new_asteroid in asteroid.split():
                        asteroids.add(new_asteroid)
                        updatable_objects.add(new_asteroid)
                        drawable_objects.add(new_asteroid)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()

    print("Game has finished. Thanks for playing!")


def render_time_running(screen, dt):
    # draw frame count in the middle of the screen
    font = pygame.font.Font(None, 36)
    text = font.render(f"Running for {dt}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)


if __name__ == "__main__":
    main()
