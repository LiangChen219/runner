import pygame
import sys
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Stupid')
clock = pygame.time.Clock()

player_surface = pygame.image.load('graphics/player/jump.png')
snail_surface = pygame.image.load('graphics/snail/snail1.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        screen.blit(player_surface, (0, 0))
        screen.blit(snail_surface, (400, 0))
        
    pygame.display.update()
