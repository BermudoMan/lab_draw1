import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 400))

# Colors
white = [255, 255, 255]
red = [255, 0, 0]
black = [0, 0, 0]
green = [0, 128, 0]
blue = [0, 0, 128]
yellow = [255, 165, 0]
water = [0, 255, 255]

screen.fill(blue)


def draw_bird(screen, bird_head, bird_body, bird_tail, bird_wing, beak):
    pygame.draw.polygon(screen, water, beak, 0)
    pygame.draw.circle(screen, yellow, bird_head, 10)
    pygame.draw.ellipse(screen, yellow, bird_body, 0)
    pygame.draw.polygon(screen, yellow, bird_tail, 0)
    pygame.draw.polygon(screen, black, bird_wing, 0)

draw_bird(screen, bird_head, bird_body, bird_tail, bird_wing, beak)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()