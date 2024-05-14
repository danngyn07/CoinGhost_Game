import pygame , random 
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((700 , 400))
def ghost_follow():
    if character_rect.centerx > ghost_rect.centerx:
        ghost_rect.centerx += 1
    if character_rect.centerx < ghost_rect.centerx:
        ghost_rect.centerx -= 1
    if character_rect.centery > ghost_rect.centery:
        ghost_rect.centery += 1
    if character_rect.centery < ghost_rect.centery:
        ghost_rect.centery -= 1
def spawn_ghost():
    ghost = pygame.image.load('ghost.png')
    ghost_rect = ghost.get_rect(center=(random.randint(0, 700), random.randint(0, 400)))
    return ghost_rect
def spawn_coin():
    coin = pygame.image.load('environment_11.png')
    coin_rect = coin.get_rect(center = (random.randint(0,700) , random.randint(0,400)))
    return coin_rect

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
ghosts = []
ghost_spawn_timer = 5000  # Thời gian đếm cho việc xuất hiện con ma
ghost_spawn_interval = 5000
#coin 
coin = pygame.image.load('environment_11.png')
coin_x = random.randint(0 , 700)
coin_y = random.randint(0 , 400)
coin_rect = coin.get_rect(center = (coin_x , coin_y))
coins = []
coin_spawn_timer = 2000
coin_spawn_interval = 2000
#diem so
point = 0
#khai bao thong tin game
character_change_movement_speed = 2
running = True 

while running: 
    #cai dat nen
    screen.blit(bg , (0, 0))
    
    #cai dat nhan vat
    screen.blit(character , character_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #character movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and character_rect.centerx <= 675:
        character_rect.centerx += character_change_movement_speed
        screen.blit(pygame.transform.rotate(character , 90) , character_rect)
    if keys[pygame.K_LEFT] and character_rect.centerx > 20:
        character_rect.centerx -= character_change_movement_speed
        screen.blit(pygame.transform.rotate(character , -90) , character_rect)
    if keys[pygame.K_DOWN] and character_rect.centery <= 375: 
        character_rect.centery += character_change_movement_speed
    if keys[pygame.K_UP] and character_rect.centery >= 20:
        character_rect.centery -= character_change_movement_speed
        screen.blit(pygame.transform.rotate(character , 180) , character_rect)
    #spawn_ghost
    ghost_spawn_timer += clock.get_rawtime()
    if ghost_spawn_timer >= ghost_spawn_interval and len(ghosts) < 4:
        ghosts.append(spawn_ghost())
        ghost_spawn_timer = 0
    coin_spawn_timer += clock.get_rawtime()
    if coin_spawn_timer >= coin_spawn_interval and len(coins) <=5:
        coins.append(spawn_coin())
        coin_spawn_timer = 0
    #tao logic cho con ma
    for ghost_rect in ghosts:
        screen.blit(pygame.image.load('ghost.png'), ghost_rect)
        # Di chuyển con ma đến nhân vật
        ghost_follow()
        
    #tao coin
    length_coins = len(coins)
    for coin_rect in coins:
        screen.blit(pygame.image.load('environment_11.png') , coin_rect)
        collide = pygame.Rect.colliderect(character_rect , coin_rect)
        if collide:
            del coins[coins.index(coin_rect)]
            point += 1
            print(point)
    # ghost_follow()
    pygame.display.update()
    clock.tick(180)
pygame.quit()