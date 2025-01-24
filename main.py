import pygame
from config.constants import *

def main():
    print("Starting Asteroids woohoo!")
    print(f"Screen size: {SCREEN_WIDTH}x{SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        # TODO: remove
        render_time_running(screen)

        pygame.display.flip()

    pygame.quit()

    print("Game has been closed. Thanks for playing!")

def render_time_running(screen):
    # draw frame count in the middle of the screen
    fps = pygame.time.get_ticks() // 1000
    font = pygame.font.Font(None, 36)
    text = font.render(f"Running for {fps}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    screen.blit(text, text_rect)


if __name__ == "__main__":
    main()