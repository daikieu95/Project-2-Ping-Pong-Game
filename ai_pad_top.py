"""
CPSC 386 - Ping Pong Game
Create a Pong game for 2 players
Player 1 Movement Keys: Arrows Keys
Player 2 Movement Keys: W A S D
Name: DAI KIEU
"""
import pygame
from pygame.sprite import Sprite


class AI_Paddle_Top(Sprite):

    def __init__(self, ai_settings, screen):
        """Initialize the ship, and set its starting position."""
        super(AI_Paddle_Top, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image, and get its rect.
        self.image = pygame.image.load('images/red_paddle_horizontal.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = -350 + self.screen_rect.centerx
        self.rect.top = self.screen_rect.top

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

    def update(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < 600:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
