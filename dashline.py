"""
CPSC 386 - Ping Pong Game
Create a Pong game for 2 players
Player 1 Movement Keys: Arrows Keys
Player 2 Movement Keys: W A S D
Name: DAI KIEU
"""
import pygame
from pygame.sprite import Sprite


class DashLine(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(DashLine, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien image 3  and set its rect attribute.
        self.image = pygame.image.load('images/dashline.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def check_edges_3(self):
        """Return True if alien is at edge of screen."""

        screen_rect = self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

