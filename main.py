import pygame, time, random
from pygame.locals import *

def main():
    #********** Game variables **********
    quit = False
    x = 50
    y = 650
    #********** Start game loop **********
    while not quit:
        window.fill((5,5,5))                            
        #********** Process events **********
        keyspressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                quit = True
        # --------- Directions ---------
            if keyspressed[ord("d")]:
                x = x + 30

            if keyspressed[ord("q")]:
                x = x - 30

            if keyspressed[ord("z")]:
                y = y - 30

            if keyspressed[ord("s")]:
                y = y + 30

        # --------- Side collision ---------
        
        if x <= 0:
            x = 0

        if x >= window.get_width() - 30:
            x = window.get_width() - 30

        if y <= 0:
            y = 0

        if y >= window.get_height() - 80:
            y = window.get_height() - 80
        #********** Your game logic here **********
        

        player = (x, y, 30, 50)

        pygame.draw.rect(window, (15, 66, 150), player)

        pygame.draw.rect(window, (0, 150, 0), (0, 700, 1200, 50))



        #********** Update screen **********
        pygame.display.update()                         # Actually does the screen update
        clock.tick(35)                                  # Run the game at 25 frames per second

#********** Initialise & run the game **********
if __name__ == "__main__":
    width, height = 1200, 750                           # Set screen width,height
    pygame.init()                                       # Start graphics system
    pygame.mixer.init()                                 # Start audio system
    window = pygame.display.set_mode((width, height))   # Create window
    clock = pygame.time.Clock()                         # Create game clock
    main()
    pygame.quit()
