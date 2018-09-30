"""
CPSC 386 - Ping Pong Game
Create a Pong game for 2 players
Player 1 Movement Keys: Arrows Keys
Player 2 Movement Keys: W A S D
Name: DAI KIEU
"""
import pygame.font
from pygame.sprite import Group

from paddlebot import Paddle_Bot


class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (230, 230, 0)
        self.font = pygame.font.SysFont(None, 30)

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Turn the score into a rendered image."""
        bg = self.ai_settings.bg_color
        txt = self.text_color
        rscreen = self.screen_rect
        player_score_str = "{}".format(self.stats.player_score)
        self.player_score_image = self.font.render(player_score_str, True, txt, bg)

        self.player_score_rect = self.player_score_image.get_rect()
        rplayer = self.player_score_rect
        rplayer.right = rscreen.centerx + 80
        rplayer.top = 20

        ai_score_str = "{}".format(self.stats.ai_score)
        self.ai_score_image = self.font.render(ai_score_str, True, txt, bg)
        self.ai_score_rect = self.ai_score_image.get_rect()
        rai = self.ai_score_rect
        rai.right = rscreen.centerx - 80 + int(rai.width)
        rai.top = 20

        winning_score_str = "{}".format(self.winning_score)
        self.winning_score_image = self.text_font.render(winning_score_str, True, (255, 0, 0), bg)

        self.winning_score_rect = self.winning_score_image.get_rect()
        rwinning = self.winning_score_rect
        rwinning.right = rscreen.centerx + int(rwinning.width/2)
        rwinning.top = rai.bottom + 20

    def show_winner(self, stats):
        self.show_score()

        winner_str = "Player WINS!" if stats.player_score >= 15 else "AI WINS!"
        self.winner_image = self.font.render(winner_str, True, self.text_color, self.ai_settings.bg_color)
        self.winner_rect = self.winner_image.get_rect()
        self.screen.blit(self.winner_image, self.winner_rect)
        pygame.display.flip()



    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = 'Normal Mode'
        self.level_image = self.font.render(level_str, True,
                                            self.text_color, self.ai_settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Paddle_Bot(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self):
        """Draw score and balls to the screen."""
        pygame.draw.rect(self.screen, (255, 255, 255), self.player_score_rect, 6)
        self.screen.blit(self.player_score_image, self.player_score_rect)

        pygame.draw.rect(self.scren, (255, 255, 255), self.ai_score_rect, 6)
        self.screen.blit(self.ai_score_image, self.ai_score_rect)

        pygame.draw.rect(self.screen, (255, 255, 255), self.winning_score_rect, 3)
        self.screen.blit(self.winning_score_image, self.winning_score_rect)

        pygame.display.flip()

