import pygame
from SpaceShip import SpaceShip


def run():
    running = True

    FPS = pygame.time.Clock()


    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    backgroundImg = pygame.image.load('background.png')

    while running:
        screen.fill((0, 0, 0))
        screen.blit(backgroundImg, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_direction('LEFT')
                if event.key == pygame.K_RIGHT:
                    player.move_direction('RIGHT')
                if event.key == pygame.K_SPACE:
                    player.fire(screen)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.move_direction('NONE')
        
        player.move()
        player.draw(screen)
        pygame.display.update()
        FPS.tick(30)


if __name__ == '__main__':
    player = SpaceShip("Player", 370, 480, 100)
    run()
