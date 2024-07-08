# Example file showing a basic pygame "game loop"
import pygame
from pygame import Rect


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

dt = 0
bat_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ball_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
mouse_prev = pygame.mouse.get_pos()
ball_x_mode = '+'
ball_y_mode = '+'
ball_speed = 750
ball_radius = 15
bat_x_speed = 1000
bat_y_speed = 200
bat_width = 100
bat_height = 20

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE

    bat_rect = pygame.draw.rect(screen, "red", Rect(bat_pos.x, bat_pos.y, bat_width, bat_height))
    ball_rect = pygame.draw.circle(screen, 'blue', (ball_pos.x, ball_pos.y), ball_radius)

    if bat_rect.colliderect(ball_rect):
        if ball_y_mode == '+':
            ball_y_mode = '-'
            ball_pos.y -= ball_radius * 2
        elif ball_y_mode == '-':
            ball_y_mode = '+'
            ball_pos.y += ball_radius * 2

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        bat_pos.y -= bat_y_speed * dt
    if keys[pygame.K_s]:
        bat_pos.y += bat_y_speed * dt
    if keys[pygame.K_a]:
        bat_pos.x -= bat_x_speed * dt
    if keys[pygame.K_d]:
        bat_pos.x += bat_x_speed * dt

    if ball_pos.x <= 0:
        ball_x_mode = '+'
    elif ball_pos.x >= screen.get_width():
        ball_x_mode = '-'

    if ball_pos.y <= 0:
        ball_y_mode = '+'
    elif ball_pos.y >= screen.get_height():
        ball_y_mode = '-'

    if ball_x_mode == '+':
        ball_pos.x += ball_speed * dt
    elif ball_x_mode == '-':
        ball_pos.x -= ball_speed * dt

    if ball_y_mode == '+':
        ball_pos.y += ball_speed * dt
    elif ball_y_mode == '-':
        ball_pos.y -= ball_speed * dt

    if pygame.mouse.get_pos() != mouse_prev:
        bat_pos.x = pygame.mouse.get_pos()[0]
        bat_pos.y = pygame.mouse.get_pos()[1]
    mouse_prev = pygame.mouse.get_pos()
    # flip() the display to put your work on screen
    pygame.display.flip()

    dt = clock.tick(240) / 1000

pygame.quit()