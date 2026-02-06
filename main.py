import pygame

pygame.init()

WIDTH = 750
HEIGHT = 1200

screen = pygame.display.set_mode((HEIGHT, WIDTH))

start = True
while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            start = False  
    pygame.display.flip()   
