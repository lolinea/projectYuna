import sys
import pygame
import time

from random import randint

from configs.settings import Settings
from configs.stats import Stats
from configs.score import Score

from models.yuna import Yuna
from models.pizza import Pizza
from models.button import Button

class MainGame:

	def __init__(self):
		pygame.init()
		self.settings = Settings()
		self.stats = Stats(self)

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

		self.scoreboard = Score(self)
		self.pizza = Pizza(self)
		self.yunas = pygame.sprite.Group()

		self._create_fleet()

		self.title = pygame.display.set_caption(self.settings.title)

		self.play_button = Button(self, "Play")

	def run(self):
		while True:
			self._check_events()

			if self.stats.game_active :
				self._update_yuna()

			self._update_screen()

	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type == pygame.MOUSEBUTTONUP:
				mouse_pos = pygame.mouse.get_pos()
				self._check_button(mouse_pos)

			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._update_collide(mouse_pos)

	def _check_keydown_events(self, event):
		if event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_r:
			self.stats.game_active = False

	def _check_keyup_events(self, event):
		if event.key == pygame.K_r:
			self.stats.game_active = True

	def _check_button(self, mouse_pos):
		if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
			self.stats.game_active = True

			self.yunas.empty()
			self.stats.reset_stats()
			self.scoreboard.blitme()

			self._create_fleet()

	def _update_collide(self, mouse_pos):

		mouse_x, mouse_y = mouse_pos

		for yuna in self.yunas:
			if self.stats.game_active and yuna.rect.collidepoint(mouse_x, mouse_y): 
				#print("0")
				self.settings.yuna_speed_x *= 1.1
				self.settings.yuna_speed_y *= 1.1
				self.recreate = True
				self.settings.yuna_size += self.settings.yuna_shrink
				#self.stats.yuna_amount += 1
		
				self.stats.score += 10
				self.stats.game_level += 1

			else:
				#print("1")0
				self.recreate = False
				self.fail_to_hit()

		self.scoreboard.update_score_image()
		self.scoreboard.check_high_score()
		self.scoreboard.update_level_image()

		if self.recreate:
			self.yunas.empty()
			self._create_fleet()

	def fail_to_hit(self):
		if self.stats.game_active:
			self.stats.pizza_amount -= 1
			self.scoreboard.update_pizza_image()

			if self.stats.pizza_amount > 0:
				self.yunas.empty()

				self._create_fleet()

				time.sleep(1)

			else:
				self.stats.game_active = False
				pygame.mouse.set_visible(True)

	def _create_fleet(self):
		yuna = Yuna(self)
		amount_yuna = self.stats.yuna_amount
		
		for steps in range(amount_yuna):
			self._create_yuna()
		
	def _create_yuna(self):
		yuna = Yuna(self)

		yuna.rect.x = randint(0, 400)
		yuna.rect.y = randint(0, 400)

		self.yunas.add(yuna)

	def _update_yuna(self):
		self._check_img_edges()	
		self.yunas.update()

	def _check_img_edges(self):
		for yuna in self.yunas.sprites():
			if yuna.check_edge() == "b":
				for yuna in self.yunas.sprites():
					self.settings.yuna_speed_x *= -1

			elif yuna.check_edge() == "a":
				for yuna in self.yunas.sprites():
					self.settings.yuna_speed_y *= -1

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.scoreboard.blitme()
	
		self.yunas.draw(self.screen)

		if not self.stats.game_active:
			self.play_button.draw()

		self.pizza.blitme()	

		pygame.display.flip()
		pygame.time.Clock().tick(30)

if __name__ == '__main__':
	myGame = MainGame()
	myGame.run()