import pygame
import sys
import time
from text import *
from pygame.math import Vector2

pygame.init()

def draw(text, font_size, y_position):
  font = pygame.font.Font(None, font_size)
  text_render = font.render(text, True, gray)
  text_rect = text_render.get_rect(center=(width // 2, y_position))
  screen.blit(text_render, text_rect)

def start_screen():
  screen.fill(black)
  starter = True
  while starter:
    draw("Rocket Lander", 100, height // 4)
    
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
  global spaceship_pos, gravity, a, v1, v2, fuel, platform_pos, platform_ground1, platform_ground2
  lead = True
  while lead:    
    screen.fill(black)
    
    draw("Coming Soon...", 100, height // 2 - 100)
    
    home = pygame.Rect(width // 2 - 200, height // 2 + 150, 400, 100)
    
    mouse_pos = pygame.mouse.get_pos()
    
    if home.collidepoint(mouse_pos):
      write(screen, home, "Home", 65, "black", "gray69", 10)
    else:
      write(screen, home, "Home", 65, "black", "white", 10)
    
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

def login():
  global username
  username = ""
  running = True
  
  while running:
    screen.fill(black)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
        elif event.key == pygame.K_RETURN:
          try:
            if username == "admin":
              running = False
              password_screen()
            elif 25000 <= int(username) <= 31000:
              running = False
            else:
              username = ""
          except:
            if len(username) == 3 and username[0].isalpha() and username[1].isalpha() and username[2].isalpha():
              running = False
            else:
              username = ""
        elif event.key == pygame.K_BACKSPACE:
          username = username[:-1]
        else:
          username += event.unicode
    
    name_surface = font.render(username, True, white)
    name_rect = name_surface.get_rect()
    name_rect.center = (width // 2, height // 2)
    screen.blit(name_surface, name_rect)
    
    text_surface = font.render("Type Your Index No. : ", True, white)
    text_rect = text_surface.get_rect()
    text_rect.center = (width // 2, height // 2 - 80)
    screen.blit(text_surface, text_rect)
    
    pygame.display.update()
  
  start_screen()
  
def password_screen():
  global me
  me = False
  password = ""
  hidden = ""
  running = True
  
  while running:
    screen.fill(black)
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
        elif event.key == pygame.K_RETURN:
          if password == "Admin":
            running = False
            me = True
          else:
            password = ""
            hidden = ""
            running = False
            login()
        elif event.key == pygame.K_BACKSPACE:
          password = password[:-1]
          hidden = hidden[:-1]
        elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
          continue
        else:
          password += event.unicode
          hidden += '*'

    pass_surface = font.render(hidden, True, white)
    pass_rect = pass_surface.get_rect()
    pass_rect.center = (width // 2, height // 2)
    screen.blit(pass_surface, pass_rect)
    
    text_surface = font.render("Password", True, white)
    text_rect = text_surface.get_rect()
    text_rect.center = (width // 2, height // 2 - 80)
    screen.blit(text_surface, text_rect)
    
    pygame.display.update()
  
  start_screen()
    
def wrong_area():
  global spaceship_pos, gravity, a, v1, v2, fuel, platform_pos, platform_ground1, platform_ground2
  screen.fill(black)
  sad = True
  while sad:
    draw("Game Over", 100, height // 2 - 250)
    draw("Reason: landed at wrong area", 100, height // 2 - 150)
    
    mouse_pos = pygame.mouse.get_pos()
    
    again = pygame.Rect(width // 2 - 200, height // 2 + 50, 400, 100)
    
    if again.collidepoint(mouse_pos):
      write(screen, again, "Play Again", 65, "black", "gray69", 10)
    else:
      write(screen, again, "Play Again", 65, "black", "white", 10)
    
    home = pygame.Rect(width // 2 - 200, height // 2 + 200, 400, 100)
    
    if home.collidepoint(mouse_pos):
      write(screen, home, "Home", 65, "black", "gray69", 10)
    else:
      write(screen, home, "Home", 65, "black", "white", 10)
    
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

def win():
  global spaceship_pos, gravity, a, v1, v2, fuel, platform_pos, platform_ground1, platform_ground2
  yay = True
  while yay:
    screen.fill(black)
    draw("You Win!", 100, height // 2 - 250)
    
    if v1 <= 1.0:
      draw(f"Touchdown Softness: Prefect ({v1:.5f} m/s)", 100, height // 2)
    elif v1 <= 2.0:
      draw(f"Touchdown Softness: Good ({v1:.5f} m/s)", 100, height // 2)
    else:
      draw(f"Touchdown Softness: Terrible ({v1:.5f} m/s)", 100, height // 2)
        
    mouse_pos = pygame.mouse.get_pos()
    
    again = pygame.Rect(width // 2 - 200, height // 2 + 50, 400, 100)
    
    if again.collidepoint(mouse_pos):
      write(screen, again, "Play Again", 65, "black", "gray69", 10)
    else:
      write(screen, again, "Play Again", 65, "black", "white", 10)
    
    home = pygame.Rect(width // 2 - 200, height // 2 + 200, 400, 100)
    
    if home.collidepoint(mouse_pos):
      write(screen, home, "Home", 65, "black", "gray69", 10)
    else:
      write(screen, home, "Home", 65, "black", "white", 10)
    
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
          yay = False
          start_screen()
        elif again.collidepoint(mouse_pos):
          yay = False
          cntdown()

def lose():
  global spaceship_pos, gravity, a, v1, v2, fuel, platform_pos, platform_ground1, platform_ground2
  sad = True
  while sad:
    draw("Game Over", 100, height // 2 - 250)
    draw("Reason: Rocket exploded due to your worse landing", 100, height // 2 - 150)
    
    mouse_pos = pygame.mouse.get_pos()
    
    again = pygame.Rect(width // 2 - 200, height // 2 + 50, 400, 100)
    
    if again.collidepoint(mouse_pos):
      write(screen, again, "Play Again", 65, "black", "gray69", 10)
    else:
      write(screen, again, "Play Again", 65, "black", "white", 10)
    
    home = pygame.Rect(width // 2 - 200, height // 2 + 200, 400, 100)
    
    if home.collidepoint(mouse_pos):
      write(screen, home, "Home", 65, "black", "gray69", 10)
    else:
      write(screen, home, "Home", 65, "black", "white", 10)
    
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
  global spaceship_pos, gravity, a, v1, v2, fuel, platform_pos, platform_ground1, platform_ground2
  screen.fill(black)
  cnt = ["3", "2", "1"]
  
  for number in cnt:
    draw(number, 100, height // 2)
    pygame.display.flip()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
          
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
  game()

def collide_line_line(p1, p2, p3, p4):
  def det(a, b):
    return a.x * b.y - a.y * b.x

  r = p2 - p1
  s = p4 - p3
  denominator = det(r, s)
  if denominator == 0:
    return False

  numerator_t = det(p3 - p1, s)
  numerator_u = det(p3 - p1, r)
  t = numerator_t / denominator
  u = numerator_u / denominator

  return 0 <= t <= 1 and 0 <= u <= 1

def point_in_polygon(point, polygon):
  x, y = point.x, point.y
  inside = False
  n = len(polygon)
  for i in range(n):
    j = (i + 1) % n
    xi, yi = polygon[i].x, polygon[i].y
    xj, yj = polygon[j].x, polygon[j].y
    intersect = ((yi > y) != (yj > y)) and \
                (x < (xj - xi) * (y - yi) / (yj - yi + 1e-10) + xi)
    if intersect:
      inside = not inside
  return inside

def polygons_collide(poly1, poly2):
  for i in range(len(poly1)):
    for j in range(len(poly2)):
      p1 = poly1[i]
      p2 = poly1[(i + 1) % len(poly1)]
      p3 = poly2[j]
      p4 = poly2[(j + 1) % len(poly2)]
      if collide_line_line(p1, p2, p3, p4):
        return True
  for p in poly1:
    if point_in_polygon(p, poly2):
      return True
  for p in poly2:
    if point_in_polygon(p, poly1):
      return True
  return False

def get_spaceship_polygon(pos):
  x, y = pos
  w, h = 10, 10
  return [Vector2(x, y), Vector2(x + w, y), Vector2(x + w, y + h), Vector2(x, y + h)]

def game():
  global spaceship_pos, gravity, a, v1, v2, fuel, platform_pos, platform_ground1, platform_ground2, ground
  
  gaming = True
  
  spaceship_pos = [10, 10]
  gravity = 3.0
  a = 6.0
  v1 = -0.1
  v2 = 0.0
  
  if username == "admin" and me:
    fuel = 1e100
  else:
    fuel = 1e3
  
  platform_pos = [randint(200, width - 200), randint(height // 2, height - 100)]
  platform_ground1 = randint(200, 1000)
  platform_ground2 = randint(200, 1000)

  pygame.display.flip()

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
    
    ground = [Vector2(platform_pos[0], platform_pos[1] + 2), 
              Vector2(platform_pos[0] - platform_ground1, height), 
              Vector2(platform_pos[0] + platform_ground2, height), 
              Vector2(platform_pos[0] + 20, platform_pos[1] + 2)]
    
    spaceship_poly = get_spaceship_polygon(spaceship_pos)
    
    pygame.draw.polygon(screen, gray, [(p.x, p.y) for p in ground])
    
    pygame.draw.rect(screen, light_blue, (int(platform_pos[0]), int(platform_pos[1]), 20, 5))
    
    pygame.draw.polygon(screen, red, [(p.x, p.y) for p in spaceship_poly])
    
    if spaceship_pos[1] + 15 >= height:
      wrong_area()
      gaming = False
    
    if polygons_collide(spaceship_poly, ground):
      wrong_area()
    
    if platform_pos[0] <= spaceship_pos[0] + 10 and spaceship_pos[0] <= platform_pos[0] + 20 and platform_pos[1] <= spaceship_pos[1] + 10 < platform_pos[1] + 5:
      if v1 <= 3.0:
        win()
      else:
        lose()
    
    v1 += gravity / fps
    spaceship_pos[1] += v1
    
    if username == "admin" and me:
      if fuel > 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
          v1 -= a / fps
          fuel -= 1
        
        if keys[pygame.K_LEFT]:
          v2 += a / (fps * 2)
          fuel -= 1
        
        if keys[pygame.K_RIGHT]:
          v2 -= a / (fps * 2)
          fuel -= 1
    else:
      if fuel > 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
          v1 -= a / fps
          fuel -= 1
        
        if keys[pygame.K_RIGHT]:
          v2 += a / (fps * 2)
          fuel -= 1
        
        if keys[pygame.K_LEFT]:
          v2 -= a / (fps * 2)
          fuel -= 1
    
    v2 = max(min(v2, 20.0), -20.0)
    
    spaceship_pos[0] += v2
    
    info_y = 10
    info_spacing = 75
    vertical_v_text = font.render(f"Vertical velocity: {v1:.5f}", True, orange)
    vertical_v_rect = vertical_v_text.get_rect(topleft = (10, info_y))
    pygame.draw.rect(screen, black, vertical_v_rect.inflate(10, 5))
    screen.blit(vertical_v_text, vertical_v_rect)
    
    horizontal_v_text = font.render(f"Horizontal velocity: {v2:.5f}", True, orange)
    horizontal_v_rect = horizontal_v_text.get_rect(topleft = (300 + info_spacing, info_y))
    pygame.draw.rect(screen, black, horizontal_v_rect.inflate(10, 5))
    screen.blit(horizontal_v_text, horizontal_v_rect)
    
    spaceship_h_text = font.render(f"Altitude: {abs(spaceship_pos[1] - height):.5f}", True, orange)
    spaceship_h_rect = spaceship_h_text.get_rect(topleft = (700 + info_spacing, info_y))
    pygame.draw.rect(screen, black, spaceship_h_rect.inflate(10, 5))
    screen.blit(spaceship_h_text, spaceship_h_rect)
    
    fuel_text = font.render(f"Fuel: {fuel}", True, orange)
    fuel_rect = fuel_text.get_rect(topleft = (1000 + info_spacing, info_y))
    pygame.draw.rect(screen, black, fuel_rect.inflate(10, 5))
    screen.blit(fuel_text, fuel_rect)
    
    if spaceship_pos[0] < -10:
      if spaceship_pos[1] < -10:
        pygame.draw.polygon(screen, white, [[10, 10], [10, 25], [25, 10]])
      else:
        pygame.draw.polygon(screen, white, [[10, spaceship_pos[1]], [25, spaceship_pos[1] - 10], [25, spaceship_pos[1] + 10]])
    
    if spaceship_pos[0] >= width:
      if spaceship_pos[1] < -10:
        pygame.draw.polygon(screen, white, [[width - 10, 10], [width - 10, 25], [width - 25, 10]])
      else:
        pygame.draw.polygon(screen, white, [[width - 10, spaceship_pos[1]], [width - 25, spaceship_pos[1] - 10], [width - 25, spaceship_pos[1] + 10]])
    
    if spaceship_pos[1] < -10 and -10 <= spaceship_pos[0] < width:
      pygame.draw.polygon(screen, white, [[spaceship_pos[0], 10], [spaceship_pos[0] - 10, 25], [spaceship_pos[0] + 10, 25]])
    
    pygame.display.flip()
    clock.tick(fps)

display_info = pygame.display.Info()
width, height = display_info.current_w, display_info.current_h
fps = 60
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (200, 200, 200)
orange = (255, 165, 0)
light_blue = (173, 116, 233)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('E')
font = pygame.font.Font(None, 36)

login()