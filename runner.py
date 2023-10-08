import pygame
import sys

GROUNDHEIGHT = 300
#initialises pygame and creates display surface
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')

clock = pygame.time.Clock()

#loading images and texts
sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/Ground.png').convert_alpha()

text_font = pygame.font.Font('font/Pixeltype.ttf', 50)


snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (800, GROUNDHEIGHT))

player_surface = pygame.image.load('graphics/player/jump.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, GROUNDHEIGHT))

def display_score(time_before):
    current_time = int(pygame.time.get_ticks()/100)
    score_surface = text_font.render(f'{current_time-time_before}', True, 'Red')
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
player_acceleration = 0
time_before = 0
gameOver = False
while True:
    #displays sky, ground, snail and player
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, GROUNDHEIGHT))
    display_score(time_before)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if gameOver == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    #double jump
                    if jumpTimes <= 1:
                        #jump
                        player_acceleration = -15
                        jumpTimes += 1
        #game is over
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    gameOver = False 
                
    if gameOver == False:   
        #moving snail
        screen.blit(snail_surface, snail_rect)
        snail_rect.x -= 4
        if snail_rect.right < 0: snail_rect.left = 800

        #moving player for jump
        player_acceleration += 1
        player_rect.y += player_acceleration

        #if player on or below ground
        if player_rect.bottom >= 300:
            jumpTimes = 0
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        #collision detection
        if snail_rect.colliderect(player_rect):
            gameOver = True
    else:
        screen.fill('Yellow')
        replay = text_font.render('Return button to play again', True, 'Red')
        replay_rect = replay.get_rect(center = (400, 50))
        screen.blit(replay, replay_rect)
        time_before = int(pygame.time.get_ticks()/100)
        snail_rect.left = 800
        

    clock.tick(60)

    pygame.display.update()




    
