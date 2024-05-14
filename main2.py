import pygame, random, math

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

def avoid_other_ghosts(ghost_rect, ghosts):
    for other_ghost in ghosts:
        if other_ghost != ghost_rect:
            distance = math.dist(ghost_rect.center, other_ghost.center)
            if distance < 50:  # Adjust the minimum distance as needed
                if ghost_rect.centerx > other_ghost.centerx:
                    ghost_rect.centerx += 1
                else:
                    ghost_rect.centerx -= 1
                if ghost_rect.centery > other_ghost.centery:
                    ghost_rect.centery += 1
                else:
                    ghost_rect.centery -= 1

def spawn_ghost(ghosts):
    ghost = pygame.image.load('ghost.png')
    while True:
        ghost_rect = ghost.get_rect(center=(random.randint(0, 700), random.randint(0, 400)))
        if all(math.dist(ghost_rect.center, other_ghost.center) > 50 for other_ghost in ghosts):
            break
    return ghost_rect

def spawn_coin():
    coin = pygame.image.load('environment_11.png')
    coin_rect = coin.get_rect(center=(random.randint(0, 700), random.randint(0, 400)))
    return coin_rect

# Background
bg = pygame.image.load('ground_04.png')

# Character setup
character = pygame.image.load('playerFace_dark.png')
character_x = 350
character_y = 200
character_rect = character.get_rect(center=(character_x, character_y))

# Ghost setup
ghosts = []
ghost_spawn_timer = 5000
ghost_spawn_interval = 5000

# Coin setup
coins = []
coin_spawn_timer = 2000
coin_spawn_interval = 2000

# Score
point = 0

# Game setup
character_change_movement_speed = 2
running = True

while running:
    # Background
    screen.blit(bg, (0, 0))

    # Character
    screen.blit(character, character_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Character movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and character_rect.centerx <= 675:
        character_rect.centerx += character_change_movement_speed
    if keys[pygame.K_LEFT] and character_rect.centerx > 20:
        character_rect.centerx -= character_change_movement_speed
    if keys[pygame.K_DOWN] and character_rect.centery <= 375:
        character_rect.centery += character_change_movement_speed
    if keys[pygame.K_UP] and character_rect.centery >= 20:
        character_rect.centery -= character_change_movement_speed

    # Spawn ghosts
    ghost_spawn_timer += clock.get_rawtime()
    if ghost_spawn_timer >= ghost_spawn_interval and len(ghosts) < 4:
        ghosts.append(spawn_ghost(ghosts))
        ghost_spawn_timer = 0

    # Spawn coins
    coin_spawn_timer += clock.get_rawtime()
    if coin_spawn_timer >= coin_spawn_interval and len(coins) <= 5:
        coins.append(spawn_coin())
        coin_spawn_timer = 0

    # Ghost logic
    for ghost_rect in ghosts:
        screen.blit(pygame.image.load('ghost.png'), ghost_rect)
        ghost_follow(ghost_rect)
        avoid_other_ghosts(ghost_rect, ghosts)
        
    # Coin logic
    for coin_rect in coins:
        screen.blit(pygame.image.load('environment_11.png'), coin_rect)
        collide = pygame.Rect.colliderect(character_rect, coin_rect)
        if collide:
            coins.remove(coin_rect)
            point += 1
            print(point)

    pygame.display.update()
    clock.tick(120)

pygame.quit()
