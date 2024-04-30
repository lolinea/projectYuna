from pygame import font
import pygame

class Button:

	def __init__(self, MainGame, text):
		self.settings = MainGame.settings
		self.screen = MainGame.screen
		self.screen_rect = self.screen.get_rect()

		self.rect = pygame.Rect(0, 0, self.settings.button_width, self.settings.button_height)
		self.rect.center = self.screen_rect.center

		self.change_text(text)

	def change_text(self, text):
		self.font = font.SysFont(self.settings.button_font, self.settings.button_font_size)
		self.text = self.font.render(text, True, self.settings.button_text_color)

		self.text_rect = self.text.get_rect()
		self.text_rect.center = self.rect.center

	def draw(self):
		pygame.draw.rect(self.screen, self.settings.button_color, self.rect)
		self.screen.blit(self.text, self.text_rect)