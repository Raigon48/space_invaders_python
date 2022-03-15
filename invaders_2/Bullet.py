import pygame

bulletImg = pygame.image.load('bullet.png')

class Bullet():
  def __init__(self, power, positionX, moving=False):
    self.power = power
    self.positionX = positionX
    self.positionY = 480
    self.bulletImg = bulletImg
    self.moving = moving
  
  def __str__(self):
    return f"Bullet({self.power})"
  
  def draw(self, screen):
    screen.blit(bulletImg, (self.positionX, self.positionY))
  
  def move(self):
    self.positionY -= 0.01