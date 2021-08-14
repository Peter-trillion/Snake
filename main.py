import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((500, 500))
snake_init_pos = [[250, 250], [240, 250], [230, 250], [220, 250]]
head_pos = [250, 250]
def main():
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.update()
        
if __name__ == '__main__':
    main()