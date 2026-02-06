import pygame

pygame.init()

WIDTH = 750
HEIGHT = 1200

screen = pygame.display.set_mode((HEIGHT, WIDTH))

def show_start_screen():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                start = False  
        window.blit(start_image, (0, 0)) 
        pygame.display.flip()   