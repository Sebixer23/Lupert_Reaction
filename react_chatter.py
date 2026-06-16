import time
import pygame
import random 

pygame.init()

screen = pygame.display.set_mode((900, 900))

running = True
font = pygame.font.Font(None, size=52)
times = 0

start_time = pygame.time.get_ticks()
react_started = False
start_time_react = 0
random_react = 0
moving = False
screen_color = 0
good_clicks = 0
begin_start = False
game_over = False
fake_color_list = [4, 4, 4, 5]
bad_clicks = 0
nothing = 0


while running:

    if not game_over:
        screen.fill(pygame.Color("coral3"))

        elapsed = pygame.time.get_ticks() - start_time
        times = max(0, 3 - elapsed // 1000)

        countdown = font.render(f"{times}s", True, (0, 0, 0))
        countdown_rect = countdown.get_rect()
        countdown_rect.center = (450, 450)
        screen.blit(countdown, countdown_rect)

        if times == 0 and not react_started:
            react_started = True
            start_time_react = pygame.time.get_ticks()
            random_react = random.uniform(0.4, 3.9)
            chosen_color = random.choice(fake_color_list)

        if react_started:
            screen.fill(pygame.Color("coral3"))
            elapsed_react = pygame.time.get_ticks() - start_time_react
            wait_text = font.render("Wait...", True, (0, 0, 0))
            wait_text_rect = wait_text.get_rect()
            wait_text_rect.center = (450, 450)
            screen.blit(wait_text, wait_text_rect)
            if chosen_color != 4 and elapsed_react >= random_react * 1000:
                screen.fill(pygame.Color("blue"))
                screen_color = 5
            elif elapsed_react >= random_react * 1000:
                if not begin_start:
                    start = int(time.perf_counter_ns())
                    begin_start = True
                screen.fill(pygame.Color("green"))
                screen_color = 3
        else:
            screen_color = 2

        if good_clicks != 0:
            screen.fill(pygame.Color("purple"))
            screen_color = 4

        elif bad_clicks != 0:
            screen.fill(pygame.Color("red"))
            fail_display = font.render("Fail!", True, (0, 0, 0))
            fail_display_rect = fail_display.get_rect()
            fail_display_rect.center = (450, 450)
            screen.blit(fail_display, fail_display_rect)

        if screen_color == 4:
            result = (end - start) // 1000000
            result_display = font.render(f"You reacted in {result}ms :D", True, (0, 0, 0))
            result_display_rect = result_display.get_rect()
            result_display_rect.center = (450, 450)
            screen.blit(result_display, result_display_rect)
            game_over = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                moving = True
                if screen_color == 3 and moving:
                    end = int(time.perf_counter_ns())
                    good_clicks += 1
                elif screen_color != 3 and moving and react_started:
                    bad_clicks += 1
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                moving = False

    pygame.display.flip()

pygame.quit()