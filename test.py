import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
OBJECT_COLOR = (0, 128, 255)
ARROW_COLOR = (255, 0, 0)
ARROW_LENGTH = 50
black = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("e")

# Object properties
object_pos = [400, 300]
object_radius = 20

# Main loop
running = True
out_of_bounds = False
last_valid_position = object_pos.copy()

while running:
    screen.fill(BACKGROUND_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.draw.polygon(screen, black, [[10, 10], [10, 25], [25, 10]])
    pygame.draw.polygon(screen, black, [[15, 20], [20, 15], [27, 15], [15, 27]])
    

    

    pygame.display.flip()
    pygame.time.Clock().tick(60)