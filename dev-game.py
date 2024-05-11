import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((700 , 400))

running = True 
while running: 
    screen.fill((250,250,250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()
    clock.tick(180)
pygame.quit()