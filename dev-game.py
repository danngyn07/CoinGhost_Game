import pygame , random
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((700 , 400))
#nen
bg = pygame.image.load('ground_04.png')
#khai bao nhan vat
character = pygame.image.load('playerFace_dark.png')
character_x = 350
character_y = 200
character_rect = character.get_rect(center = (character_x,character_y))
#ma
ghost = pygame.image.load('ghost.png')
ghost_x = random.randint(0,700)
ghost_y = random.randint(0,400)
ghost_rect = ghost.get_rect(center = (ghost_x , ghost_y))
#coin 
coin = pygame.image.load('environment_11.png')
coin_x = random.randint(0 , 700)
coin_y = random.randint(0 , 400)
coin_rect = coin.get_rect(center = (coin_x , coin_y))
#khai bao thong tin game
character_change_movement_speed = 2
running = True 
while running: 
    #cai dat nen
    screen.blit(bg , (0, 0))
    #cai dat ma
    screen.blit(ghost , ghost_rect)
    #cai dat coin
    screen.blit(coin , coin_rect)
    #cai dat nhan vat
    screen.blit(character , character_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #character movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and character_rect.centerx <= 675:
        character_rect.centerx += character_change_movement_speed
    if keys[pygame.K_LEFT] and character_rect.centerx > 20:
        character_rect.centerx -= character_change_movement_speed
    if keys[pygame.K_DOWN] and character_rect.centery <= 375: 
        character_rect.centery += character_change_movement_speed
    if keys[pygame.K_UP] and character_rect.centery >= 20:
        character_rect.centery -= character_change_movement_speed
    
    

    pygame.display.update()
    clock.tick(180)
pygame.quit()