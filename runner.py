import pygame
import sys
#initialises pygame
pygame.init()
snailXpos = 800
#creates display surface
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
text_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/Ground.png')
text_surface = text_font.render('My Game', False, 'Red')
snail_surface = pygame.image.load('graphics/snail/snail1.png')
player_surface = pygame.image.load('graphics/player/jump.png')
while True:
    snailXpos -= 4 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #places a regular surface over a display surface
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (350, 50))
    screen.blit(snail_surface, (snailXpos, 270))
    screen.blit(player_surface, (100, 220))
    pygame.display.update()
    
    clock.tick(60)
