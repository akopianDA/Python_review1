import pygame
from enum import Enum


pygame.init()
pygame.font.init()


scrren_widht = scrren_height = 720
cell_size = scrren_widht / 15
maxHeightInCells = 14
minHeightInCells = 0
maxWidthInCells = 14
minWidthInCells = 0
freeSpace1 = 6
freeSpace2 = 22
ground = pygame.image.load('images/ground.png')
ground = pygame.transform.scale(ground, (int(cell_size), int(cell_size)))
box = pygame.image.load('images/box.png')
box = pygame.transform.scale(box, (int(cell_size), int(cell_size)))
block = pygame.image.load('images/block.png')
block = pygame.transform.scale(block, (int(cell_size), int(cell_size)))
bombImage = pygame.image.load('images/bomb.png')
bombImage = pygame.transform.scale(bombImage, (int(cell_size * 2), int(cell_size * 2)))
fireImage = pygame.image.load('images/explosion.png')
fireImage = pygame.transform.scale(fireImage, (int(cell_size), int(cell_size)))

f = pygame.font.Font(None, 20)
win = pygame.display.set_mode((scrren_widht, scrren_height))
pygame.display.set_caption("BomberMan")
x = 0.5*cell_size
y = 0.5*cell_size
widht = 40
heigth = 60
speed = 15

units = list()


class Action(Enum):
    bomb = 'bomb'
    left = 'left'
    right = 'right'
    up = 'up'
    down = 'down'


class Surface(Enum):
    ground = 1
    box = 2
    block = 3


class Directions(Enum):
    up = 0
    down = 1
    right = 2
    left = 3
