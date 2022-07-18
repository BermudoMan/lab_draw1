import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

#Colors
white = [255, 255, 255]
red = [255, 0, 0]
black = [0, 0, 0]
green = [0, 128, 0]
blue = [0, 0, 128]

screen.fill(black)

circle(screen, white, (200, 200), 150)
circle(screen, green, (250, 170), 35)
circle(screen, green, (150, 170), 35)
circle(screen, black, (250, 170), 15)
circle(screen, black, (150, 170), 15)

rect(screen, black, (150, 260, 100 , 15))

line(screen, red, [110, 100],[190, 150], 6)
line(screen, red, [210, 150],[290, 100], 6)




pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()