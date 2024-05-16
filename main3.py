import pygame, random

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((700, 400))

def ghost_follow(ghost_rect):
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
    coin_rect = coin_image.get_rect(center=(random.randint(0, 700), random.randint(0, 400)))
    return coin_rect

def Character_movement():
    global move_Count
    if move_Count + 1 >= 12:
        move_Count = 0
    if right != True and left != True and down != True and up != True:
        screen.blit(character , character_rect)
    if right:
        screen.blit(move_right[move_Count//4] , character_rect)
        move_Count += 1
    if left:
        screen.blit(move_left[move_Count//4] , character_rect)
        move_Count += 1
    if up:
        screen.blit(move_up[move_Count//4] , character_rect)
        move_Count += 1
    if down:
        screen.blit(move_down[move_Count//4] , character_rect)
        move_Count += 1

def reset_game():
    global character_rect, ghosts, coins, point, ghost_spawn_timer, coin_spawn_timer, game_over, high_score
    character_rect = character.get_rect(center=(350, 200))
    ghosts = []
    coins = []
    if point > high_score:
        high_score = point
    point = 0
    ghost_spawn_timer = 0
    coin_spawn_timer = 0
    game_over = False

# Load images
coin_image = pygame.image.load('environment_11.png')
bg = pygame.image.load('ground_04.png')
bg_width, bg_height = bg.get_size()
character = pygame.image.load('move_down.png')
bg = pygame.transform.scale(bg, (bg_width * 2, bg_height * 2))  # Phóng to nền
ghost_image = pygame.image.load('ghost.png')
game_over_image = pygame.image.load('gameover.png')

# Resize game over image
game_over_image = pygame.transform.scale(game_over_image, (400, 200))  

# Load font
font = pygame.font.Font('freesansbold.ttf', 32)  

# Character setup
character_x = 350
character_y = 200
character_rect = character.get_rect(center=(character_x, character_y))

# Character Movement
move_down = [pygame.image.load('move_down.png') , pygame.image.load('move_down1.png') ,pygame.image.load('move_down2.png')]
move_up = [pygame.image.load('move_up.png') , pygame.image.load('move_up1.png') , pygame.image.load('move_up2.png')]
move_right = [pygame.image.load('move_r.png') , pygame.image.load('move_r1.png') , pygame.image.load('move_r2.png')]
move_left = [pygame.image.load('move_l.png') ,pygame.image.load('move_l1.png') , pygame.image.load('move_l2.png')]
right , left  , up , down = False , False , False , False
move_Count = 0

# Ghost setup
ghosts = []
ghost_spawn_timer = 0
ghost_spawn_interval = 5000

# Coin setup
coins = []
coin_spawn_timer = 0
coin_spawn_interval = 2000

# Score
point = 0
high_score = 0

# Game setup
character_change_movement_speed = 2
game_over = False
running = True
reset_game()

def draw_background():
    bg_x = max(0, min(character_rect.centerx - screen.get_width() // 2, bg.get_width() - screen.get_width()))
    bg_y = max(0, min(character_rect.centery - screen.get_height() // 2, bg.get_height() - screen.get_height()))
    screen.blit(bg, (0, 0), (bg_x, bg_y, screen.get_width(), screen.get_height()))
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_background()
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and character_rect.centerx <= 675:
            character_rect.centerx += character_change_movement_speed
            left , up , down = False , False , False   
            right = True
        
        if keys[pygame.K_LEFT] and character_rect.centerx > 20:
            character_rect.centerx -= character_change_movement_speed
            right , up , down = False,False ,False 
            left = True
            
        if keys[pygame.K_DOWN] and character_rect.centery <= 375:
            character_rect.centery += character_change_movement_speed
            right , left , up = False,False ,False 
            down = True
            
        if keys[pygame.K_UP] and character_rect.centery >= 20:
            character_rect.centery -= character_change_movement_speed
            right , left , down = False , False , False 
            up = True
        
    
        Character_movement()
        right , left  , up , down = False , False , False , False  
         # Spawn ghosts
        ghost_spawn_timer += clock.get_time()
        if ghost_spawn_timer >= ghost_spawn_interval and len(ghosts) < 4:
            ghosts.append(spawn_ghost())
            ghost_spawn_timer = 0

        # Spawn coins
        coin_spawn_timer += clock.get_time()
        if coin_spawn_timer >= coin_spawn_interval and len(coins) <= 5:
            coins.append(spawn_coin())
            coin_spawn_timer = 0

        #Ghost logic
        for ghost_rect in ghosts:
            screen.blit(ghost_image, ghost_rect)
            ghost_follow(ghost_rect)
            if character_rect.colliderect(ghost_rect):
                game_over = True

        #Coin logic
        for coin_rect in coins:
            screen.blit(coin_image, coin_rect)
            if character_rect.colliderect(coin_rect):
                coins.remove(coin_rect)
                point += 1

        score_text = font.render('Score: ' + str(point), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    else:
        game_over_rect = game_over_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(game_over_image, game_over_rect)

        final_score_text = font.render('Final Score: ' + str(point), True, (255, 255, 255))
        final_score_rect = final_score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
        screen.blit(final_score_text, final_score_rect)
        
        high_score_text = font.render('High Score: ' + str(high_score), True, (255, 255, 255))
        high_score_rect = high_score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))
        screen.blit(high_score_text, high_score_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()

    pygame.display.update()
    clock.tick(50)

pygame.quit()
