import pygame
import sys
import time
from text import *

pygame.init()

def draw(text, font_size, y_position, screen):
  font = pygame.font.Font(None, font_size)
  text_render = font.render(text, True, (200, 200, 200))
  text_rect = text_render.get_rect(center=(width // 2, y_position))
  screen.blit(text_render, text_rect)

def start_screen():
  screen.fill(black)
  starter = True
  while starter:
    draw("E", 100, height // 4, screen)
    
    start = pygame.Rect(width // 2 - 200, height // 2 + 50, 400, 100)
    lead = pygame.Rect(width // 2 - 200, height // 2 + 200, 400, 100)
    
    mouse_pos = pygame.mouse.get_pos()

    if start.collidepoint(mouse_pos):
      write(screen, start, "Start", 65, "black", "gray69", 10)
    else:
      write(screen, start, "Start", 65, "black", "white", 10)
    
    if lead.collidepoint(mouse_pos):
      write(screen, lead, "Leaderboard", 65, "black", "gray69", 10)
    else:
      write(screen, lead, "Leaderboard", 65, "black", "white", 10)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if start.collidepoint(mouse_pos):
          starter = False
          cntdown()
        elif lead.collidepoint(mouse_pos):
          starter = False
          leaderboard_screen()

def leaderboard_screen():
  lead = True
  while lead:    
    screen.fill(black)
    
    draw("Coming Soon...", 100, height // 2 - 100, screen)
    
    home = pygame.Rect(width // 2 - 200, height // 2 + 150, 400, 100)
    
    mouse_pos = pygame.mouse.get_pos()
    
    if home.collidepoint(mouse_pos):
      write(screen, home, "Return", 65, "black", "gray69", 10)
    else:
      write(screen, home, "Return", 65, "black", "white", 10)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if home.collidepoint(mouse_pos):
          lead = False
          start_screen()

def wrong_area():
  sad = True
  while sad:
    draw("Game Over", 100, height // 2 - 250, screen)
    draw("Reason: landed at wrong area", 100, height // 2 - 150, screen)
    
    mouse_pos = pygame.mouse.get_pos()
    
    again = pygame.Rect(width // 2 - 200, height // 2 + 50, 400, 100)
    
    if again.collidepoint(mouse_pos):
      write(screen, again, "Play Again", 65, "black", "gray69", 10)
    else:
      write(screen, again, "Play Again", 65, "black", "white", 10)
    
    home = pygame.Rect(width // 2 - 200, height // 2 + 200, 400, 100)
    
    if home.collidepoint(mouse_pos):
      write(screen, home, "Return", 65, "black", "gray69", 10)
    else:
      write(screen, home, "Return", 65, "black", "white", 10)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if home.collidepoint(mouse_pos):
          sad = False
          start_screen()
        elif again.collidepoint(mouse_pos):
          sad = False
          cntdown()

def cntdown():
  global spaceship_pos, gravity, a, v1, v2, fuel  # Declare globals
  screen.fill(black)
  cnt = ["3", "2", "1"]
  
  for number in cnt:
    draw(number, 100, height // 2, screen)
    pygame.display.flip() 
    time.sleep(1) 
    screen.fill(black)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()

  game()  # Start the game after countdown

def game():
  global spaceship_pos, gravity, a, v1, v2, fuel  # Declare globals
  gaming = True

  # Reset game state
  spaceship_pos = [10, 10]
  gravity = 3.0
  a = 6.0
  v1 = -0.1
  v2 = 0.0
  fuel = 1000

  while gaming:
    screen.fill(black)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()

    # Game logic
    if spaceship_pos[1] + 15 >= height:
      wrong_area()
      gaming = False
    
    # Drawing and updating spaceship
    pygame.draw.rect(screen, red, (int(spaceship_pos[0]), int(spaceship_pos[1]), 10, 10))
    
    v1 += gravity / fps
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
      v1 -= a / fps
      fuel -= 1
    
    spaceship_pos[1] += v1
    
    if keys[pygame.K_LEFT]:
      v2 += a / (fps * 2)
      fuel -= 1
    
    if keys[pygame.K_RIGHT]:
      v2 -= a / (fps * 2)
      fuel -= 1
    
    v2 = max(min(v2, 20.0), -20.0)
    
    spaceship_pos[0] += v2
    
    # Update display
    pygame.display.flip()
    clock.tick(fps)

# Initialize display settings
display_info = pygame.display.Info()
width, height = display_info.current_w, display_info.current_h
fps = 60
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (200, 200, 200)
orange = (255, 165, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('E')
font = pygame.font.Font(None, 36)

# Start the game
start_screen()