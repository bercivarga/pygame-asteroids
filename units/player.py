import pygame
from shapes.circleshape import CircleShape
from config.constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_ROTATION_SPEED, PLAYER_VELOCITY_DECAY, SCREEN_WIDTH, SCREEN_HEIGHT
from units.bullet import Bullet

# Player class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.bullets = pygame.sprite.Group()
        self.time_since_last_shot = 0
        self.bullet_cooldown = 0.1

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def update(self, dt):
        self.time_since_last_shot += dt

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotation -= PLAYER_ROTATION_SPEED * dt
        if keys[pygame.K_d]:
            self.rotation += PLAYER_ROTATION_SPEED * dt
        if keys[pygame.K_w]:
            self.velocity += pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            self.velocity -= pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SPEED * dt
        if keys[pygame.K_SPACE]:
            if self.time_since_last_shot > self.bullet_cooldown:
                self.time_since_last_shot = 0
                bullet = self.shoot()
                self.bullets.add(bullet)


        self.position += self.velocity * dt
        self.velocity *= PLAYER_VELOCITY_DECAY
        self.position.x %= SCREEN_WIDTH
        self.position.y %= SCREEN_HEIGHT
        self.rotation %= 360

    def shoot(self):
        return Bullet(self.position.x, self.position.y, pygame.Vector2(0, 1).rotate(self.rotation) * 200)
