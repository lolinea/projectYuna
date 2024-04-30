import pygame
from pygame.sprite import Sprite
from random import randint

class Yuna(Sprite):

	def __init__(self, MainGame):

		super().__init__()
		self.screen = MainGame.screen
		self.screen_rect = self.screen.get_rect()
		self.settings = MainGame.settings
		self.stats = MainGame.stats

		self.image = pygame.image.load(self.settings.yuna_img)
		self.rect = self.image.get_rect()
		if self.settings.yuna_size <= 20:
			self.image = pygame.transform.scale(self.image, (self.rect.width//self.settings.yuna_size, self.rect.height//self.settings.yuna_size))
		else:
			self.image = pygame.transform.scale(self.image, (self.rect.width//20, self.rect.height//20))


		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

	def update(self):
		self.rect.x += self.settings.yuna_speed_x
		self.rect.y += self.settings.yuna_speed_y

	def check_edge(self):
		if (self.rect.x >= self.screen_rect.right) or (self.rect.left <= 0):
			return "b"

		elif (self.rect.top <= 0) or (self.rect.y >= self.screen_rect.bottom)  :
			return "a"