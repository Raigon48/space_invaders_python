import math
import pygame
import random
from pygame import mixer

# initialize pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
backgroundImg = pygame.image.load('background.png')
mixer.music.load('background.wav')
mixer.music.play(-1)

pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
player_X = 370
player_Y = 480
playerX_change = 0

enemyImg = []
enemy_X = []
enemy_Y = []
enemyX_change = []
enemyY_change = []

for i in range(6):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemy_X.append(random.randint(0, 735))
    enemy_Y.append(random.randint(50, 150))
    enemyX_change.append(0.5)
    enemyY_change.append(64)

bulletImg = pygame.image.load('bullet.png')
bullet_X = 0
bullet_Y = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = 'ready'


def player(x=player_X, y=player_Y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x+16, y+10))


def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow((bulletX - enemyX), 2) +
                         math.pow((bulletY - enemyY), 2))
    if distance < 27:
        return True
    else:
        return False


running = True
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

game_over_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over():
    text = game_over_font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(text, (200, 250))


def display_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Game loop
while running:
    screen.fill((0, 0, 0))
    screen.blit(backgroundImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.6
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.6
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bullet_X = player_X
                    fire(bullet_X, bullet_Y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    player_X += playerX_change
    if player_X <= 0:
        player_X = 0
    if player_X >= 736:
        player_X = 736
    player(player_X, player_Y)

    if bullet_Y <= 0:
        bullet_Y = 480
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire(bullet_X, bullet_Y)
        bullet_Y -= bulletY_change

    for i in range(6):
        if enemy_Y[i] >= 480:
            for j in range(6):
                enemy_Y[j] = 2000
            game_over()
            break

        isCollision = collision(enemy_X[i], enemy_Y[i], bullet_X, bullet_Y)
        if isCollision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bullet_Y = 480
            bullet_state = 'ready'
            enemy_X[i] = random.randint(0, 735)
            enemy_Y[i] = random.randint(50, 150)
            score_value += 1
            print(score_value)

        if enemy_X[i] >= 736:
            enemyX_change[i] = -0.5
            enemy_Y[i] += enemyY_change[i]
        elif enemy_X[i] <= 0:
            enemyX_change[i] = 0.5
            enemy_Y[i] += enemyY_change[i]

        enemy_X[i] += enemyX_change[i]
        enemy(enemy_X[i], enemy_Y[i], i)

    display_score(textX, textY)

    pygame.display.update()
