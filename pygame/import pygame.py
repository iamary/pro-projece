import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("GTA 5 ")#heder name
clock = pygame.time.Clock()

surface = pygame.Surface((100,200))
surface.fill('blue')

while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
              pygame.quit()
              exit()
    screen.blit(surface,(0,0))#draw all our element
    # update evetything
    pygame.display.update()
    clock.tick(40)