import pygame, random, os
from pygame import gfxdraw

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
    ghost = pygame.image.load(os.path.join(asset_path, 'ghost.png'))
    ghost_rect = ghost.get_rect(center=(random.randint(0, 700), random.randint(0, 400)))
    return ghost_rect

def spawn_coin():
    coin_rect = coin_image.get_rect(center=(random.randint(0, 700), random.randint(0, 400)))
    return coin_rect

def draw_window_game():
    global move_count
    if move_count + 1 >= 12:
        move_count = 0
    if not right and not left and not down and not up:
        screen.blit(character, character_rect)
    if right:
        screen.blit(move_right[move_count // 4], character_rect)
        move_count += 1
    if left:
        screen.blit(move_left[move_count // 4], character_rect)
        move_count += 1
    if up:
        screen.blit(move_up[move_count // 4], character_rect)
        move_count += 1
    if down:
        screen.blit(move_down[move_count // 4], character_rect)
        move_count += 1

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

#Load images
asset_path = 'assets'
coin_image = pygame.image.load(os.path.join(asset_path, 'environment_11.png'))
bg = pygame.image.load(os.path.join(asset_path, 'ground_04.png'))
bg_width, bg_height = bg.get_size()
bg = pygame.transform.scale(bg, (bg_width * 2, bg_height * 2))
character = pygame.image.load(os.path.join(asset_path, 'move_down.png'))
ghost_image = pygame.image.load(os.path.join(asset_path, 'ghost.png'))
game_over_image = pygame.image.load(os.path.join(asset_path, 'gameover.png'))
start_game_image = pygame.image.load(os.path.join(asset_path, 'start.png'))

#Resize images
game_over_image = pygame.transform.scale(game_over_image, (500, 100))
start_game_image = pygame.transform.scale(start_game_image, (300, 90))

# Load font
font = pygame.font.Font('MinecraftRegular-Bmg3.ttf', 32)

# Character setup
character_x = 350
character_y = 200
character_rect = character.get_rect(center=(character_x, character_y))

# Character Movement
move_down = [pygame.image.load(os.path.join(asset_path, 'move_down.png')),
             pygame.image.load(os.path.join(asset_path, 'move_down1.png')),
             pygame.image.load(os.path.join(asset_path, 'move_down2.png'))]
move_up = [pygame.image.load(os.path.join(asset_path, 'move_up.png')),
           pygame.image.load(os.path.join(asset_path, 'move_up1.png')),
           pygame.image.load(os.path.join(asset_path, 'move_up2.png'))]
move_right = [pygame.image.load(os.path.join(asset_path, 'move_r.png')),
              pygame.image.load(os.path.join(asset_path, 'move_r1.png')),
              pygame.image.load(os.path.join(asset_path, 'move_r2.png'))]
move_left = [pygame.image.load(os.path.join(asset_path, 'move_l.png')),
             pygame.image.load(os.path.join(asset_path, 'move_l1.png')),
             pygame.image.load(os.path.join(asset_path, 'move_l2.png'))]
right, left, up, down = False, False, False, False
move_count = 0

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
game_started = False
running = True
reset_game()

def draw_background():
    bg_x = max(0, min(character_rect.centerx - screen.get_width() // 2, bg.get_width() - screen.get_width()))
    bg_y = max(0, min(character_rect.centery - screen.get_height() // 2, bg.get_height() - screen.get_height()))
    screen.blit(bg, (0, 0), (bg_x, bg_y, screen.get_width(), screen.get_height()))

def blur_surface(surface, radius):
    if radius < 1:
        return surface
    scale = 1.0 / (2 ** radius)
    surf_size = surface.get_size()
    blur_size = (max(1, int(surf_size[0] * scale)), max(1, int(surf_size[1] * scale)))
    surf = pygame.transform.smoothscale(surface, blur_size)
    surf = pygame.transform.smoothscale(surf, surf_size)
    return surf

def draw_start_button():
    start_button_rect = start_game_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(start_game_image, start_button_rect)
    return start_button_rect

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_SPACE:
                reset_game()
                game_started = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started:
                mouse_pos = event.pos
                if draw_start_button().collidepoint(mouse_pos):
                    game_started = True

    if game_started:
        draw_background()
        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and character_rect.centerx <= 675:
                character_rect.centerx += character_change_movement_speed
                left, up, down = False, False, False
                right = True

            if keys[pygame.K_LEFT] and character_rect.centerx > 20:
                character_rect.centerx -= character_change_movement_speed
                right, up, down = False, False, False
                left = True

            if keys[pygame.K_DOWN] and character_rect.centery <= 375:
                character_rect.centery += character_change_movement_speed
                right, left, up = False, False, False
                down = True

            if keys[pygame.K_UP] and character_rect.centery >= 20:
                character_rect.centery -= character_change_movement_speed
                right, left, down = False, False, False
                up = True

            draw_window_game()
            right, left, up, down = False, False, False, False

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

            # Ghost logic
            for ghost_rect in ghosts:
                screen.blit(ghost_image, ghost_rect)
                ghost_follow(ghost_rect)
                if character_rect.colliderect(ghost_rect):
                    game_over = True

            # Coin logic
            for coin_rect in coins:
                screen.blit(coin_image, coin_rect)
                if character_rect.colliderect(coin_rect):
                    coins.remove(coin_rect)
                    point += 1
                    print(point)

            score_text = font.render('Score: ' + str(point), True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

        else:
            game_over_rect = game_over_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
            screen.blit(game_over_image, game_over_rect)

            final_score_text = font.render('Final Score: ' + str(point), True, (255, 255, 255))
            final_score_rect = final_score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
            screen.blit(final_score_text, final_score_rect)

            high_score_text = font.render('High Score: ' + str(high_score), True, (255, 255, 255))
            high_score_rect = high_score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))
            screen.blit(high_score_text, high_score_rect)
    else:
        blurred_bg = blur_surface(bg, 5)
        screen.blit(blurred_bg, (0, 0))
        draw_start_button()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
