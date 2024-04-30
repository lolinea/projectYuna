import pygame
from pygame import font

from models.pizza import Pizza

class Score:

	def __init__(self, MainGame):
		self.game = MainGame
		self.settings = MainGame.settings
		self.screen = MainGame.screen
		self.screen_rect = self.screen.get_rect()
		self.stats = MainGame.stats

		self.font = font.SysFont(self.settings.score_font, self.settings.score_font_size)

		self.update_score_image()
		self.update_high_score_image()
		self.update_level_image()

		self.pizzas = pygame.sprite.Group()
		self.update_pizza_image()

	def update_pizza_image(self):
		self.pizzas.empty()
		pizza = Pizza(self.game)

		pizza.image = pygame.transform.scale(pizza.image, (pizza.rect.width//30, pizza.rect.height//30))
		pizza.rect = pizza.image.get_rect()
		pizza_width = pizza.rect.width
		
		for every_pizza in range(self.stats.pizza_amount):
			pizza = Pizza(self.game)
			pizza.image = pygame.transform.scale(pizza.image, (pizza.rect.width//30, pizza.rect.height//30))
			pizza.rect = pizza.image.get_rect()
			pizza.rect.x = self.screen_rect.left + 2 + (every_pizza*pizza_width)
			pizza.rect.y = 5
			self.pizzas.add(pizza)

	def update_score_image(self):
		self.score_image = self.font.render(str(self.stats.score), True, self.settings.score_text_color)

		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.topright = self.screen_rect.topright

		self.score_image_rect.y += 7
		self.score_image_rect.x -= 5

	def update_high_score_image(self):
		self.high_score_image = self.font.render(str(self.stats.high_score), True, self.settings.score_text_color)

		self.high_score_image_rect = self.high_score_image.get_rect()
		self.high_score_image_rect.midtop = self.screen_rect.midtop

		self.high_score_image_rect.y += 7

	def check_high_score(self):
		if self.stats.score > self.stats.high_score:
			self.stats.high_score = self.stats.score
			self.update_high_score_image()

	def update_level_image(self):
		self.level_image = self.font.render(str(self.stats.game_level), True, self.settings.score_text_color)

		self.level_image_rect = self.level_image.get_rect()
		self.level_image_rect.topright = self.screen_rect.topright

		self.level_image_rect.x -= 6
		self.level_image_rect.y += 40

	def blitme(self):
		self.screen.blit(self.score_image, self.score_image_rect)
		self.screen.blit(self.high_score_image, self.high_score_image_rect)
		self.screen.blit(self.level_image, self.level_image_rect)
		self.pizzas.draw(self.screen)

