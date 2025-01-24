import pygame

from config.constants import *
from units.player import Player


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

    updatable_objects.add(player)
    drawable_objects.add(player)

    # game loop
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # render_time_running(screen, dt)
        # player.update(dt)
        # player.draw(screen)

        for obj in updatable_objects:
            obj.update(dt)
        for obj in drawable_objects:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()

    print("Game has been closed. Thanks for playing!")


def render_time_running(screen, dt):
    # draw frame count in the middle of the screen
    font = pygame.font.Font(None, 36)
    text = font.render(f"Running for {dt}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)


if __name__ == "__main__":
    main()
