import pygame
from shapes.circleshape import CircleShape
from config.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class Asteroid(CircleShape):
    def __init__(self, x, y, radius, can_split=True):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.can_split = can_split

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT
        self.rotation %= 360

    def split(self):
        if not self.can_split:
            return []

        # create two smaller asteroids from this one that are moving in opposite directions
        asteroid1 = Asteroid(self.position.x, self.position.y, self.radius // 2, False)
        asteroid1.velocity = self.velocity.rotate(90)
        asteroid2 = Asteroid(self.position.x, self.position.y, self.radius // 2, False)
        asteroid2.velocity = self.velocity.rotate(-90)

        return [
            asteroid1,
            asteroid2,
        ]