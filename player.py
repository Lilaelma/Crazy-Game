import pygame


class Player(pygame.sprite.Sprite) :

	def __init__(self, x, y) :

		super().__init__()
		self.x = x
		self.y = y
		self.size = [35, 45]
		self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
		self.player_img = pygame.image.load("image/kit.png").convert_alpha()
		self.jump = 0
		self.jump_climb = 0
		self.jump_descent = 5
		self.number_jump = 0
		self.jumped = False


	def move(self, speed) :

		self.rect.x += speed

	def ft_print(self, area) :

		#pygame.draw.rect(area, (255, 75, 0), self.rect)
		area.blit(self.player_img, self.rect)

	def ft_jump(self) :

		if self.jumped :
			if self.jump_climb >= 10 :
				self.jump_descent -= 1
				self.jump = self.jump_descent

			else :
				self.jump_climb += 1
				self.jump = self.jump_climb

			if self.jump_descent < 0 :
				self.jump_climb = 0
				self.jump_descent = 5
				self.jumped = False

		self.rect.y = self.rect.y - (8 * (self.jump / 2))