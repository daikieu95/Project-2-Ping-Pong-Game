"""
CPSC 386 - Ping Pong Game
Create a Pong game for 2 players
Player 1 Movement Keys: Arrows Keys
Player 2 Movement Keys: W A S D
Name: DAI KIEU
"""
import sys
import pygame


def check_key_down_event(event):
    if event.key == pygame.K_q:
        sys.exit()


def check_events(stats, buttons, click):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_buttons_down(buttons, mouse_x, mouse_y, click)
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_buttons_up(stats, buttons, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_key_down_event(event)


def update_screen(ai_s, screen, buttons, title):
    screen.fill(ai_s.bg_color)
    title.draw_button()
    for button in buttons:
        button.draw_button()
    pygame.display.flip()


def check_buttons_up(stats, buttons, mouse_x, mouse_y):
    button = get_button(buttons, mouse_x, mouse_y)
    if button == buttons[0]:
        stats.game_active = True
        pygame.mouse.set_visible(False)
        pygame.mixer.music.load("sounds/background.wav")
        pygame.mixer.music.play(-1)


def check_buttons_down(buttons, mouse_x, mouse_y, click):
    button = get_button(buttons, mouse_x, mouse_y)
    if button:
        click.play()


def get_button(buttons, mouse_x, mouse_y):
    for button in buttons:
        clicked = button.rect.collidepoint(mouse_x, mouse_y)
        if clicked:
            return button





