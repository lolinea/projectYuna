
class Stats:

	def __init__(self, MainGame):
		self.settings = MainGame.settings
		self.game_active = False
		self.replay_game = False
		self.yuna_amount = 1

		self.score = 0
		self.pizza_amount = 6
		self.game_level = 1
		self.high_score = 0

		self.reset_stats()

	def reset_stats(self):
		self.yuna_amount = 1

		self.score = 0
		self.pizza_amount = 6
		self.game_level = 1

		self.settings.yuna_speed_x = 5
		self.settings.yuna_speed_y = 3

		self.settings.yuna_size = 10