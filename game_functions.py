"""
CPSC 386 - Ping Pong Game
Create a Pong game for 2 players
Player 1 Movement Keys: Arrows Keys
Player 2 Movement Keys: W A S D
Name: DAI KIEU
"""

import sys
import random
import pygame
from dashline import DashLine
from ball import Ball
from vector import Vector


def background_music():
    pygame.mixer.music.load("sounds/space invader.wav")
    pygame.mixer.music.play(-1)


def stop_music():
    """stop currently playing music"""
    pygame.mixer.music.stop()


def check_keydown_events(event, ai_settings, screen, paddlebot, paddletop, paddleside, ai_paddlebot, ai_paddletop, ai_paddleside):
    """Respond to keypresses."""
    # Player 1 movement keys
    if event.key == pygame.K_RIGHT:
        paddlebot.moving_right = True
        paddletop.moving_right = True
    elif event.key == pygame.K_LEFT:
        paddlebot.moving_left = True
        paddletop.moving_left = True
    elif event.key == pygame.K_DOWN:
        paddleside.moving_down = True
    elif event.key == pygame.K_UP:
        paddleside.moving_up = True

    # Player 2 movement keys
    elif event.key == pygame.K_d:
        ai_paddlebot.moving_right = True
        ai_paddletop.moving_right = True
    elif event.key == pygame.K_a:
        ai_paddlebot.moving_left = True
        ai_paddletop.moving_left = True
    elif event.key == pygame.K_s:
        ai_paddleside.moving_down = True
    elif event.key == pygame.K_w:
        ai_paddleside.moving_up = True

    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, paddlebot, paddletop, paddleside, ai_paddlebot, ai_paddletop, ai_paddleside):
    """Respond to key releases."""
    # Player 1 movement keys
    if event.key == pygame.K_RIGHT:
        paddlebot.moving_right = False
        paddletop.moving_right = False
    elif event.key == pygame.K_LEFT:
        paddlebot.moving_left = False
        paddletop.moving_left = False
    elif event.key == pygame.K_DOWN:
        paddleside.moving_down = False
    elif event.key == pygame.K_UP:
        paddleside.moving_up = False

    # Player 2 movement keys
    elif event.key == pygame.K_d:
        ai_paddlebot.moving_right = False
        ai_paddletop.moving_right = False
    elif event.key == pygame.K_a:
        ai_paddlebot.moving_left = False
        ai_paddletop.moving_left = False
    elif event.key == pygame.K_s:
        ai_paddleside.moving_down = False
    elif event.key == pygame.K_w:
        ai_paddleside.moving_up = False


def check_events(ai_settings, screen, stats, sb, paddlebot, paddletop, paddleside, dashline, ai_paddlebot, ai_paddletop, ai_paddleside):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, paddlebot, paddletop, paddleside, ai_paddlebot, ai_paddletop, ai_paddleside)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddlebot, paddletop, paddleside, ai_paddlebot, ai_paddletop, ai_paddleside)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb,
                              paddlebot, paddletop, paddleside, ai_paddlebot, ai_paddletop, ai_paddleside,
                              dashline, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, sb, paddlebot, paddletop, paddleside, ai_paddlebot, ai_paddletop, ai_paddleside,
                      dashline, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""

    # When the player click button plays, then start the background music right away.
    background_music()
    if not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        dashline.empty()

        # Create a new fleet and center the ship.
        create_dashlines(ai_settings, screen, dashline)


def update_screen(ai_settings, screen, stats, sb, paddlebot, paddletop, paddleside, dashline, ai_paddlebot, ai_paddletop, ai_paddleside, ball):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets, behind ship and aliens.
    paddlebot.blitme()
    paddletop.blitme()
    paddleside.blitme()

    ai_paddlebot.blitme()
    ai_paddletop.blitme()
    ai_paddleside.blitme()

    ball.blitme()

    dashline.draw(screen)




    pygame.display.flip()


# Check Collision between ball and Player-Paddle-Side
def collide_check_1(ai_settings, ball, paddleside):
    if ball.rect.colliderect(paddleside.rect):
        hitSound = pygame.mixer.Sound("sounds/hit.wav")
        hitSound.play()
        ai_settings.fleet_direction_aliens_1 *= -1


# Check Collision between ball and AI-Paddle-Side
def collide_check_2(ai_settings, ball, ai_paddleside):
    if ball.rect.colliderect(ai_paddleside.rect):
        hitSound = pygame.mixer.Sound("sounds/hit.wav")
        hitSound.play()
        ai_settings.fleet_direction_aliens_1 *= -1


# Check Collision between ball and AI-Paddle-Bot
def collide_check_3(ai_settings, ball, ai_paddlebot):
    if ball.rect.colliderect(ai_paddlebot.rect):
        hitSound = pygame.mixer.Sound("sounds/hit.wav")
        hitSound.play()
        ai_settings.fleet_direction_aliens_1 *= -1


# Check Collision between ball and Paddle-Bot
def collide_check_4(ai_settings, ball, paddlebot):
    if ball.rect.colliderect(paddlebot.rect):
        hitSound = pygame.mixer.Sound("sounds/hit.wav")
        hitSound.play()
        ai_settings.fleet_direction_aliens_1 *= -1


# Check Collision between ball and Paddle-Top
def collide_check_5(ai_settings, ball, paddletop):
    if ball.rect.colliderect(paddletop.rect):
        hitSound = pygame.mixer.Sound("sounds/hit.wav")
        hitSound.play()
        ai_settings.fleet_direction_aliens_1 *= -1


# Check Collision between ball and AI-Paddle-Top
def collide_check_6(ai_settings, ball, ai_paddletop):
    if ball.rect.colliderect(ai_paddletop.rect):
        hitSound = pygame.mixer.Sound("sounds/hit.wav")
        hitSound.play()
        ai_settings.fleet_direction_aliens_1 *= -1


def serve_ball(ai_settings, screen):
    r = screen.get_rect()
    position = Vector(r.centerx, r.centery)
    vx = random.randint(10, 20)
    vy = random.randint(10, 20)
    vxsign = -1 if random.randint(10, 20) == 0 else 1
    vysign = -1 if random.randint(10, 20) == 0 else 1
    velocity = Vector(vxsign *vx, vysign * vy)
    return Ball(ai_settings, screen)


def create_dashlines(ai_settings, screen, dashline):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.

    # Create the fleet of aliens.
    for row_number in range(1):
        for alien_number in range(1):
            create_a_dash(ai_settings, screen, dashline, alien_number)


def create_a_dash(ai_settings, screen, dashline, alien_number7):   # Paddle-Side
    """Create an alien, and place it in the row."""
    divider = DashLine(ai_settings, screen)
    alien_width7 = divider.rect.width
    divider.x = 300 + 5 * alien_width7 * alien_number7
    divider.rect.x = divider.x
    divider.rect.y = 4
    dashline.add(divider)


