import pygame
from pygame.draw import *
import numpy

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 400))

#Colors
white = [255, 255, 255]
red = [255, 0, 0]
black = [0, 0, 0]
green = [0, 128, 0]
blue = [0, 0, 128]
yellow = [255, 165, 0]
water = [0, 255, 255]

screen.fill(blue)

rect(screen, yellow, (0, 300, 600, 300))
rect(screen, water, (0, 150, 600, 150))
polygon(screen, black, [(50, 270), (20, 210), (250, 210), (200 ,270)])
rect(screen, black, (120, 80, 10, 130))
arc(screen, white, (90, 80, 80, 115), numpy.pi*3/2, numpy.pi/2, width=300)
circle(screen, white, (500, 50), 40)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()