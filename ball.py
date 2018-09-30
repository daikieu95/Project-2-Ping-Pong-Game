"""
CPSC 386 - Ping Pong Game
Create a Pong game for 2 players
Player 1 Movement Keys: Arrows Keys
Player 2 Movement Keys: W A S D
Name: DAI KIEU
"""
import pygame
from math import cos, sin
import random


class Ball:

    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.min_angle = 45
        self.max_angle = 135
        self.theta = 0

        self.image = pygame.image.load('images/ball.png')
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        # Store the alien's exact position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.x)
        self.theta = random.uniform(self.min_angle, self.max_angle)
        self.moving = False

    def check_edges_1(self):
        """Return True if alien is at edge of screen."""

        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def off_screen(self):
        r = self.rect
        rscreen = self.screen.get_rect()
        return (r.bottom <= -50) or (r.top >= rscreen.bottom) or (r.right >= 50)

    def update(self):
        """Move the fleet to the left."""

        self.x += (2 * self.ai_settings.fleet_direction_aliens_1) * cos(self.theta)
        self.rect.x = self.x
        self.y += (2 * self.ai_settings.fleet_direction_aliens_1) * sin(self.theta)
        self.rect.y = self.y

    def blitme(self):

        self.screen.blit(self.image, self.rect)