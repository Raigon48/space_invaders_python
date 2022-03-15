import pygame
shipImg = pygame.image.load('player.png')
from Bullet import Bullet


class SpaceShip():

    def __init__(self, name, positionX, positionY, health) -> None:
        self.name = name
        self.positionX = positionX
        self.positionY = positionY
        self.health = health
        self.shipImg = shipImg
        self.position_change = 0

    def __str__(self) -> str:
        return self.name
    
    def move(self):
        if self.positionX <= 0:
            self.positionX = 0
        if self.positionX >= 736:
            self.positionX = 736
        self.positionX += self.position_change
    
    def move_direction(self, direction):
        if direction == 'LEFT':
            self.position_change = -0.6
        if direction == 'RIGHT':
            self.position_change = 0.6
        if direction == 'NONE':
            self.position_change = 0

    def draw(self, screen):
        screen.blit(shipImg, (self.positionX, self.positionY))
    
    def fire(self, screen):
        bullet = Bullet(5, self.positionX, True)
        while bullet.moving == True:
            bullet.move()
            bullet.draw(screen)
            if bullet.positionY <= 0:
                bullet.moving = False
