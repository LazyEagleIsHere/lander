import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Downward Starfield (No Classes)")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Star settings
NUM_STARS = 100
STAR_SPEED_MIN = 1
STAR_SPEED_MAX = 4
STAR_SIZE_MIN = 1
STAR_SIZE_MAX = 3

# Initialize stars as a list of dictionaries
stars = []
for _ in range(NUM_STARS):
    star = {
        'x': random.randint(0, WIDTH),
        'y': random.randint(0, HEIGHT),
        'speed': random.uniform(STAR_SPEED_MIN, STAR_SPEED_MAX),
        'size': random.randint(STAR_SIZE_MIN, STAR_SIZE_MAX)
    }
    stars.append(star)

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update star positions
    for star in stars:
        star['y'] += star['speed']
        if star['y'] > HEIGHT:
            star['y'] = 0
            star['x'] = random.randint(0, WIDTH)
            star['speed'] = random.uniform(STAR_SPEED_MIN, STAR_SPEED_MAX)
            star['size'] = random.randint(STAR_SIZE_MIN, STAR_SIZE_MAX)

    # Draw everything
    screen.fill(BLACK)
    for star in stars:
        pygame.draw.circle(screen, WHITE, (int(star['x']), int(star['y'])), star['size'])

    pygame.display.flip()

pygame.quit()
