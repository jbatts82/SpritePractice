###############################################################################
# File Name  : main.py
# Date       : 11/12/2022
# Description: Sprite Ideas
###############################################################################

import pygame
import sys
import random


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("laser.wav")

    def shoot(self):
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


# Initialization
pygame.init()
clock = pygame.time.Clock()

# Game Screen
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("simple_bg.png")
pygame.mouse.set_visible(False)

# Crosshair
crosshair = Crosshair('crosshair_outline_small.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Target
target_group = pygame.sprite.Group()
for target in range(3):
    new_target = Target("sam.png", random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)

if __name__ == '__main__':
    print("Hello Mario!")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shoot()

        pygame.display.flip()
        screen.blit(background, (0, 0))
        target_group.draw(screen)
        crosshair_group.draw(screen)
        crosshair_group.update()
        clock.tick(60)