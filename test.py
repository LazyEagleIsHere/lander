import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
width, height = 800, 600
BACKGROUND_COLOR = (255, 255, 255)
OBJECT_COLOR = (0, 128, 255)
ARROW_COLOR = (255, 0, 0)
ARROW_LENGTH = 50
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (200, 200, 200)
orange = (255, 165, 0)
light_blue = (173, 116, 233)

# Set up the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("e")

# Object properties
object_pos = [400, 300]
object_radius = 20

# Main loop
running = True
out_of_bounds = False
last_valid_position = object_pos.copy()

def draw(text, font_size, y_position):
    font = pygame.font.Font(None, font_size)
    text_render = font.render(text, True, gray)
    text_rect = text_render.get_rect(center=(width // 2, y_position))
    screen.blit(text_render, text_rect)

while running:
    screen.fill(black)
    run = True
    countdown_numbers = ["3", "2", "1"]
    
    for number in countdown_numbers:
        draw(number, 100, height // 2)
        pygame.display.flip()  # Update the display here
        time.sleep(1)          # Wait for 1 second
        screen.fill(black)     # Clear the screen for the next number

    while run:  # Keep checking for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    pygame.display.flip()
    pygame.time.Clock().tick(60)