import pygame
pygame.init()

screen = pygame.display.set_mode((400 , 650))

running = True 
while running: 
    screen.blit((0 , 0 , 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()

pygame.quit()