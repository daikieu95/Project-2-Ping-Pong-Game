"""
CPSC 386 - Ping Pong Game
Create a Pong game for 2 players
Player 1 Movement Keys: Arrows Keys
Player 2 Movement Keys: W A S D
Name: DAI KIEU
"""
import pygame
from pygame.sprite import Sprite


class Paddle_Side(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        super(Paddle_Side, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image, and get its rect.
        self.image = pygame.image.load('images/blue_paddle.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = 592 + self.screen_rect.centerx

        self.rect.top = 300 + self.screen_rect.top

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flags.
        self.moving_down = False
        self.moving_up = False

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

    def update(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        if self.moving_up or self.moving_down:
            self.rect.centery = self.centery

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
