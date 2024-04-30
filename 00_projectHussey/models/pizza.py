import pygame
from pygame.sprite import Sprite

class Pizza(Sprite):

	def __init__(self, MainGame):
		super().__init__()

		self.screen = MainGame.screen
		self.settings = MainGame.settings
		self.screen_rect = MainGame.screen.get_rect()

		self.image = pygame.image.load(self.settings.pizza_img)
		self.rect = self.image.get_rect()
		self.image = pygame.transform.scale(self.image, (self.rect.width//30, self.rect.height//30))

	def _update_cursor(self):
		pygame.mouse.set_visible(False)

		self.cursor = self.image.convert_alpha()

	def blitme(self):
		self._update_cursor()
		self.screen.blit(self.cursor, (pygame.mouse.get_pos())) 
