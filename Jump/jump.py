import pygame
import sys
import time
from text import *

pygame.init()

display_info = pygame.display.Info()
width, height = display_info.current_w, display_info.current_h
FPS = 100
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (200, 200, 200)
orange = (255, 165, 0)
light_blue = (173, 116, 233)

screen = pygame.display.set_mode((width, height))
screen_color = black
pygame.display.set_caption('E')
font = pygame.font.Font(None, 36)

def draw(text, font_size, y_position):
  font = pygame.font.Font(None, font_size)
  text_render = font.render(text, True, gray)
  text_rect = text_render.get_rect(center=(width // 2, y_position))
  screen.blit(text_render, text_rect)

def start_screen():
  screen.fill(black)
  starter = True
  while starter:
    draw("E", 100, height // 4)
    
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
          game()
        elif lead.collidepoint(mouse_pos):
          starter = False
          leaderboard_screen()

def leaderboard_screen():
  lead = True
  while lead:    
    screen.fill(black)
    
    draw("Coming Soon...", 100, height // 2 - 100)
    
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
        if home.collidepoint(pygame.mouse.get_pos()):
          lead = False
          start_screen()

def game():
  gaming = True
  while gaming:
    screen.fill(black)
    
    draw("Coming Soon...", 100, height // 2 - 100)
    
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
          gaming = False
          start_screen()
    
start_screen()