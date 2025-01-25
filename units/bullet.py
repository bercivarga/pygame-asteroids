import pygame

from config.constants import SCREEN_WIDTH, SCREEN_HEIGHT, BULLET_RADIUS, BULLET_SPEED, BULLET_LIFETIME
from shapes.circleshape import CircleShape


class Bullet(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, BULLET_RADIUS)
        self.velocity = velocity
        self.lifetime = BULLET_LIFETIME
        self.age = 0.0

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)


    def update(self, dt):
        self.position += self.velocity * dt * BULLET_SPEED

        # kill if out of bounds
        if (self.position.x < 0 or self.position.x > SCREEN_WIDTH or
                self.position.y < 0 or self.position.y > SCREEN_HEIGHT):
            self.kill()

        # update age
        self.age += dt
        if self.age > self.lifetime:
            self.kill()
