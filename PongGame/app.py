import pygame
import sys

pygame.init()

# Screen dimensions
WIDTH = 800
HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

# Paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((15, 90))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 6

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= self.speed

    def move_down(self):
        if self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((15, 15))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.speed_x = 5
        self.speed_y = 5

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.reset()

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x *= -1

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Game loop
player1 = Paddle(10, HEIGHT // 2 - 45)
player2 = Paddle(WIDTH - 25, HEIGHT // 2 - 45)
ball = Ball()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1.move_up()
    if keys[pygame.K_s]:
        player1.move_down()
    if keys[pygame.K_UP]:
        player2.move_up()
    if keys[pygame.K_DOWN]:
        player2.move_down()

    ball.update()

    # Collision detection
    if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
        ball.speed_x *= -1

    screen.fill(BLACK)
    player1.draw(screen)
    player2.draw(screen)
    ball.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()