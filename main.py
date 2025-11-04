import pygame

pygame.init()
pygame.display.set_mode((600,300))
pygame.display.set_caption("title")
icon = pygame.image.load("image.png")
pygame.display.set_icon(icon)

run = True
while run:

  pygame.display.update()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      pygame.quit()

  
