import pygame
import random 

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        mole_rect =  mole_image.get_rect(topleft=(0,0))
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()

        #functions 
        def draw_grid():
            for x in range(0, 640, 32):
                pygame.draw.line(screen, "black", (x, 0), (x, 512))
                
            for y in range(0, 512, 32): 
                pygame.draw.line(screen, "black", (0, y), (640, y))
        def move_mole():
            col = random.randrange(0, 20)
            row = random.randrange(0, 16)
            new_x = col * 32
            new_y = row * 32
            mole_rect.topleft = (new_x, new_y)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN: 
                    if mole_rect.collidepoint(event.pos): 
                        move_mole()

            screen.fill("light green")
            draw_grid()
            # where mole goes 
            screen.blit(mole_image, mole_rect)

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
