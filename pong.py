"""
CPSC 386 - Ping Pong Game
Create a Pong game for 2 players
Player 1 Movement Keys: Arrows Keys
Player 2 Movement Keys: W A S D
Name: DAI KIEU
"""
import pygame
from pygame.sprite import Group

from settings import Settings

from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from paddlebot import Paddle_Bot
from paddletop import Paddle_Top
from paddleside import Paddle_Side
from ai_pad_bot import AI_Paddle_Bot
from ai_pad_top import AI_Paddle_Top
from ai_pad_side import AI_Paddle_Side
from ball import Ball
import game_functions as gf
import menu_functions as mf


def menu_music_play():
    pygame.mixer.music.load("sounds/8bitsmisc.wav")
    pygame.mixer.music.play(-1)


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Pong AI without Walls")

    # Create a Menu for the Game
    black = (0, 0, 0)
    green = (0, 200, 0)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    click = pygame.mixer.Sound('sounds/click.wav')
    ai_s = Settings()
    down = Button(ai_s, screen, '..more', 200, 40, 300, 300, green, blue, 40)    # The More button
    title = Button(ai_s, screen, 'Pong AI without Walls', 600, 200, 0, -(ai_s.screen_height / 2) + 150, black, green, 120)
    game_o = Button(ai_s, screen, 'Game Over', 200, 40, 0, 0, blue, green, 60)
    back = Button(ai_s, screen, '<-', 40, 40, 600, -330, green, blue, 48)
    play = Button(ai_s, screen, 'PLAY', 200, 40, 0, -10, green, red, 48)
    buttons = [play, back]

    # Create an instance to store game statistics, and a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make the Menu playing Music
    menu_music_play()

    # Make Player-Paddles
    paddlebot = Paddle_Bot(ai_settings, screen)
    paddletop = Paddle_Top(ai_settings, screen)
    paddleside = Paddle_Side(ai_settings, screen)

    # Make AI-Paddles
    ai_paddlebot = AI_Paddle_Bot(ai_settings, screen)
    ai_paddletop = AI_Paddle_Top(ai_settings, screen)
    ai_paddleside = AI_Paddle_Side(ai_settings, screen)

    # Make a Ball
    ball = Ball(ai_settings, screen)

    # Make a group to store dashline in.
    dashline = Group()

    # Create the fleet of aliens
    gf.create_dashlines(ai_settings, screen, dashline)
    # Start the main loop for the game.
    while True:
        if not stats.game_active:
            mf.check_events(stats, buttons, click)

            mf.update_screen(ai_settings, screen, buttons, title)

        if stats.game_active:
            gf.check_events(ai_settings, screen, stats, sb, paddlebot, paddletop, paddleside, dashline, ai_paddlebot, ai_paddletop, ai_paddleside)
            gf.serve_ball(ai_settings, screen)
            ball.update(stats)
            if ball.off_screen():        # someone scored
                if ball.rect.x > screen.get_rect().x:
                    stats.ai_score += 1
                else:
                    stats.player_score += 1

                sb.prep_score()
                sb.show_score()

                if (stats.ai_score >= sb.winning_score or stats.player_score >= sb.winning_score or stats.player_score >= sb.winning_score):
                    sb.show_winner(stats)

                del ball

            gf.collide_check_1(ai_settings, ball, paddleside)
            gf.collide_check_2(ai_settings, ball, ai_paddleside)
            gf.collide_check_3(ai_settings, ball, ai_paddlebot)
            gf.collide_check_4(ai_settings, ball, paddlebot)
            gf.collide_check_5(ai_settings, ball, paddletop)
            gf.collide_check_6(ai_settings, ball, ai_paddletop)

            paddlebot.update()
            paddletop.update()
            paddleside.update()
            ai_paddlebot.update()
            ai_paddletop.update()
            ai_paddleside.update()

            gf.update_screen(ai_settings, screen, stats, sb, paddlebot, paddletop, paddleside, dashline, ai_paddlebot, ai_paddletop, ai_paddleside, ball)


run_game()
