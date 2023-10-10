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

player = pygame.image.load('graphics/player/jump.png').convert_alpha()
player_rect = player.get_rect(midbottom = (80, GROUNDHEIGHT))


def display_score(time_before):
    current_time = int(pygame.time.get_ticks()/1000)
    score = current_time - time_before
    score_surf = text_font.render(f"Score:{score}", True, "Red")
    score_rect = score_surf.get_rect(center=(400, 50))
    return score, score_surf, score_rect


player_acceleration = 0
time_before = 0
score = 0
scorelist = list()
gameOver = True
while True:
    #displays sky, ground, snail and player
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, GROUNDHEIGHT))
    
        
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
        score, score_surf, score_rect = display_score(time_before)
        screen.blit(score_surf,score_rect) 
        #moving snail
        screen.blit(snail_surface, snail_rect)
        snail_rect.x -= 7
        if snail_rect.right < 0: snail_rect.left = 800

        #moving player for jump
        player_acceleration += 1
        player_rect.y += player_acceleration

        #if player on or below ground
        if player_rect.bottom >= 300:
            jumpTimes = 0
            player_rect.bottom = 300
        screen.blit(player, player_rect)

        #collision detection
        if snail_rect.colliderect(player_rect): gameOver = True
            
    if gameOver:
        screen.fill((51, 204, 255))
        scorelist.append(score)
        game_name = text_font.render("Pixel Runner", True, "Green")
        game_name_rect = game_name.get_rect(center = (400, 50))

        player_stand = pygame.transform.rotozoom(pygame.image.load('graphics/player/player_stand.png').convert_alpha(),0,3)
        player_stand_rect = player_stand.get_rect(center=(400, 200))

        message = text_font.render("press space to jump", True, "Green")
        message_rect = message.get_rect(center=(400, 350))

        score_message = text_font.render(f"Score:{score}", True, "Green")
        score_message_rect = score_message.get_rect(center=(400, 350))

        high_score = max(scorelist)
        maxscore_message = text_font.render(f"high score:{high_score}", True, "Red")
        maxscore_message_rect = maxscore_message.get_rect(center=(100, 30))
        screen.blit(game_name, game_name_rect)
        screen.blit(player_stand, player_stand_rect)
        if score == 0: screen.blit(message, message_rect)
        else:
            screen.blit(score_message, score_message_rect)
            screen.blit(maxscore_message, maxscore_message_rect)
        
        time_before = int(pygame.time.get_ticks()/1000)
        snail_rect.left = 800
        

    clock.tick(60)

    pygame.display.update()




    
