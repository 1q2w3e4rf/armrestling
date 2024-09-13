import pygame
import random


pygame.init()


screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))


rek1_key = pygame.K_SPACE
rek2_key = pygame.MOUSEBUTTONDOWN
click_speed = 10
win_threshold = 100


rek1_score = 0
rek2_score = 0
rek1_click_speed = 0
rek2_click_speed = 0
game_over = False
winner_image = None
winner_image_time = 0


rek1_image = pygame.image.load('1.png')
rek2_image = pygame.image.load('2.png')
rek1_win_image = pygame.image.load('3.png')
rek2_win_image = pygame.image.load('4.png')
tie_image = pygame.image.load('5.png')


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == rek1_key:
                rek1_click_speed += 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                rek2_click_speed += 1


    screen.fill((255, 255, 255))


    if winner_image:
        screen.blit(winner_image, (0, 0))
        winner_image_time += 1 / 60
        if winner_image_time >= 5:
            winner_image = None
            winner_image_time = 0
            rek1_score = 0
            rek2_score = 0
    else:
        if rek1_score > rek2_score:
            screen.blit(rek1_image, (0, 0))
        elif rek2_score > rek1_score:
            screen.blit(rek2_image, (0, 0))
        elif rek1_score == rek2_score:
            screen.blit(tie_image, (0, 0))


        font = pygame.font.Font(None, 36)
        text = font.render(f"Rek 1: {rek1_score} | Rek 2: {rek2_score}", True, (0, 0, 0))
        screen.blit(text, (100, 100))


        if rek1_click_speed > rek2_click_speed:
            rek1_score += 1
            rek1_click_speed = 0
            rek2_click_speed = 0
        elif rek2_click_speed > rek1_click_speed:
            rek2_score += 1
            rek1_click_speed = 0
            rek2_click_speed = 0


        if rek1_score >= win_threshold:
            winner_image = rek1_win_image
        elif rek2_score >= win_threshold:
            winner_image = rek2_win_image


    pygame.display.flip()
    pygame.time.Clock().tick(60)


pygame.quit()